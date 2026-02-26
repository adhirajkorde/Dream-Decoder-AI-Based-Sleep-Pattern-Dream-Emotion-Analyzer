# Dream Decoder: Project Q&A

### 1. What is the Dream Decoder project?
Dream Decoder is a full-stack AI platform that analyzes dreams to provide psychological and symbolic insights. It uses advanced NLP to detect emotions and sentiments across multiple languages.

### 2. How does the emotion detection logic work?
We use a hybrid approach combining **HuggingFace transformers** with **context-weighted scoring**. For example, if "peaceful" keywords are detected, the system boosts positive emotion scores to ensure accuracy.

### 3. What languages are supported, and how are they handled?
The system supports **English, Hindi, Marathi, and Hinglish**. It uses an automatic script-aware detector to identify the language and apply the correct symbolic database for interpretation.

### 4. What is the "Sentiment Voting System"?
It is a logic layer that coordinates model outputs. If there's a conflict (e.g., negative model score but positive dream symbols), the "voting" system uses symbol polarity to correct the final sentiment label.

### 5. How are keywords extracted without fillers?
We use **SpaCy** with a custom "Dream Stopword" filter. This removes non-symbolic words like "dream", "thought", or "felt", ensuring only Locations, Symbols, and Actions are extracted.

### 6. Is user data secure?
Yes. We implement **Argon2id hashing** for passwords and **JWT (JSON Web Tokens)** for session security. Local database storage ensures that personal dream journals remain private.

### 7. How does the Voice-to-Text feature work?
It uses the browser's native **Web Speech API** with custom persistence logic. This allows users to narrate long dreams continuously without the microphone cutting off early.

### 8. How did you improve analysis accuracy?
By implementing **Symbolic Reinforcement** — cross-referencing analysis outputs with a 300+ item symbolic database — we eliminate misclassified labels and ensure interpretations are grounded in verified dream elements.

### 9. Can I visualize my dream patterns?
Absolutely. The **Insights Dashboard** uses **Chart.js** to display emotional trends, sleep quality correlations, and long-term psychological patterns.

### 10. How do I start the project?
Simply run `setup.bat` to install dependencies and `start.bat` to launch the server. The app is then available locally at `http://localhost:5000`.
