import os
import time
import google.generativeai as genai

from pinecone import Pinecone,ServerlessSpec

# Initialize a Pinecone client with your API key
pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])
# Configure genai keys
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

# Create a dense index with integrated embedding
index_name = "rag-gemini-demo"

# Delete old one if it exists
if index_name in [i["name"] for i in pc.list_indexes()]:
    pc.delete_index(index_name)

# Create with correct dimension
if index_name not in [idx["name"] for idx in pc.list_indexes()]:
    pc.create_index(
        name=index_name,
        dimension=3072,
        metric="cosine",
	spec=ServerlessSpec(cloud="aws", region="us-east-1")
    )

# Sample Knowledge base
documents = [
    {
        "id": "doc1",
        "text": "Our company offers a 30-day refund policy for all digital products. "
                "Refunds are processed within 5 business days after approval."
    },
    {
        "id": "doc2",
        "text": "Technical support is available 24/7 via email or live chat. "
                "Most issues are resolved within 48 hours."
    },
    {
        "id": "doc3",
        "text": "RAG = Retrieval + Generation. Gemini provides smart generation, and Pinecone provides fast retrieval. "
		" Combine them to create your own AI assistant that can answer domain-specific questions accurately."
    },
    {
        "id": "doc4",
        "text": "Pinecone is a fully-managed vector database that indexes, stores, and retrieves vectors. In the era of generative AI, databases like Pinecone are what help many software engineers and data scientists quickly build applications or perform analysis."
    },
    {
        "id": "doc5",
        "text": "Gemini API & Google AI Studio: An approachable way to explore and prototype with generative AI applications."
    }
]


# Target the index
dense_index = pc.Index(index_name)

# Embed text
def embed_text(text: str):
    result = genai.embed_content(
        model="gemini-embedding-001",
        content=text
    )
    return result["embedding"]

vectors = []
for doc in documents:
    embedding = embed_text(doc["text"])
    vectors.append({"id": doc["id"], "values": embedding, "metadata": {"text": doc["text"]}})

# Upsert to Pinecone
dense_index.upsert(vectors=vectors, namespace="rag-gemini-namespace")

# Extend the sleep time if necessary
time.sleep(20)
print("Documents indexed in Pinecone.")

# Check that vectors exist
stats = dense_index.describe_index_stats()
print(stats)

query = "How do I request a refund for a digital product?"
#query = "What is Pinecone?"
query_embedding = embed_text(query)

results = dense_index.query(vector=query_embedding, top_k=2, include_metadata=True, namespace="rag-gemini-namespace")
context = "\n".join([match["metadata"]["text"] for match in results["matches"]])

prompt = f"""You are a helpful assistant.
Use the following information from our knowledge base to answer the question.

Context:
{context}

Question: {query}

Answer:"""

model = genai.GenerativeModel("gemini-2.5-flash")
response = model.generate_content(prompt)

print("\n Query:", query)
print("\n Answer:\n", response.text)
