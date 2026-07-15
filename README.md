# OptiCrop &mdash; Smart Agricultural Production Optimization Engine

# OptiCrop
# 🌾 OptiCrop – Smart Agricultural Production Optimization Engine

An intelligent Machine Learning-based web application that recommends the most suitable crop for a plot of land using soil and climate data, helping farmers, agribusinesses, and agricultural researchers make faster, more accurate, and data-driven planting decisions.

---

## 📌 Project Overview

OptiCrop is a Machine Learning-based web application developed to recommend the most suitable crop for cultivation. The system analyzes soil nutrient levels and climate conditions and predicts the crop most likely to give the best yield.

The application applies **K-Means clustering** to uncover soil/climate patterns and trains a **Logistic Regression** classifier for crop prediction, integrating the trained model into a **Flask** web application for real-time crop recommendation.

---

## Live Application Link 👇

https://opti-crop-rcxf.onrender.com 🔗

---

## 🎯 Problem Statement

Farmers often select crops based on habit, tradition, or guesswork rather than the actual soil and climate conditions of their land, which can lead to poor yield and financial loss.

OptiCrop addresses this challenge by automating crop suitability assessment using Machine Learning, enabling farmers and agricultural stakeholders to:

- Reduce reliance on guesswork
- Improve crop selection accuracy
- Optimize the use of water, fertilizer, and soil nutrients
- Get instant, data-driven crop recommendations

---

# 🚀 Key Features

| Feature | Description |
|----------|-------------|
| ✅ Crop Recommendation | Predicts the most suitable crop instantly |
| ✅ Data Preprocessing | Cleans and prepares soil/climate data |
| ✅ Outlier Handling | Removes outliers using the IQR method |
| ✅ Exploratory Data Analysis | Understands data patterns and relationships |
| ✅ K-Means Clustering | Groups similar soil/climate conditions |
| ✅ Logistic Regression Model | Classifies the best-suited crop |
| ✅ Flask Web Application | Real-time prediction through an interactive web interface |
| ✅ Crop Description | Shows a short, farmer-friendly reason for the recommendation |
| ✅ Cloud Ready | Easily deployable on Render, PythonAnywhere, or similar platforms |

---

# 🏗️ System Architecture

```
                    +----------------------+
                    |      User Layer      |
                    |----------------------|
                    | Farmers              |
                    | Agricultural Advisors |
                    | Researchers/Policy    |
                    +----------+-----------+
                               |
                               ▼
                    +----------------------+
                    |   Frontend Layer     |
                    |----------------------|
                    | HTML Templates       |
                    | CSS                  |
                    | Responsive Forms     |
                    +----------+-----------+
                               |
                               ▼
                    +----------------------+
                    | Flask Application    |
                    |----------------------|
                    | Request Handling     |
                    | Input Validation     |
                    | Prediction Engine    |
                    | Result Rendering     |
                    +----------+-----------+
                               |
                               ▼
                    +----------------------+
                    | Machine Learning     |
                    |----------------------|
                    | Data Preprocessing   |
                    | K-Means Clustering   |
                    | Model Training       |
                    | Model Evaluation     |
                    | Logistic Regression  |
                    +----------+-----------+
                               |
                               ▼
                    +----------------------+
                    | Deployment Layer     |
                    |----------------------|
                    | Render / Local Server|
                    | Web Browser Access   |
                    +----------------------+
```

---

# 📊 Dataset Information

| Feature | Description |
|----------|-------------|
| Nitrogen (N) | Soil nitrogen content ratio |
| Phosphorous (P) | Soil phosphorous content ratio |
| Potassium (K) | Soil potassium content ratio |
| Temperature | Ambient temperature (°C) |
| Humidity | Relative humidity (%) |
| pH | Soil pH value |
| Rainfall | Rainfall (mm) |
| Label | Recommended crop (22 crop classes) |

---

# 🔍 Data Preprocessing

The following preprocessing techniques were applied before model training:

- Null Value Checking
- Outlier Detection & Removal (IQR method)
- Seasonal Crop Extraction
- Feature/Target Split
- Train/Test Split
- Data Cleaning & Validation

---

# 🤖 Machine Learning Models

| Model | Purpose | Status |
|--------|----------|--------|
| K-Means Clustering | Groups similar soil/climate conditions (elbow method used to choose cluster count) | ✅ Trained |
| Logistic Regression | Classifies the most suitable crop | ⭐ Best / Deployed Model |

---

# 📈 Model Performance

| Metric | Value |
|---------|-------|
| Best Algorithm | Logistic Regression |
| Test Accuracy | **98%** |
| Macro Avg F1-score | **0.95** |
| Prediction Type | Multi-class Classification (22 crops) |

The trained **Logistic Regression** model was selected for deployment due to its high accuracy and fast, reliable predictions.

---

# ⚙️ Technology Stack

## Programming Language

- Python

## Libraries

| Library | Purpose |
|----------|---------|
| NumPy | Numerical Computing |
| Pandas | Data Manipulation |
| Matplotlib | Data Visualization |
| Seaborn | Statistical Visualization |
| Scikit-learn | Machine Learning (K-Means, Logistic Regression) |

## Web Framework

- Flask

## Frontend

- HTML5
- CSS3
- JavaScript

## Deployment

- Browser based (local host) / Render

---

## 📂 Repository Structure

