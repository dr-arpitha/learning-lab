import os
from google import genai
from mem0 import MemoryClient

# Set your Gemini and Mem0 key
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
memory_client = MemoryClient(api_key=os.environ["MEM0_API_KEY"])

def fitness_advisor_with_memory(user_input, client_id="client001"):

    # Retrieve memories
    mem_results = memory_client.search(user_input, filters={"user_id": client_id})
    memories = [m["memory"] for m in mem_results.get("results", [])]

    mem_text = "\n".join(f"- {m}" for m in memories) or "(no prior data)"

    prompt = f"""
You are a fitness tutor.

User memory:
{mem_text}

Respond to this message using what you know about their current health limitation,
 fitness goal, their learning pace, preferences, strengths, and weaknesses:

"{user_input}"
"""

    response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt)
    answer = response.text

    # Update memory
    memory_client.add(
        [
            {"role": "user", "content": user_input},
            {"role": "assistant", "content": answer},
        ],
        user_id=client_id
    )

    return answer

def main():
    print("\n ********* AI Fitness Advisor ********* \n")
    print("Type 'exit' to quit.\n")

    while True:
        fitness_client_input = input("User: ").strip()
        if fitness_client_input.lower() == "exit":
            break

        reply = fitness_advisor_with_memory(fitness_client_input, client_id="client001")
        print("Fitness Advisor:", reply, "\n")

if __name__ == "__main__":
    main()
