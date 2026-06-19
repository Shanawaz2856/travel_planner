from crewai import Task

from agents import (
    hotel_agent,
    transport_agent,
    food_agent,
    weather_agent,
    itinerary_agent
)


def create_tasks(
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

    # Budget Allocation
    hotel_budget = int(budget * 0.40)
    transport_budget = int(budget * 0.25)
    food_budget = int(budget * 0.20)
    activity_budget = int(budget * 0.15)

    # ---------------- HOTEL TASK ----------------
    hotel_task = Task(
        description=f"""
        Find 3 hotel options in {destination}.

        Requirements:
        - Hotel Preference: {hotel_preference}
        - Total Hotel Budget: ₹{hotel_budget}
        - Number of Travelers: {travelers}
        - Trip Duration: {days} days

        Return:
        - Hotel Name
        - Location
        - Price Per Night
        - Total Stay Cost
        - Amenities
        - Why Recommended

        IMPORTANT:
        Stay within the allocated hotel budget.
        """,
        expected_output="3 hotel recommendations with costs and amenities.",
        agent=hotel_agent
    )

    # ---------------- TRANSPORT TASK ----------------
    transport_task = Task(
        description=f"""
        Plan transportation.

        Source: {source}
        Destination: {destination}

        Preferred Transport:
        {transport_type}

        Transport Budget:
        ₹{transport_budget}

        Include:
        - Recommended route
        - Estimated fare
        - Travel duration
        - Local transportation options
        - Approximate local transport costs

        IMPORTANT:
        Stay within the transport budget.
        """,
        expected_output="Transportation plan with estimated costs.",
        agent=transport_agent
    )

    # ---------------- FOOD TASK ----------------
    food_task = Task(
        description=f"""
        Recommend food options in {destination}.

        Travelers:
        {travelers}

        Travel Type:
        {travel_type}

        Interests:
        {interest}

        Food Budget:
        ₹{food_budget}

        Include:

        Day-wise:
        - Breakfast
        - Lunch
        - Dinner

        Mention:
        - Restaurant Name
        - Local Dish
        - Estimated Cost

        IMPORTANT:
        Total food expenses must stay within budget.
        """,
        expected_output="Day-wise food recommendations and costs.",
        agent=food_agent
    )

    # ---------------- WEATHER TASK ----------------
    weather_task = Task(
        description=f"""
        Provide weather information for {destination}.

        Include:
        - Expected temperature
        - Rainfall chances
        - Best clothing suggestions
        - Packing recommendations
        - Travel advisories if any
        """,
        expected_output="Weather forecast and packing suggestions.",
        agent=weather_agent
    )

    # ---------------- FINAL ITINERARY TASK ----------------
    itinerary_task = Task(
        description=f"""
        Create a COMPLETE TRAVEL ITINERARY.

        Trip Details:

        Source: {source}
        Destination: {destination}
        Days: {days}
        Travelers: {travelers}
        Travel Type: {travel_type}
        Transport Type: {transport_type}
        Interests: {interest}
        Hotel Preference: {hotel_preference}

        TOTAL BUDGET:
        ₹{budget}

        ACTIVITY BUDGET:
        ₹{activity_budget}

        IMPORTANT RULES:

        1. Activities must match interests:
           - food → food streets, restaurants, food tours
           - nature → parks, lakes, gardens
           - history → forts, museums, monuments
           - shopping → markets, malls
           - adventure → trekking, adventure activities

        2. Create a realistic day-wise itinerary.

        3. Include:
           - Morning
           - Afternoon
           - Evening

        4. Mention estimated costs.

        5. Verify total budget.

        6. If budget exceeds ₹{budget},
           replace expensive options with cheaper alternatives.

        OUTPUT FORMAT:

        ====================================================
        TRIP SUMMARY
        ====================================================

        Route:
        {source} → {destination}

        Travelers:
        {travelers}

        Travel Type:
        {travel_type}

        Transport:
        {transport_type}

        ====================================================
        DAY 1
        ====================================================

        Morning:
        Afternoon:
        Evening:

        ====================================================
        DAY 2
        ====================================================

        Morning:
        Afternoon:
        Evening:

        Continue for all days.

        ====================================================
        WEATHER
        ====================================================

        Weather summary

        ====================================================
        BUDGET BREAKDOWN
        ====================================================

        Hotel:
        Transport:
        Food:
        Activities:

        Total Cost:

        Remaining Budget:

        Budget Status:
        WITHIN BUDGET / OVER BUDGET
        """,
        expected_output="Complete travel itinerary with budget validation.",
        agent=itinerary_agent,
        context=[
            hotel_task,
            transport_task,
            food_task,
            weather_task
        ]
    )

    return [
        hotel_task,
        transport_task,
        food_task,
        weather_task,
        itinerary_task
    ]