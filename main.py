from crew import run_travel_planner


def get_input(prompt, default=None):
    value = input(prompt).strip()

    if not value and default is not None:
        return default

    return value


if __name__ == "__main__":

    print("\n🌍 AI Travel Planner")
    print("=" * 60)

    source = get_input(
        "🚉 Starting Location: "
    )

    destination = get_input(
        "📍 Destination: "
    )

    days = int(
        get_input(
            "📅 Number of Days: "
        )
    )

    budget = int(
        get_input(
            "💰 Total Budget (₹): "
        )
    )

    travel_type = get_input(
        "👥 Travel Type (solo/couple/family/friends): "
    )

    travelers = get_input(
        "🧳 Number of Travelers: "
    )

    transport_type = get_input(
        "🚆 Transport (flight/train/bus/car): "
    )

    interest = get_input(
        "🎯 Interest (history/food/adventure/nature/shopping): "
    )

    hotel_preference = get_input(
        "🏨 Hotel Preference (budget/standard/luxury): "
    )

    print("\n⏳ Creating itinerary...\n")

    result = run_travel_planner(
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

    print("\n" + "=" * 60)
    print("✈️ YOUR TRAVEL PLAN")
    print("=" * 60)

    print(result)

    with open(
        "travel_plan.txt",
        "w",
        encoding="utf-8"
    ) as file:
        file.write(str(result))

    print("\n📄 Travel plan saved to travel_plan.txt")