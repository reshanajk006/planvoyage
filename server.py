from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
from flask_cors import CORS
import markdown2
import os

app = Flask(__name__)
CORS(app)

GOOGLE_API_KEY = "AIzaSyBDXN_mym1PMgNa1UQggGNljy1rFt9fxp8"  # Replace with your Gemini API key
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/trip-plan', methods=['POST'])
def plan_trip():
    data = request.get_json()
    location = data.get("location")
    days = data.get("days")
    budget = data.get("budget")

    if not location or not days or not budget:
        return jsonify({"error": "Location, days, and budget are required"}), 400

    prompt = f"""
I want to travel to {location} for {days} days with a total budget of ₹{budget}.
Make it engaging and realistic for a first-time traveler. Format the response using basic HTML tags like <b>, <ul>, <li>, <p> instead of Markdown.

Include the following for each day:
- Sightseeing plan with locations
- Local food or dishes to try that fit the budget
- Budget-friendly travel and stay options
- Safety tips or cultural notes for travelers

Also provide nearby recommendations for:
- Affordable hospitals or clinics
- Budget-friendly hotels or homestays
- Popular restaurants, bars, and cafés
- Any lesser-known but worthwhile attractions

Keep the suggestions practical and suitable for someone on a ₹{budget} budget.
Structure it clearly day-wise and ensure it’s beginner-friendly.
"""


    try:
        response = model.generate_content(prompt)
        html_response = markdown2.markdown(response.text)
        return jsonify({"plan": html_response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
