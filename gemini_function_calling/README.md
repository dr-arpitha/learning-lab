#### Beginner Guide: Gemini LLM and Function Calling

**Function calling** (also known as **tool calling**) is a powerful feature of modern language models, where the model doesn’t just generate text — it can **decide when and how to use external functions** (tools) to solve a problem.

Instead of hardcoding every step, you define a set of **tools (functions)** with input/output schemas, and the LLM:

*   Understands your request
    
*   Selects the right tool(s)
    
*   Fills in the parameters
    
*   Executes them automatically
    
*   Continues the conversation using the results
    

### When is Function Calling Useful?

Without function calling:

*   You write and run each function manually.
    
*   The LLM just gives instructions or summaries.
    

With function calling:

*   The LLM **calls your code itself** — like a smart assistant.
    
*   It can orchestrate workflows using your tools.
    

### Using Gemini LLM + Function Calling to Fetch Real-Time Weather

#### Step 1: Prerequisites

*   A **Google Gemini API Key** – [get one here](https://aistudio.google.com/app/api-keys)
    
*   A **Free OpenWeatherMap API Key** – [sign up](https://openweathermap.org/api)
    
*   Python installed (3.8+ recommended)
    

#### Install dependencies

```   pip install google-generativeai requests  ```

#### Step 2: Set Your API Keys

You’ll need to set your API keys as environment variables.

In your terminal or at the top of your script:

```
export GOOGLE_API_KEY=”your-gemini-api-key”  
export OPENWEATHER_API_KEY=”your-openweather-api-key”
```

In Python:

``` 
import os  os.environ[”GOOGLE_API_KEY”] = “your-gemini-api-key”
os.environ[”OPENWEATHER_API_KEY”] = “your-openweather-api-key”
```

#### Step 3: The Python Code

Clone the source code from this directory. 

### Step-by-Step Breakdown

#### Step 1: Define the Weather Tool (Function)

You create a simple function called get\_weather(city) that:

*   Hits OpenWeatherMap’s API
    
*   Parses the temperature and description
    
*   Returns a readable sentence like:
    

> “The current weather in Paris is clear sky with a temperature of 19°C.”

#### Step 2: Register the Function with Gemini

```  model = genai.GenerativeModel(model_name=”gemini-2.5-flash”, tools=[get_weather])  ```

This tells Gemini:

> “Hey, here’s a tool you can use if the user asks about the weather.”

#### Step 3: Gemini Makes the Call

When the user types:

> “Can you tell me the weather in Paris?”

Gemini thinks:

> “I should call the get\_weather function with city=’Paris’.”

You inspect the function\_call, run the function, and get the result.

#### Step 4: Add Some Fun!

Instead of just returning the raw weather info, you send it **back into Gemini** with this custom prompt:

```
prompt = f”“”You are a humorous weather assistant.   
Use the below weather information to generate a funny weather update back to user  Weather: {result}  “”“
 ```

This is where models shine—**turning plain info into personality**.

### Example Output

**User:** “What’s the weather in Paris?”

**Gemini Function Call:**

```   get_weather(city=”Paris”)  ```

**Weather API Response:**

> “The current weather in Paris is light rain with a temperature of 18°C.”

**Funny Gemini Response:**

> “Grab your umbrella and pretend you’re in a romantic movie—Paris is serving up some light rain with a cool 18°C. Bonus points if you twirl in it!”

#### **References and Reading Material**

\- [Gemini Function Calling](https://ai.google.dev/gemini-api/docs/function-calling)

\- [OpenAI Function Calling](https://platform.openai.com/docs/guides/function-calling)

#### **🌐 Stay Connected**

\- 👉 [Subscribe to our newsletter](https://aiengarena.com/) to hear about upcoming events, challenges, and seminars.

\- 💬 [Join our Discord](https://discord.gg/NY2rJY7N) to brainstorm ideas, ask questions, and get support from the community.

\- 📸 [Follow us on LinkedIn](https://www.linkedin.com/company/aiengarena/) for updates and insights.

\- 📸 [Follow us on Instagram](https://www.instagram.com/aiengarena) for updates and insights.

Happy learning & coding,

– The AI Arena Team
