import os
import requests
import google.generativeai as genai

# Set up API keys
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
OPENWEATHER_API_KEY = os.environ["OPENWEATHER_API_KEY"]

# 1. Weather Lookup Function
def get_weather(city: str) -> str:
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}&units=metric"
    response = requests.get(url)
    
    if response.status_code != 200:
        return f"Sorry, I couldn't fetch the weather for {city}."

    data = response.json()
    temp = data['main']['temp']
    desc = data['weather'][0]['description']
    return f"The current weather in {city} is {desc} with a temperature of {temp}°C."

# === CREATE GEMINI MODEL WITH TOOL USE ===

model = genai.GenerativeModel(model_name="gemini-2.5-flash", tools=[get_weather])

# 4. Start the chat session
chat = model.start_chat()

# 5. Send a user message that should trigger the function
user_input = "Can you tell me the weather in Paris?"
response = chat.send_message(user_input)

# 6. Handle the tool/function call
for candidate in response.candidates:
    if candidate.content.parts and hasattr(candidate.content.parts[0], "function_call"):
        function_call = candidate.content.parts[0].function_call
        print(f"Gemini wants to call: {function_call.name} with args: {function_call.args} \n")

        if function_call.name == "get_weather":
            city = function_call.args["city"]
            result = get_weather(city)

            # Send the result back to Gemini
            model = genai.GenerativeModel(model_name="gemini-2.5-flash")
            prompt = f"""You are a humorous weather assistant. 
            Use the below weather information to generate a funny weather update back to user
            Weather: {result}
            """
            final_response = model.generate_content(prompt)
            print("Weather update: \n", final_response.text)
    else:
        print("Gemini replied directly:", response.text)

