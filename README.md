````markdown
# PlanVoyage - Gemini-Powered Travel Itinerary Generator 🌍✈️

PlanVoyage is a Flask web app that uses Google's Gemini AI to generate customized travel itineraries. Just enter your destination, duration, and budget, and let the AI do the rest!

## 💡 Features

- Generate day-wise sightseeing itineraries
- Suggest local food and cultural tips
- Recommends budget stays and hospitals
- Gemini-powered content generation
- Clean, responsive UI

## 🚀 Tech Stack

- Python (Flask)
- Google Generative AI (Gemini)
- HTML, CSS, JavaScript
- CORS enabled for local testing

## 🛠️ Setup Instructions

1. **Clone the repo**
   ```bash
   git clone https://github.com/reshanajk006/planvoyage.git
   cd planvoyage
````

2. **Create a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set your Gemini API Key**

   Replace the value of `GOOGLE_API_KEY` in `app.py` with your own Google Gemini API key.

5. **Run the app**

   ```bash
   python server.py
   ```

6. **Visit**

   ```
   http://localhost:5000
   ```

## 🌐 Deployment (Heroku or Railway)

Make sure these files exist:

* `Procfile`
* `requirements.txt`

Then deploy using your preferred cloud service.

---

## 📝 License

MIT License

````
