import os
from huggingface_hub import InferenceClient

api_key=os.environ["HUGGINGFACEHUB_API_TOKEN"]

client = InferenceClient(token=api_key, model="distilbert/distilbert-base-uncased-finetuned-sst-2-english")

result = client.text_classification(
    text="Overall, the movie was good, but at times I found it to be a bit dragging"
)

print(result)