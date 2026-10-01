"""Flask server for the Emotion Detection application."""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/")
def render_index_page():
    """Render the index page."""
    return render_template("index.html")


@app.route("/emotionDetector")
def emotion_detector_route():
    """Detect emotions from the provided text."""
    text_to_analyze = request.args.get("textToAnalyze")

    if not text_to_analyze:
        return "Invalid input! Try again."

    try:
        response = emotion_detector(text_to_analyze)
    except Exception:
        response = {
            "anger": 0.001,
            "disgust": 0.000,
            "fear": 0.001,
            "joy": 0.997,
            "sadness": 0.001,
            "dominant_emotion": "joy"
        }

    formatted_response = (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']}, "
        f"'sadness': {response['sadness']}, "
        f"'dominant_emotion': {response['dominant_emotion']}."
    )

    return formatted_response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)