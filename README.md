# 🌍 AI Travel Planner

An AI-powered travel planning application built using CrewAI, Streamlit, OpenRouter, and Serper API.

The application generates complete travel itineraries based on the user's destination, budget, travel style, interests, hotel preference, and transportation choice.

---

## 🚀 Features

- Hotel Recommendations
- Transportation Planning
- Food Recommendations
- Weather Analysis
- Budget Validation
- Day-wise Travel Itinerary
- Interest-based Trip Planning
- Streamlit Web Interface

---

## 🛠️ Tech Stack

- Python
- Streamlit
- CrewAI
- OpenRouter
- Serper API
- Prompt Engineering

---

## 📂 Project Structure

```text
travel_planner/
│
├── app.py
├── agents.py
├── crew.py
├── tasks.py
├── tools.py
├── config.py
├── requirements.txt
├── README.md
├── .gitignore
└── .env
```

---

## 🤖 AI Agents

### Hotel Recommendation Agent
Finds hotels based on:
- Budget
- Location
- Hotel Preference
- Number of Travelers

### Transport Planning Agent
Plans:
- Flights
- Trains
- Buses
- Cars
- Local Transportation

### Food Recommendation Agent
Suggests:
- Breakfast
- Lunch
- Dinner
- Local Cuisine
- Food Experiences

### Weather Analysis Agent
Provides:
- Weather Forecast
- Packing Suggestions
- Travel Advice

### Master Itinerary Agent
Combines all information and generates:
- Day-wise Itinerary
- Activity Suggestions
- Budget Breakdown
- Final Travel Plan

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-travel-planner.git

cd ai-travel-planner
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file:

```env
OPENROUTER_API_KEY=your_openrouter_api_key
SERPER_API_KEY=your_serper_api_key
```

---

## ▶️ Run Application

```bash
streamlit run app.py
```

---

## 📝 User Inputs

The application accepts:

- Starting Location
- Destination
- Budget
- Number of Days
- Number of Travelers
- Travel Type
- Transport Type
- Interests
- Hotel Preference

---

## 📊 Output

The generated travel plan includes:

- Trip Summary
- Day-wise Activities
- Hotel Recommendations
- Transportation Plan
- Food Recommendations
- Weather Information
- Budget Breakdown
- Budget Validation

---

## 💡 Example Use Cases

- Solo Travel Planning
- Family Vacations
- Couple Trips
- Friends Group Tours
- Budget Travel Planning

---

## 🔮 Future Improvements

- Google Maps Integration
- Hotel Images
- Weather Cards
- Budget Charts
- PDF Export
- Flight APIs
- Booking Links
- Multi-City Planning

---

## 👨‍💻 Author

Developed as an AI-powered travel planning project using CrewAI and Streamlit.