```text
📁 1. Brainstorming & Ideation
│── Brainstorm & Idea Prioritization.pdf
│── Define Problem Statements.pdf
│── Empathize Map.pdf

📁 2. Requirements Analysis
│── Customer Journey Map.pdf
│── Data Flow Diagram.pdf
│── Solution Requirements.pdf
│── Technology Stack.pdf

📁 3. Project Design Phase
│── Problem-Solution Fit.pdf
│── Proposed Solution.pdf
│── Solution Architecture.pdf

📁 4. Project Planning Phase
│── Project Planning.pdf

📁 5. Project Development Phase
│── Coding & Solution.pdf
│── Code-Layout, Readability and Reusability.pdf
│── No. of Functional Features Included in the Solution.pdf

📁 6. Project Testing
│── Performance Testing.pdf

📁 7. Project Documentation
│── Project Executable Files.pdf
│── Sample Project Documentation.pdf

📁 8. Project Demonstration
│── Communication.pdf
│── Demonstration of Proposed Features.pdf
│── Project Demo Planning.pdf
│── Scalability & Future Plan.pdf
│── Team Involvement in Demonstration.pdf

📁 Project Demo Video
│── README.md (add your demo video link)

📁 Project Code Files
│── data/
│── ├── Crop_recommendation.csv
│── ├── generate_dataset.py
│── model/
│── ├── train_model.py
│── ├── model.pkl
│── ├── plots/
│── app/
│── ├── app.py
│── ├── static/style.css
│── ├── templates/
│── ├── ├── base.html
│── ├── ├── home.html
│── ├── ├── about.html
│── ├── ├── findyourcrop.html
│── requirements.txt
│── README.md
```

---

# 📂 OptiCrop Project Code File Structure

```
Project Code Files/
│
├── data/
│    ├── Crop_recommendation.csv
│    └── generate_dataset.py
├── model/
│    ├── train_model.py
│    ├── model.pkl
│    └── plots/
├── app/
│    ├── app.py
│    ├── static/
│    │    └── style.css
│    └── templates/
│         ├── base.html
│         ├── home.html
│         ├── about.html
│         └── findyourcrop.html
├── requirements.txt
└── README.md
```

---

# 🔄 Application Workflow

1. User enters soil and climate readings (N, P, K, temperature, humidity, pH, rainfall).
2. Flask validates the input.
3. Data is preprocessed and formatted.
4. Features are passed to the trained Logistic Regression model.
5. The model predicts the most suitable crop.
6. The recommended crop and a short description are displayed to the user.

---

# 💼 Business Use Cases

| Use Case | Description |
|----------|-------------|
| Smart Crop Recommendation | Instantly recommend the best crop for a farmer's soil and climate |
| Crop Suitability Assessment | Check whether current conditions suit a specific crop |
| Agricultural Research & Policy | Analyze crop-environment patterns for evidence-based planning |
| Resource Optimization | Improve use of water, fertilizer, and soil nutrients |

---

# 🎓 Learning Outcomes

Through this project, the following skills were developed:

- Machine Learning Model Development
- Data Cleaning & Preprocessing
- Outlier Detection (IQR method)
- Exploratory Data Analysis (EDA)
- Unsupervised Learning (K-Means Clustering)
- Classification Algorithms (Logistic Regression)
- Model Evaluation
- Flask Web Development
- Machine Learning Deployment
- End-to-End AI Application Development

---

# 🚀 Installation

### Clone the Repository

```bash
git clone https://github.com/<your-username>/OptiCrop
```

### Navigate to the Project

```bash
cd OptiCrop/"Project Code Files"
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
cd app
python app.py
```

## Local Host server

```bash
http://127.0.0.1:5000
```

---

# 🌐 Usage

1. Open the application in your browser.
2. Go to **Find your crop**.
3. Enter the soil and climate readings (N, P, K, temperature, humidity, pH, rainfall).
4. Click **Recommend a crop**.
5. View the recommended crop and its description.

---

# 🔮 Future Enhancements

- Cloud Deployment & Database Integration
- User Authentication & Admin Dashboard
- Recommendation History & Analytics Dashboard
- Additional ML Models (Random Forest, XGBoost) for comparison
- Weather API Integration for live climate data
- Multi-language Support (regional languages for farmers)
- Explainable AI (SHAP/LIME) for recommendation reasoning
- REST API Support
- Docker Deployment

---

## Live Application Link 👇

[https://opti-crop-rcxf.onrender.com] 🔗

---

# 👨‍💻 Author

## K.Hemanth Kumar

🎓 **B.Tech – Computer Science & Management (CSM)**

🏫 **Anantha Lakshmi Institute of Technology and Sciences**

### 📫 Connect with Me

| Platform | Profile |
|----------|---------|
| 🐙 GitHub | [] |
| 💼 LinkedIn | [] |

---

# ⭐ Acknowledgements

This project was developed as part of the **SmartBridge AI & Machine Learning Virtual Internship Program** to demonstrate the practical application of **Machine Learning** and **Flask** in solving real-world agricultural crop recommendation problems.

### Special Thanks

- Faculty members and mentors for their guidance and support.
- Anantha Lakshmi Institute of Technology and Sciences for providing the academic environment to complete this project.
- The open-source community for providing powerful libraries such as **NumPy**, **Pandas**, **Scikit-learn**, **Matplotlib**, **Seaborn**, and **Flask**.
- Everyone who contributed feedback and ideas during the development of this project.

---

**This project is intended for educational and learning purposes.**
