import streamlit as st
from crew import run_travel_planner

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="AI Travel Planner",
    page_icon="🌍",
    layout="wide"
)

# -----------------------------
# Title
# -----------------------------
st.title("🌍 AI Travel Planner")
st.markdown("Plan your trip using CrewAI + OpenRouter")

st.divider()

# -----------------------------
# Input Section
# -----------------------------
col1, col2 = st.columns(2)

with col1:
    source = st.text_input(
        "🚉 Starting Location",
        placeholder="e.g. Hyderabad"
    )

    destination = st.text_input(
        "📍 Destination",
        placeholder="e.g. Jaipur"
    )

    days = st.number_input(
        "📅 Number of Days",
        min_value=1,
        max_value=30,
        value=3
    )

    budget = st.number_input(
        "💰 Total Budget (₹)",
        min_value=1000,
        value=10000,
        step=1000
    )

with col2:
    travel_type = st.selectbox(
        "👥 Travel Type",
        ["solo", "couple", "family", "friends"]
    )

    travelers = st.number_input(
        "🧳 Number of Travelers",
        min_value=1,
        value=1
    )

    transport_type = st.selectbox(
        "🚆 Transport Type",
        ["flight", "train", "bus", "car"]
    )

    hotel_preference = st.selectbox(
        "🏨 Hotel Preference",
        ["budget", "standard", "luxury"]
    )

interest = st.multiselect(
    "🎯 Interests",
    [
        "food",
        "nature",
        "history",
        "shopping",
        "adventure",
        "culture",
        "wildlife",
        "nightlife"
    ]
)

st.divider()

# -----------------------------
# Generate Button
# -----------------------------
if st.button("🚀 Generate Travel Plan"):

    if not source or not destination:
        st.error("Please enter both source and destination.")
        st.stop()

    try:

        with st.spinner("⏳ Creating your personalized itinerary..."):

            result = run_travel_planner(
                source=source,
                destination=destination,
                budget=budget,
                days=days,
                travel_type=travel_type,
                travelers=travelers,
                transport_type=transport_type,
                interest=", ".join(interest),
                hotel_preference=hotel_preference
            )

        st.success("✅ Travel Plan Generated Successfully!")

        st.divider()

        # Summary Metrics
        c1, c2, c3, c4 = st.columns(4)

        with c1:
            st.metric("Budget", f"₹{budget:,}")

        with c2:
            st.metric("Days", days)

        with c3:
            st.metric("Travelers", travelers)

        with c4:
            st.metric("Transport", transport_type.title())

        st.divider()

        # Travel Plan Output
        st.subheader("✈️ Your Travel Plan")

        st.markdown(str(result))

        st.divider()

        # Download Button
        st.download_button(
            label="📄 Download Travel Plan",
            data=str(result),
            file_name="travel_plan.txt",
            mime="text/plain"
        )

    except Exception as e:
        st.error(f"Error: {str(e)}")