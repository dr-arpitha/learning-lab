import os

import google.generativeai as genai

# Configure the API key
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

# Create the model with a system prompt
system_instruction = (
    "You are a friendly and humorous chatbot. "
    "Always respond with light-hearted jokes, puns, or funny remarks. "
    "Avoid anything offensive, racist, vulgar, or harmful. "
    "If a user asks something serious, reply with a playful, clean, and funny twist."
)

model = genai.GenerativeModel(
    "gemini-2.5-flash",
    system_instruction=system_instruction
)

# Start a conversation
chat = model.start_chat()

print("Chatbot is ready! Type 'exit' or 'quit' to stop.")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Chatbot: Goodbye! Remember to laugh today!")
        break
    response = chat.send_message(user_input)
    print("Chatbot:", response.text)
