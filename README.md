# Feedback Hub

**Feedback Hub** is a customer feedback analyzer built for **Giva Jewelry**. It allows users to submit product reviews, automatically analyzes sentiment using a rule-based approach, detects key themes, and displays insights on a dashboard with charts.

This project demonstrates careful attention to real-world feedback challenges and implements thoughtful solutions to improve accuracy and usability.

---

## Key Improvements & Attention to Detail

1. **Negation Handling**  
   - Reviews with phrases like "not good" or "never comfortable" are correctly identified as negative, even if the words themselves are positive.

2. **Star Rating Adjustment**  
   - Star ratings influence sentiment: a 3-star review with clearly negative text is counted as negative. This ensures alignment between numeric and textual feedback.

3. **Duplicate Review Detection**  
   - Prevents identical reviews from skewing insights.

4. **Expanded Keyword Lists & Themes**  
   - Positive and negative keyword lists are comprehensive.
   - Reviews are categorized into themes such as Comfort, Durability, and Appearance for deeper insights.

5. **Weighted Insights**  
   - Insights are not just raw counts; they are weighted by review severity and star rating.
   - Positive mentions are also tracked to balance recommendations.

6. **Immediate Insight Generation**  
   - Insights appear as soon as two reviews are submitted, even if neutral, ensuring the dashboard is always informative.

7. **Multi-Word Phrase Detection**  
   - Phrases like "not comfortable" are correctly interpreted to avoid misclassification.

8. **Data-Driven Dashboard**  
   - Displays sentiment distribution and theme counts with charts.
   - Automatically refreshes after submission for immediate feedback.

---

## Features

- **Feedback Submission**: Select a product, provide a rating (1–5), and write a review.
- **Sentiment Analysis**: Positive, Negative, Neutral classification with star-rating adjustment.
- **Theme Detection**: Categorizes reviews into Comfort, Durability, Appearance.
- **Insights Generator**: Provides actionable insights including potential improvements and highlights positive feedback.
- **Dashboard**: Pie and bar charts show sentiment distribution and theme counts for quick understanding.

---

## Project Structure

```
Feedback_hub/
│-- app.py                  # Flask backend
│-- requirements.txt        # Python dependencies
└-- frontend/
    └-- index.html          # Frontend interface
```

---

## Installation

1. **Clone the repository**

```bash
git clone https://github.com/your-username/Feedback_hub.git
cd Feedback_hub
```

2. **Create a virtual environment (optional but recommended)**

```bash
python -m venv env
# Linux/Mac
source env/bin/activate
# Windows
env\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

---

## Running the Project

1. **Start the Flask backend**

```bash
python app.py
```

By default, it will run at `http://127.0.0.1:5000/`.

2. **Open the frontend**

Open `frontend/index.html` in your browser. Submit feedback, view the dashboard, and generate insights instantly.

---

## Usage

- **Submit Feedback**: Select a product, provide a rating (1–5), and write a review.
- **Dashboard**: Click "Refresh Dashboard" to see sentiment distribution and theme counts.
- **Insights**: Click "Generate Insights" to view actionable insights immediately.

---

## Dependencies

- Flask  
- Flask-CORS  

Install all dependencies using:

```bash
pip install -r requirements.txt
```

---

## Future Improvements

- Expand keyword lists further and include more multi-word phrases.
- Enhance insights weighting and reporting (e.g., highlight trends over time).
- Improve frontend interactivity and dashboard charts.
- Consider storing feedback in a persistent database instead of in-memory storage.

---

## License

This project is for educational purposes and can be used or modified freely.




