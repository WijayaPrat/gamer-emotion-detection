# gamer-emotion-detection


# 🎮 Gamer Emotion Detection (AI Web Application)

Gamer Emotion Detection adalah **aplikasi web berbasis Artificial Intelligence (AI)**  
yang digunakan untuk **mendeteksi emosi gamer dari teks input** sebelum bermain game.

Aplikasi ini dibangun menggunakan **Machine Learning (NLP)**,  
di-deploy secara **cloud-native** menggunakan **Google Cloud Compute Engine**,  
serta dilengkapi **monitoring & observability** menggunakan **Prometheus dan Grafana**.

🌐 **Live Demo (website):**  
👉 http://34.122.202.126/

command 

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

## 🧠 AI Approach

Aplikasi ini menggunakan pendekatan **Machine Learning – Text Classification (NLP)**.

### 📌 Detail AI:
- Tipe model: **Supervised Machine Learning**
- Task: **Emotion Classification**
- Input: Teks bebas dari user
- Output: Kategori emosi

### 🎭 Kelas Emosi:
- 😡 **Marah**
- 😢 **Sedih**
- 😊 **Senang**

Model dilatih menggunakan dataset teks sederhana dan disimpan dalam format:
- `model.pkl`
- `vectorizer.pkl`

---

## 🏗️ Arsitektur Sistem (Cloud-Native)
