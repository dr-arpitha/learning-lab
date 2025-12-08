from crewai import Agent, Task, Crew, LLM
from dotenv import load_dotenv
import os
#
# Load secrets from .env file
load_dotenv()

gemini_llm = LLM(
    model="gemini-2.5-flash", 
    api_key=os.getenv("GOOGLE_API_KEY"),
    provider="google"
)

# Agent 1: Master Travel Planner
planner_agent = Agent(
    name="Trip Planner",
    role="Master travel planner",
    goal="Break down the travel planning into stays, food, and activities.",
    backstory=(
        "An expert travel consultant responsible for creating trip blueprints "
        "based on destination, duration, budget, and preferences."
    ),
    llm=gemini_llm,
    verbose=True
)

# Agent 2: Stay Suggestion Agent
stay_agent = Agent(
    name="Hotel & Stay Specialist",
    role="Find and summarize best stay options",
    goal="Provide several stay options at the destination based on preferences.",
    backstory=(
        "A hospitality expert who finds hotels, Airbnbs, and stays "
        "matching the user's travel style and budget."
    ),
    llm=gemini_llm,
    verbose=True
)

# Agent 3: Restaurant Agent
restaurant_agent = Agent(
    name="Food & Restaurants Specialist",
    role="Find restaurants near the provided stays",
    goal="Recommend restaurants close to each stay option.",
    backstory=(
        "A culinary expert who identifies food options around each stay."
    ),
    llm=gemini_llm,
    verbose=True
)

# Agent 4: Activities Agent
activity_agent = Agent(
    name="Activities & Attractions Specialist",
    role="Find attractions and activities near stays",
    goal="Suggest kid-friendly, budget-friendly or preference-based activities.",
    backstory=(
        "An expert in attractions and things to do based on trip preferences."
    ),
    llm=gemini_llm,
    verbose=True
)

def build_travel_tasks(destination, days, preferences):
    return [

        # Task 1 – Trip Breakdown
        Task(
            description=(
                f"Create a plan outline for a trip to {destination} for {days} days. "
                f"Consider preferences: {preferences}. "
                f"Break the plan into: stay options, restaurants, and activities."
            ),
            expected_output=(
                f"Create a plan outline for a trip to {destination} for {days} days. "
                f"Consider preferences: {preferences}. "
                f"Break the plan into: stay options, restaurants, and activities."
            ),
            agent=planner_agent,
            output_key="trip_outline"
        ),

        # Task 2 – Find Stays
        Task(
            description=(
                f"Using the trip_outline, find 4–6 stay options in/near {destination}. "
                f"Consider budget and family/kid preferences: {preferences}."
            ),
            expected_output=(
                f"Using the trip_outline, find 4–6 stay options in/near {destination}. "
                f"Consider budget and family/kid preferences: {preferences}."
            ),
            agent=stay_agent,
            output_key="stay_options"
        ),

        # Task 3 – Find Restaurants near Each Stay
        Task(
            description=(
                f"For each stay option from stay_options, find nearby restaurants "
                f"in line with preferences {preferences}. Output must be grouped by stay."
            ),
            expected_output=(
                f"For each stay option from stay_options, find nearby restaurants "
                f"in line with preferences {preferences}. Output must be grouped by stay."
            ),
            agent=restaurant_agent,
            output_key="restaurants_near_stays"
        ),

        # Task 4 – Find Activities near Each Stay
        Task(
            description=(
                f"For each stay option from stay_options, find nearby activities, "
                f"sightseeing, adventure, or kid-friendly attractions based on {preferences}. "
                f"Output must be grouped by stay."
            ),
            expected_output=(
                f"For each stay option from stay_options, find nearby activities, "
                f"sightseeing, adventure, or kid-friendly attractions based on {preferences}. "
                f"Output must be grouped by stay."
            ),
            agent=activity_agent,
            output_key="activities_near_stays"
        )

    ]

# -----------------------------------------------------------
# 5. CREATE CREW & RUN WORKFLOW
# -----------------------------------------------------------

def run_travel_planner(destination, days, preferences):

    tasks = build_travel_tasks(destination, days, preferences)

    crew = Crew(
        agents=[planner_agent, stay_agent, restaurant_agent, activity_agent],
        tasks=tasks,
        verbose=True
    )

    result = crew.kickoff()

    return result

if __name__ == "__main__":
    destination = "TIGNES, France"
    days = 5
    preferences = {
        "budget": "medium",
        "activities": "culture, food, sightseeing",
        "kids": "yes"
    }

    final_output = run_travel_planner(destination, days, preferences)
    print("\n\n=================== FINAL OUTPUT ===================\n")
    print(final_output)

