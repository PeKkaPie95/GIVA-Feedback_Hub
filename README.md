# Feedback Hub

This repository contains **Feedback Hub**, a customer feedback analysis system developed for **Giva Jewelry**. The project enables users to submit product reviews, performs **rule-based sentiment analysis**, detects key product-related themes, and generates **actionable insights** displayed through a visual dashboard.

The application is built using **Flask** for the backend and **HTML/JavaScript** for the frontend, with a strong emphasis on transparent logic, keyword-based rules, and careful handling of edge cases such as negations and star–sentiment mismatches.

---

## Project Overview

Feedback Hub is designed to help analyze customer reviews in a structured and interpretable manner. Instead of relying on black-box models, it uses **explicit rules and keyword mappings** to ensure clarity, explainability, and easy extensibility.

The system processes user-submitted feedback to:
- Classify sentiment
- Detect recurring themes
- Generate insights useful for product improvement and decision-making

---

## Key Features

### Feedback Submission
- Users can submit product reviews with:
  - A **1–5 star rating**
  - A textual comment

### Rule-Based Sentiment Analysis
- Classifies feedback as **Positive**, **Negative**, or **Neutral**
- Uses expanded sentiment keyword lists
- Correctly handles negations (e.g., *“not good”*, *“not comfortable”*)

### Theme Detection
- Automatically categorizes reviews into predefined themes such as:
  - Comfort
  - Durability
  - Appearance
- Keyword-driven classification ensures consistent and interpretable results

### Insights Generator
- Produces actionable insights including:
  - Positive highlights
  - Common negative issues
  - Neutral trends
  - Star rating vs sentiment mismatches
- Weighted by severity and designed to remain informative even with limited data

### Dashboard Visualization
- Displays:
  - Sentiment distribution
  - Theme frequency counts
- Uses charts for quick and intuitive understanding of customer feedback trends

---

## Project Structure

Feedback_hub/
│── app.py # Flask backend
│── requirements.txt # Python dependencies
└── frontend/
└── index.html # Frontend interface

yaml
Copy code

---

## Installation

### Clone the Repository
```bash
git clone https://github.com/your-username/Feedback_hub.git
cd Feedback_hub
Create a Virtual Environment (Recommended)
bash
Copy code
python -m venv env

# Linux / macOS
source env/bin/activate

# Windows
env\Scripts\activate
Install Dependencies
bash
Copy code
pip install -r requirements.txt
Running the Project
Start the Backend
bash
Copy code
python app.py
The Flask server will start at:

cpp
Copy code
http://127.0.0.1:5000/
Open the Frontend
Open the following file in your browser:

bash
Copy code
frontend/index.html
You can now submit feedback, refresh the dashboard, and generate insights in real time.

Usage
Submit Feedback

Select a product

Choose a star rating (1–5)

Write a review

Dashboard

Click “Refresh Dashboard” to view updated sentiment and theme charts

Insights

Click “Generate Insights” to view summarized findings and recommendations

Logic and Design Considerations
Sentiment Analysis

Keyword-based with negation handling

Ensures interpretable and predictable classification

Star Rating Adjustment

Star ratings influence sentiment interpretation

Example: a clearly negative review with 3 stars is still treated as negative

Theme Detection

Carefully curated keyword lists reduce misclassification

Insights Generation

Includes positive, negative, and neutral signals

Highlights inconsistencies between star ratings and textual sentiment

Technologies Used
Python

Flask

Flask-CORS

HTML, JavaScript

Chart-based visualizations

Future Improvements
Expand keyword lists and multi-word phrase detection

Improve insight weighting and reporting depth

Enhance frontend dashboard interactivity and visuals

License
This project is intended for educational purposes and may be freely used or modified.

