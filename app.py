"""
app.py
------
OptiCrop - Smart Agricultural Production Optimization Engine
Flask backend that loads the trained Logistic Regression model and
serves the Home, About, and FindYourCrop pages.
"""

import os
import pickle

import numpy as np
import pandas as pd
from flask import Flask, render_template, request

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "model", "model.pkl")

app = Flask(__name__)

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

FEATURE_COLUMNS = ["nitrogen", "phosphorous", "potassium", "temperature", "humidity", "ph", "rainfall"]

# Short, farmer-friendly blurbs shown alongside the prediction
CROP_INFO = {
    "rice": "Thrives in warm, humid conditions with heavy rainfall and standing water.",
    "maize": "A versatile cereal crop that prefers warm days and moderate rainfall.",
    "chickpea": "A cool-season legume that does well in low humidity and moderate soil fertility.",
    "kidneybeans": "Grows best in cool, moderately humid climates with well-drained soil.",
    "pigeonpeas": "A hardy legume tolerant of a wide range of temperature and rainfall.",
    "mothbeans": "A drought-resistant crop suited to hot, arid regions.",
    "mungbean": "Prefers warm temperatures and high humidity with moderate rainfall.",
    "blackgram": "Grows well in warm, moderately humid conditions.",
    "lentil": "A cool-climate legume needing moderate rainfall and fertile soil.",
    "pomegranate": "Prefers a dry climate with high humidity and moderate rainfall for fruiting.",
    "banana": "Needs rich soil, high nitrogen, warm temperatures and steady rainfall.",
    "mango": "A tropical fruit tree that thrives in hot temperatures with moderate humidity.",
    "grapes": "Requires high phosphorous and potassium with a wide temperature tolerance.",
    "watermelon": "Prefers warm temperatures, high humidity, and sandy, nutrient-rich soil.",
    "muskmelon": "Grows best in warm temperatures with very high humidity and low rainfall.",
    "apple": "A temperate fruit crop needing high potassium and moderate cool temperatures.",
    "orange": "Citrus crop that favors high humidity and a wide temperature range.",
    "papaya": "A fast-growing tropical fruit tolerant of a wide range of rainfall.",
    "coconut": "Needs consistently high humidity, warm temperatures, and heavy rainfall.",
    "cotton": "Requires high nitrogen, warm temperatures, and moderate rainfall.",
    "jute": "A fibre crop that needs high humidity and heavy rainfall.",
    "coffee": "Grows best in warm, humid climates with consistent rainfall.",
}


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/findyourcrop", methods=["GET", "POST"])
def findyourcrop():
    prediction = None
    info = None
    form_values = {}

    if request.method == "POST":
        try:
            form_values = {
                "nitrogen": request.form.get("nitrogen", ""),
                "phosphorous": request.form.get("phosphorous", ""),
                "potassium": request.form.get("potassium", ""),
                "temperature": request.form.get("temperature", ""),
                "humidity": request.form.get("humidity", ""),
                "ph": request.form.get("ph", ""),
                "rainfall": request.form.get("rainfall", ""),
            }

            values = [float(form_values[col]) for col in FEATURE_COLUMNS]
            input_df = pd.DataFrame([values], columns=FEATURE_COLUMNS)

            result = model.predict(input_df)[0]
            prediction = result
            info = CROP_INFO.get(result, "")
        except (ValueError, TypeError):
            prediction = "Invalid input. Please enter valid numeric values."

    return render_template(
        "findyourcrop.html",
        prediction=prediction,
        info=info,
        form_values=form_values,
    )


if __name__ == "__main__":
    app.run(debug=True)