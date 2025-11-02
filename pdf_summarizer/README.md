#### Turn PDFs into Podcasts: Summarize, Translate, and Speak Any Document

- Do you ever find yourself drowning in lengthy PDFs, research papers, or reports? 
- Do you manually translate every document that is not in your preferred language?
- Do you want to listen to these documents while you multitask?  
- Do you want to send a summary of your document to a friend/relative in their preferred language?

These are the problems I am tackling today. 

Reading through lengthy PDF documents can be time-consuming — especially if they’re in another language. 
Today we will be using Google’s Gemini Large Language Model (LLM) to summarize a document, translate it, and listen to the spoken version — all with a few lines of Python.

**Note**: The audio file generated is of wave format and this program is tested ONLY on MAC OS .

-------------
#### Key Features

- **PDF Summarization:** Extracts key ideas, facts, and insights in seconds.
- **Multilingual Output:** Supports translation and speech in any language of your choice.
- **Text-to-Speech Integration:** Converts summaries into smooth, realistic audio.
- **Powered by Gemini LLM:** Ensures high-quality, context-aware summaries.
-------------
#### Prerequisites

You’ll need:

- A Google API key (for Gemini) → [Get one here](https://aistudio.google.com/app/api-keys)
- Export your Gemini API key:

  ```
  export GOOGLE_API_KEY="your-gemini-api-key"
  ```

- Python 3.9+

- Install the dependencies:

    ```   
    pip install google-genai  
    ```
-------------

#### The Python Code

Clone the source code from this directory. 

#### Run the script:
You have to provide absolute path to your PDF file and the target language as user input (ex: English, Kannada, Dutch, French)

Sample Run:

```
bash-3.2$ python main.py
Enter your file absolute path: /Users/xxx/Downloads/sample_pdf_to_summarise.pdf
Enter your language the document should be summarised in: Kannada
```

#### **References and Reading Material**

- [Speech Generation - Beta](https://ai.google.dev/gemini-api/docs/speech-generation)
- [Gemini TTS](https://docs.cloud.google.com/text-to-speech/docs/gemini-tts)


#### **🌐 Stay Connected**

- [Subscribe to our newsletter](https://aiengarena.com/) to hear about upcoming events, challenges, and seminars.

- [Join our Discord](https://discord.gg/NY2rJY7N) to brainstorm ideas, ask questions, and get support from the community.

- [Follow us on LinkedIn](https://www.linkedin.com/company/aiengarena/) for updates and insights.

- [Follow us on Instagram](https://www.instagram.com/aiengarena) for updates and insights.

Happy learning & coding,

– The AI Arena Team
 


