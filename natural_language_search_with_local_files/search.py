import faiss
import numpy as np
from tqdm import tqdm

from google import genai

from pathlib import Path
from PyPDF2 import PdfReader
from docx import Document

TEXT_EXTENSIONS = {".txt", ".md", ".py", ".json", ".csv"}
client = genai.Client()
EMBED_MODEL = "gemini-embedding-001"

def extract_text(path: Path) -> str:
    try:
        if path.suffix == ".pdf":
            reader = PdfReader(str(path))
            return "\n".join(p.extract_text() or "" for p in reader.pages)

        if path.suffix == ".docx":
            doc = Document(str(path))
            return "\n".join(p.text for p in doc.paragraphs)

        if path.suffix in TEXT_EXTENSIONS:
            return path.read_text(errors="ignore")

    except Exception:
        return ""

    return ""

def embed_text(text: str) -> list[float]:
    result = client.models.embed_content(
        model=EMBED_MODEL,
        contents=text,
    )

    return result.embeddings[0].values

class GeminiFileIndex:
    def __init__(self):
        self.index = None
        self.paths = []

    def build(self, root_dir: str):
        embeddings = []
        root = Path(root_dir).expanduser()

        for path in tqdm(root.rglob("*")):
            print(path)
            if not path.is_file():
                continue

            text = extract_text(path)
            if not text.strip():
                continue

            vector = embed_text(text[:8000])  # truncate for cost & speed
            embeddings.append(vector)
            self.paths.append(str(path))


        dim = len(embeddings[0])
        self.index = faiss.IndexFlatL2(dim)
        self.index.add(np.array(embeddings).astype("float32"))

    def save(self, path="file_index.faiss"):
        faiss.write_index(self.index, path)

    def save_path(self, path="file_path.txt"):
        with open(path, "w", encoding="utf-8") as f:
            for path in self.paths:
                f.write(path)
                f.write("\n")
                print(path)


    def load(self, path="file_index.faiss"):
        self.index = faiss.read_index(path)

    def load_path(self, path="file_path.txt"):
        with open(path, encoding="utf-8") as f:
            for line in f:
                self.paths.append(line.rstrip("\n"))

def semantic_search(query: str, index: GeminiFileIndex, top_k=2):
    query_vec = embed_text(query)
    query_vec = np.array([query_vec]).astype("float32")

    distances, indices = index.index.search(query_vec, top_k)

    return [index.paths[i] for i in indices[0]]


if __name__ == "__main__":
    index = GeminiFileIndex()

    # Run once to build index and path
    # index.build("~/Documents/")
    # index.save()
    # index.save_path()

    #Later reuse
    index.load()
    index.load_path()

    while True:
        q = input("AI Search>")
        if q.lower() in ["exit", "quit"]:
            print("AI Search: Goodbye! Remember to laugh today!")
            break
        results = semantic_search(q, index)
        for r in results:
            print("•", r)
