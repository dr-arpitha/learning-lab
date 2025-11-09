## Getting Started with Hugging Face: Running Models Using the Inference Client

Hugging Face has become one of the most important platforms in the machine learning ecosystem. It provides access to thousands of pre-trained models for natural language processing (NLP), computer vision, speech recognition, and more. With its open-source libraries and cloud-based inference tools, developers can easily build and deploy AI-powered applications without managing heavy infrastructure or training models from scratch.

In this post, we will explore what Hugging Face is, and how to use the Inference Client to run a sentiment analysis model.

We will also do a brief comparison between Hugging Face, LLMs and [OLLAMA](https://aiengarena.substack.com/p/local-llms-using-ollama)

-------------

### What Is Hugging Face?

Hugging Face has quickly evolved into a hub for machine learning innovation. The company is best known for maintaining the “Transformers” library, which provides implementations of state-of-the-art models such as BERT, GPT, RoBERTa, and DistilBERT.

Beyond open-source tools, Hugging Face offers a cloud-based ecosystem for model hosting, dataset sharing, and collaboration. The Hugging Face Hub is a centralized platform where you can find over tens of thousands of datasets, models and prebuilt applications (Spaces) created by the community.

-------------

### LLMs vs. Hugging Face’s Broader Model Ecosystem

It’s easy to associate Hugging Face primarily with language models, but its ecosystem is much broader. Understanding this distinction clarifies why Hugging Face is more than just an LLM platform.


#### What Are LLMs?

Large Language Models (LLMs) are transformer-based models designed to understand and generate human language. Examples include GPT, Llama, and Mistral.They handle text-centric tasks like:

*   Generation and summarization
    
*   Question answering
    
*   Code generation
    
*   Translation
    
*   Chat and reasoning
    

#### Hugging Face’s Broader Scope

Hugging Face supports not only LLMs but also models across many domains:

*   **Computer Vision**: image classification, object detection
    
*   **Speech and Audio**: transcription, speaker ID
    
*   **Multimodal**: combining text and images
    
*   **Reinforcement Learning**, **tabular**, and **time-series** models
    

In short, Hugging Face is a universal model hub, not limited to text.

Every LLM can live on Hugging Face, but not every Hugging Face model is an LLM.This diversity makes Hugging Face a go-to platform for end-to-end AI development, from natural language to vision and beyond.

-------------

### Hugging Face Inference API

The **Inference API** allows you to run models hosted on the Hugging Face Hub directly through a simple HTTP request. You can send text, images, or audio data to a model endpoint and get back predictions in JSON format. This means you don’t need to install heavy libraries or configure GPU environments locally.

The API can handle a wide variety of tasks, including:

*   Sentiment analysis
    
*   Text generation
    
*   Question answering
    
*   Image classification
    
*   Text summarization
    
*   Translation
    

Hugging Face manages all the underlying compute and scaling. You only need an API token and an endpoint URL.

-------------

### Using the Hugging Face Inference Client in Python

To simplify communication with the API, Hugging Face provides an official Python package called "huggingface\_hub". It includes an **InferenceClient** class that wraps the API in a user-friendly way.

#### Step 1: Install the required package

```
pip install huggingface_hub  

```

#### Step 2: Authenticate with your Hugging Face token

If you don’t have a token yet, create one from your [Hugging Face account settings](https://huggingface.co/settings/tokens).

Ensure the API token has access to Inference calls. **It is NOT enabled by default.**

Then, set it as an environment variable:

  
```
export HUGGINGFACEHUB_API_TOKEN=”your_api_token_here” 
 ```

-------------

### Running Sentiment Analysis with the Inference API

Let’s use sentiment analysis as an example. We’ll use the model "distilbert-base-uncased-finetuned-sst-2-english", which is trained to classify text as either positive or negative.

Run the code in this directory.
 

Example output:
``` 
[TextClassificationOutputElement(label=’NEGATIVE’, score=0.9946038126945496), TextClassificationOutputElement(label=’POSITIVE’, score=0.005396206863224506)]  
```   


The model predicts that the sentence expresses a negative sentiment more.

-------------

### Using Hugging Face Locally and Privately

While Hugging Face provides powerful cloud APIs, you can also run models entirely locally, ensuring that your data never leaves your environment. This is important for users or organizations with privacy, compliance, or data security concerns.

#### 1\. Run Models Locally with Transformers

You can download and run models using the transformers library:

``` 
from transformers import pipeline  
classifier = pipeline(”sentiment-analysis”, model=”distilbert-base-uncased-finetuned-sst-2-english”)  
result = classifier(”I love running models locally with Hugging Face!”)  
print(result)
```


Once downloaded, all computation runs offline. You can also manually download models:

```   
huggingface-cli download distilbert-base-uncased-finetuned-sst-2-english  
 ```

Then load it directly:

```
classifier = pipeline(”sentiment-analysis”, model=”./path/to/local/model”) 
```
No data leaves your machine during inference.

#### 2\. Use Offline Mode

You can ensure that Hugging Face makes no network calls by enabling offline mode:

```
export TRANSFORMERS_OFFLINE=1
```

This guarantees all operations use cached files only.

#### 3\. Private and On-Premise Deployment

For larger or team-based setups:

*   **Private model repositories** on Hugging Face let you control who can access your models.
    
*   **Inference Endpoints (private cloud)** allow enterprise-grade, isolated deployments, even inside your own virtual private cloud (VPC).
    
-------------

### Conclusion

Hugging Face has revolutionized how developers access and deploy AI models. The Inference API and InferenceClient make cloud-based inference effortless, while the Transformers library enables fully private, local execution.

Compared to Ollama’s LLM-focused local approach, Hugging Face offers a broader, more flexible ecosystem, covering text, vision, audio, and multimodal tasks. Whether you need a simple sentiment classifier or an enterprise-grade private deployment, Hugging Face provides the tools to scale from experimentation to production securely and efficiently.

-------------

#### **References**

\- [Hugging Face](https://huggingface.co/)

-------------

#### **🌐 Stay Connected**

\- 👉 [Subscribe to our newsletter](https://aiengarena.com/) to hear about upcoming events, challenges, and seminars.

\- 💬 [Join our Discord](https://discord.gg/NY2rJY7N) to brainstorm ideas, ask questions, and get support from the community.

\- 📸 [Follow us on LinkedIn](https://www.linkedin.com/company/aiengarena/) for updates and insights.

\- 📸 [Follow us on Instagram](https://www.instagram.com/aiengarena) for updates and insights.

Happy learning & coding,

– The AI Arena Team