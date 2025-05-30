# 🌍✈️ PlanVoyage – Gemini-Powered Travel Itinerary Generator

**PlanVoyage** is a Flask-based web application that leverages **Google's Gemini AI** to craft personalized travel itineraries. Just enter your **destination**, **trip duration**, and **budget** – and let the AI do the rest!

---
[Live Demo](https://planvoyage-oi97.onrender.com/)
## 💡 Features

* 🗓️ Day-wise sightseeing itineraries
* 🍽️ Local food suggestions & cultural tips
* 🏨 Budget stay recommendations
* 🏥 Nearby hospitals for emergencies
* ⚡ Powered by Google Gemini (Generative AI)
* 📱 Clean, responsive user interface

---

## 🚀 Tech Stack

* **Backend**: Python (Flask)
* **AI Integration**: Google Generative AI (Gemini)
* **Frontend**: HTML, CSS, JavaScript
* **Other**: CORS enabled for local API communication

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/reshanajk006/planvoyage.git
cd planvoyage
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate        # For macOS/Linux
venv\Scripts\activate           # For Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Your Gemini API Key

Open `app.py` and replace:

```python
GOOGLE_API_KEY = "your-api-key-here"
```

with your actual **Google Gemini API key**.

### 5. Run the App

```bash
python server.py
```

### 6. Access the App

Open your browser and go to:

```
http://localhost:5000
```

---

## 🌐 Deployment Guide (Heroku or Railway)

Ensure the following files are present in your project directory:

* `Procfile`
* `requirements.txt`

---

## 📄 License

This project is licensed under the **MIT License**.
Feel free to use, modify, and share!

---

