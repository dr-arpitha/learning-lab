#### Building a Simple Chatbot with Gemini LLM

In today’s guide we will be creating a chatbot using modern large language models (LLMs). We’ll walk through how to build a simple chatbot powered by **Google’s Gemini LLM** using Python. Feel free to use any of the other LLMs(OpenAI’s models, Meta’s Llama, Anthropic models) if you prefer.

You can view this sample program at [Google Colab](https://colab.research.google.com/drive/1QSoinUItV8q6O8jE1RxQp0sU_SYdfMuY?usp=sharing)
 
Prerequisites
-------------

Before you begin, make sure you have:

*   An **API key** from the [Google AI Studio](https://aistudio.google.com/) (You may have to create a dummy cloud project to generate the API key)
    
*   Python installed on your system
    

### Install pip (if not already installed)

pip is Python’s package manager. Most modern Python installations come with it, but if you don’t have it:

*   On **Windows/Mac/Linux**, download [get-pip.py](https://bootstrap.pypa.io/get-pip.py) and run:
 
 ``` python get-pip.py  ```

*   To check if pip is installed, run:
    

  `   pip --version   `

### Install the Google Generative AI SDK

Once pip is ready, install the Gemini SDK:

  `   pip install google-generativeai   `

Summary Of How Code Works
-------------------------

1.  **Initialize the SDK** – The script imports and configures the Gemini model with your API key. You can use any of the [gemini models listed](https://ai.google.dev/gemini-api/docs/models). We will be using “gemini-2.5-flash” in this guide.
    
2.  **System Prompt** – We added instructions that guide the chatbot to generate only humorous and safe responses. This is done to avoid LLM responses going rogue, as an additional safety net.
    
3.  **Start a Chat Session** – start\_chat() creates a conversational context.
    
4.  **User Interaction** – The program loops, accepting user input and passing it to Gemini.
    
5.  **Response Generation** – The model generates a clean, funny reply.
    

Writing the Chatbot
-------------------

Here’s a chatbot that **only produces humorous, light-hearted responses** while avoiding any racist, vulgar, or harmful content.

- Clone the code from this directory.

Testing the Chatbot in Google Colab
-----------------------------------

If you don’t want to set up Python locally, you can test your chatbot directly in the cloud using **Google Colab**.

### Steps:

1.  Open [Google Colab](https://colab.research.google.com/).
    
2.  Click on **New Notebook**.
    
3.  In the first cell, install the Gemini SDK:
    

  `   !pip install google-generativeai   `

1.  In the next cell, paste your chatbot code.
    
2.  Replace “GOOGLE\_API\_KEY“ with your Gemini API key.
    
3.  Run the cells with **Shift + Enter**.
    

Colab will open an input prompt directly in the notebook, and you can chat with your bot there!

💡 **Tip**: Always keep your API key a secret.

Example Conversation
--------------------

```   
Chatbot is ready! 
Type ‘exit’ or ‘quit’ to stop.  
You: Tell me something about cats.  
Chatbot: Cats are basically ninjas in fur coats… but with less discipline and way more naps. 🐱💤  
You: Give me career advice.  
Chatbot: Sure! Be like a kangaroo—always take big leaps, but keep something in your pouch for snacks. 🦘😂   
```

Congratulations, you’ve just created your first **humorous Gemini-powered chatbot**! 🎉

##### 📚 Getting Started Guides

*   [Google Gemini](https://ai.google.dev/gemini-api/docs/quickstart)
    
*   [OpenAI](https://platform.openai.com/docs/overview)
    
*   [Anthropic Claude](https://docs.claude.com/en/docs/get-started)
    

#### 🌐 Stay Connected

*   👉 [Subscribe to our newsletter](https://aiengarena.com/) to hear about upcoming events, challenges, and seminars.
    
*   💬 [Join our Discord](https://discord.gg/NY2rJY7N) to brainstorm ideas, ask questions, and get support from the community.
    
*   📸 [Follow us on Instagram](https://www.instagram.com/aiengarena) for updates and insights.
    

Happy learning & coding,

– The AI Arena Team