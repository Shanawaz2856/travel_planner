import os
from pathlib import Path
from dotenv import load_dotenv

from crewai import Agent, LLM
from tools import search_tool

load_dotenv(Path(__file__).parent / ".env")

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

if not OPENROUTER_API_KEY:
    raise ValueError("OPENROUTER_API_KEY not found")

openrouter_llm = LLM(
    model="openrouter/qwen/qwen3-coder:free",
    api_key=OPENROUTER_API_KEY
)

hotel_agent = Agent(
    role="Hotel Recommendation Specialist",
    goal="Find hotels within the user's budget",
    backstory="Expert hotel consultant.",
    tools=[search_tool],
    llm=openrouter_llm,
    verbose=False
)

transport_agent = Agent(
    role="Transport Planner",
    goal="Plan cost effective transportation",
    backstory="Expert travel logistics planner.",
    tools=[search_tool],
    llm=openrouter_llm,
    verbose=False
)

food_agent = Agent(
    role="Food Expert",
    goal="Recommend budget friendly food options",
    backstory="Expert food critic.",
    tools=[search_tool],
    llm=openrouter_llm,
    verbose=False
)

weather_agent = Agent(
    role="Weather Analyst",
    goal="Provide weather insights",
    backstory="Weather specialist.",
    tools=[search_tool],
    llm=openrouter_llm,
    verbose=False
)

itinerary_agent = Agent(
    role="Master Itinerary Planner",
    goal="Create a complete travel itinerary within budget",
    backstory="Senior travel planner.",
    llm=openrouter_llm,
    verbose=False
)
budget_agent = Agent(
    role="Budget Auditor",
    goal="Ensure the itinerary stays within budget",
    backstory="""
    You are a travel budget expert.
    You verify all calculations and ensure
    the trip remains financially feasible.
    """,
    llm=openrouter_llm,
    verbose=False
)