import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle

data = {
    "text": [
        # MARAH
        "ga bener kamu mainnya",
        "tim sialan",
        "gue kesel banget",
        "aku marah sama kamu",
        "emosi banget hari ini",

        # SEDIH
        "aku kecewa banget",
        "sedih sekali hari ini",
        "aku ngerasa gagal",
        "down banget",
        "keadaan lagi buruk",

        # SENANG
        "aku senang sekali",
        "hari ini bahagia",
        "mood lagi bagus",
        "aku excited main game",
        "hari ini menyenangkan"
    ],
    "label": [
        0,0,0,0,0,      # Marah
        1,1,1,1,1,      # Sedih
        2,2,2,2,2       # Senang
    ]
}

df = pd.DataFrame(data)

vectorizer = TfidfVectorizer(stop_words="english")
X = vectorizer.fit_transform(df["text"])
y = df["label"]

model = LogisticRegression(max_iter=1000)
model.fit(X, y)

pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

print("Model emotion detection saved successfully")
