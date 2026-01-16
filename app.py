from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# In-memory storage
feedbacks = []

# Sentiment vocabulary
positive_words = {
    "shiny", "elegant", "premium", "beautiful", "comfortable",
    "good", "nice", "love", "amazing", "great", "perfect", "pretty", "lovely",
    "strong", "durable", "great"
}

negative_words = {
    "tarnish", "dull", "broke","broken", "breaks", "breaking", "heavy", "bad",
    "uncomfortable", "poor", "fragile", "cheap", "worst", "disappointing"
}
     
negations = {"not", "never", "no"}

# THEMES (single + multi-word)
themes = {
    "Comfort": [
        "comfortable", "uncomfortable", "light", "light weight"
        "not comfortable", "too heavy", "very heavy",
        "easy to wear", "hard to wear", "comfy", "heavy"
    ],
    "Durability": [
        "broke", "broken", "fragile",
        "poor quality", "cheap quality",
        "long lasting", "very durable", "tarnish", "durable"
    ],
    "Appearance": [
        "shiny", "very shiny", "beautiful design",
        "looks cheap", "premium look",
        "dull finish", "pretty", "beautiful", "shiny"
    ]
}

# Utility functions
def tokenize(review):
    return review.lower().split()


def analyze_sentiment(review):
    words = tokenize(review)
    pos, neg = 0, 0

    for i, word in enumerate(words):
        flip = i > 0 and words[i - 1] in negations

        if word in positive_words:
            pos += -1 if flip else 1
        if word in negative_words:
            neg += -1 if flip else 1

    if pos > neg:
        return "Positive"
    elif neg > pos:
        return "Negative"
    return "Neutral"


def adjust_sentiment_with_rating(sentiment, rating):
    """
    Sentiment rules:
    - Text sentiment has priority
    - Star rating only resolves Neutral text
    """

    try:
        rating = int(rating)
    except ValueError:
        return sentiment

    # If text already expresses sentiment, keep it
    if sentiment in ["Positive", "Negative"]:
        return sentiment

    # Only use stars when text is neutral
    if rating <= 2:
        return "Negative"
    elif rating >= 4:
        return "Positive"

    return "Neutral"



def detect_star_sentiment_mismatch(sentiment, rating):
    rating = int(rating)
    if sentiment == "Positive" and rating <= 2:
        return True
    if sentiment == "Negative" and rating >= 4:
        return True
    return False


def detect_themes(review):
    review_lc = review.lower()
    detected = []

    for theme, keywords in themes.items():
        for kw in keywords:
            if kw in review_lc:
                detected.append(theme)
                break

    return detected


def severity_weight(rating):
    rating = int(rating)
    if rating == 1:
        return 1.5
    if rating == 2:
        return 1.2
    if rating == 3:
        return 1.0
    if rating == 4:
        return 0.7
    return 0.5

# API Routes
@app.route("/feedback", methods=["POST"])
def submit_feedback():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No JSON data"}), 400

    required = {"product_id", "rating", "review"}
    if not required.issubset(data):
        return jsonify({"error": "Missing fields"}), 400

    # Duplicate detection
    for f in feedbacks:
        if (
            f["product_id"] == data["product_id"]
            and f["review"].strip().lower() == data["review"].strip().lower()
        ):
            return jsonify({"error": "Duplicate review detected"}), 400

    sentiment = analyze_sentiment(data["review"])
    sentiment = adjust_sentiment_with_rating(sentiment, data["rating"])

    feedback = {
        "product_id": data["product_id"],
        "rating": int(data["rating"]),
        "review": data["review"],
        "sentiment": sentiment,
        "themes": detect_themes(data["review"]),
        "mismatch": detect_star_sentiment_mismatch(sentiment, data["rating"])
    }

    feedbacks.append(feedback)

    return jsonify({"message": "Feedback submitted", "feedback": feedback}), 201



@app.route("/dashboard/<product_id>")
def dashboard(product_id):
    data = [f for f in feedbacks if f["product_id"] == product_id]
    total = len(data) or 1

    sentiment_counts = {"Positive": 0, "Negative": 0, "Neutral": 0}
    theme_counts = {t: 0 for t in themes}
    mismatch_count = 0

    for f in data:
        sentiment_counts[f["sentiment"]] += 1
        for t in f["themes"]:
            theme_counts[t] += 1
        if f["mismatch"]:
            mismatch_count += 1

    return jsonify({
        "total_reviews": total,
        "sentiment_counts": sentiment_counts,
        "theme_counts": theme_counts,
        "mismatch_percentage": round((mismatch_count / total) * 100, 1)
    })


@app.route("/insights/<product_id>")
def insights(product_id):
    data = [f for f in feedbacks if f["product_id"] == product_id]
    total = len(data)

    if total == 0:
        return jsonify([])

    theme_negative_scores = {t: 0.0 for t in themes}
    theme_positive_counts = {t: 0 for t in themes}
    neutral_count = 0
    star_mismatch_count = 0

    for f in data:
        w = severity_weight(f["rating"])

        for t in f["themes"]:
            if f["sentiment"] == "Negative":
                theme_negative_scores[t] += w
            elif f["sentiment"] == "Positive":
                theme_positive_counts[t] += 1

        if f["sentiment"] == "Neutral":
            neutral_count += 1

        # Negative text but high star
        if f["sentiment"] == "Negative" and int(f["rating"]) >= 3:
            star_mismatch_count += 1

    insights = []

    # If there are at least 2 reviews, always give basic insight
    if total >= 2:
        # Negative themes
        for t, score in theme_negative_scores.items():
            percent = (score / total) * 100
            if score > 0:
                insights.append(
                    f"{round(percent)}% of users report {t.lower()} issues, needs attention"
                )

        # Positive themes
        for t, count in theme_positive_counts.items():
            percent = (count / total) * 100
            if count > 0:
                insights.append(
                    f"Users are pleased"
                )

        # Neutral reviews
        if neutral_count > 0:
            insights.append(f"{neutral_count} neutral review(s) received")

        # Star-sentiment mismatch
        if star_mismatch_count > 0:
            insights.append(
                f"{star_mismatch_count} review(s) have negative feedback but high stars"
            )

    # If fewer than 2 reviews, just summarize
    else:
        for f in data:
            insights.append(f"Review received: {f['sentiment']}")

    return jsonify(insights)

if __name__ == "__main__":
    app.run(debug=True)

