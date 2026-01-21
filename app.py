from flask import Flask, render_template, request
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
import pickle

app = Flask(__name__)

# ======================
# LOAD MODEL
# ======================
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# ======================
# LABEL & RECOMMENDATION
# ======================
EMOTION_LABELS = {
    0: "😡 Marah",
    1: "😢 Sedih",
    2: "😊 Senang"
}

RECOMMENDATION = {
    "😡 Marah": "You seem angry. Calm down first to avoid bad performance.",
    "😢 Sedih": "You seem sad. Take a short rest before playing.",
    "😊 Senang": "You are feeling good. You can play right now!"
}

# ======================
# PROMETHEUS METRICS
# ======================
REQUEST_COUNT = Counter(
    "http_requests_total",
    "Total HTTP requests",
    ["method", "endpoint"]
)

REQUEST_LATENCY = Histogram(
    "http_request_latency_seconds",
    "Request latency",
    ["endpoint"]
)

EMOTION_COUNT = Counter(
    "emotion_prediction_total",
    "Total emotion predictions",
    ["emotion"]
)

# ======================
# ROUTES
# ======================
@app.route("/", methods=["GET", "POST"])
@REQUEST_LATENCY.labels(endpoint="/").time()
def index():
    REQUEST_COUNT.labels(method=request.method, endpoint="/").inc()

    emotion = None
    advice = None
    text_input = ""

    if request.method == "POST":
        text_input = request.form["text"].strip().lower()
        vector = vectorizer.transform([text_input])
        prediction = model.predict(vector)[0]
        emotion = EMOTION_LABELS[prediction]
        advice = RECOMMENDATION[emotion]

        # business metric
        EMOTION_COUNT.labels(emotion=emotion).inc()

    return render_template(
        "index.html",
        emotion=emotion,
        advice=advice,
        text_input=text_input
    )

# ======================
# METRICS ENDPOINT
# ======================
@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {"Content-Type": CONTENT_TYPE_LATEST}

# ======================
# RUN APP
# ======================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
