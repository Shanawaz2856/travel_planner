from crewai import Crew, Process

from agents import (
    hotel_agent,
    transport_agent,
    food_agent,
    weather_agent,
    itinerary_agent
)

from tasks import create_tasks


def run_travel_planner(
    source,
    destination,
    budget,
    days,
    travel_type,
    travelers,
    transport_type,
    interest,
    hotel_preference
):

    tasks = create_tasks(
        source=source,
        destination=destination,
        budget=budget,
        days=days,
        travel_type=travel_type,
        travelers=travelers,
        transport_type=transport_type,
        interest=interest,
        hotel_preference=hotel_preference
    )

    crew = Crew(
        agents=[
            hotel_agent,
            transport_agent,
            food_agent,
            weather_agent,
            itinerary_agent
        ],
        tasks=tasks,
        process=Process.sequential,
        verbose=False
    )

    result = crew.kickoff()

    return result