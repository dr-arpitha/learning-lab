from ollama import generate
# Regular response
response = generate('llama2', 'Explain why one should not use local LLMs or disadvantages?')
print(response['response'])