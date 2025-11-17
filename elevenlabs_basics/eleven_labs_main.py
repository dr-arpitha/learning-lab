import re
import requests
from pypdf import PdfReader
from bs4 import BeautifulSoup
from elevenlabs.client import ElevenLabs
import os

# -----------------------------------------------------
API_KEY = os.environ["ELEVENLABS_API_KEY"]
# -----------------------------------------------------

elevenlabs = ElevenLabs(api_key=API_KEY)


# -----------------------------
# Extract text from PDF
# -----------------------------
def extract_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"
    return text


# -----------------------------
# Extract text from URL (HTML newsletters)
# -----------------------------
def extract_from_url(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    # Remove scripts and styles
    for tag in soup(["script", "style"]):
        tag.extract()

    text = soup.get_text(separator="\n")
    return re.sub(r"\n+", "\n", text).strip()  # Cleanup


# -----------------------------
# Clean text (optional)
# -----------------------------
def clean_text(text):
    # Remove repeated whitespace
    text = re.sub(r"\n{2,}", "\n\n", text)

    # Remove extremely long blank areas
    return text.strip()


# -----------------------------
# Convert text → MP3 using ElevenLabs
# -----------------------------
def text_to_audio(text, output_file="newsletter.mp3", voice="Rachel"):
    print("Generating audio...")

    audio_stream = elevenlabs.text_to_speech.convert(
        voice_id="JBFqnCBsd6RMkjVDRZzb",
        model_id="eleven_multilingual_v2",
        text=text
    )

    with open(output_file, "wb") as f:
        for chunk in audio_stream:
            f.write(chunk)

    print(f"Saved audio to {output_file}")


# -----------------------------
# MASTER FUNCTION
# -----------------------------
def convert_newsletter_to_audio(source, source_type="pdf", out_file="newsletter.mp3"):
    if source_type == "pdf":
        text = extract_from_pdf(source)
    elif source_type == "url":
        text = extract_from_url(source)
    elif source_type == "text":
        text = source
    else:
        raise ValueError("source_type must be 'pdf', 'url', or 'text'.")

    text = clean_text(text)
    text_to_audio(text, output_file=out_file)


# -----------------------------
# RUN EXAMPLES
# -----------------------------
if __name__ == "__main__":
    # OPTION 1: Newsletter PDF
    # convert_newsletter_to_audio("newsletter.pdf", source_type="pdf")

    # OPTION 2: Newsletter URL
    #convert_newsletter_to_audio("https://open.substack.com/pub/aiengarena/p/turn-your-newsletters-into-audio", source_type="url")

    # OPTION 3: Pasted Text
    sample_newsletter = """
        Weekly Tech Newsletter - Nov 2025
        ---------------------------------
        🚀 AI is reshaping the world...
        📱 New iPhone details leak...
        🌍 Climate report shows...
        """
    convert_newsletter_to_audio(sample_newsletter, source_type="text", out_file="sample_newsletter.mp3")



