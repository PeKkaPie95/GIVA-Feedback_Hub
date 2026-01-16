# Feedback Hub

**Feedback Hub** is a customer feedback analyzer built for Giva Jewelry. It allows users to submit product reviews, analyzes sentiment using a rule-based approach, detects key themes, and displays insights on a dashboard with charts.

This project uses **Flask** for the backend and **HTML/JavaScript** for the frontend. The focus is on clear, rule-based logic for sentiment analysis, theme detection, and insights generation, with careful attention to detail in handling keywords, negations, and star ratings.

---

## Features

- **Feedback Submission**: Submit reviews with a rating (1–5) and text comment.
- **Rule-Based Sentiment Analysis**: Detects Positive, Negative, or Neutral sentiment using expanded keywords and handling negations.
- **Theme Detection**: Categorizes reviews into themes such as Comfort, Durability, and Appearance.
- **Insights Generator**: Provides actionable insights based on feedback, including positive mentions, negative issues, and star-sentiment mismatches.
- **Dashboard**: Visualizes sentiment distribution and theme counts using charts for immediate understanding.

---

## Project Structure

Feedback_hub/
│-- app.py # Flask backend
│-- requirements.txt # Python dependencies
└-- frontend/
└-- index.html # Frontend interface

yaml
Copy code

---

## Installation

1. **Clone the repository**

```bash
git clone https://github.com/your-username/Feedback_hub.git
cd Feedback_hub
Create a virtual environment (optional but recommended)

bash
Copy code
python -m venv env
source env/bin/activate  # Linux/Mac
env\Scripts\activate     # Windows
Install dependencies

bash
Copy code
pip install -r requirements.txt
Running the Project
Start the Flask backend

bash
Copy code
python app.py
By default, it will run at http://127.0.0.1:5000/.

Open the frontend

Open frontend/index.html in your browser. Submit feedback, view the dashboard, and generate insights instantly.

Usage
Submit Feedback: Select a product, provide a rating (1–5), and write a review.

Dashboard: Click "Refresh Dashboard" to see sentiment distribution and theme counts.

Insights: Click "Generate Insights" to view actionable insights.

Logic and Attention to Detail
Sentiment Analysis: Uses expanded keyword lists and handles negations (e.g., "not good") correctly.

Rating Adjustment: Star ratings influence neutral reviews. For example, a negative review with 3 stars is counted as negative.

Theme Detection: Carefully categorized keywords ensure accurate theme assignment.

Insights Generation: Weighted by severity, includes positive mentions, negative issues, neutral reviews, and star-sentiment mismatches. Provides insights even with minimal reviews to make the dashboard immediately informative.

Dependencies
Flask

Flask-CORS

Install all dependencies using:

bash
Copy code
pip install -r requirements.txt
Future Improvements
Expand keyword lists and multi-word phrase detection.

Enhance insights weighting and reporting.

Improve frontend charts and dashboard interactivity.

License
This project is for educational purposes and can be used or modified freely.
