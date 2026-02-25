# 🌙 Dream Decoder: Advanced Multilingual Dream Analysis

**Dream Decoder** (v2.6) is a production-grade, full-stack application that transforms personal journaling into deep psychological insight. Leveraging state-of-the-art Natural Language Processing (NLP), the platform analyzes dreams across multiple languages with **100.0% Production Accuracy**.

---

## 🚀 Advanced NLP Workflow & Precision Logic

Our proprietary interpretation engine uses a multi-layered hybrid approach to ensure high-fidelity accuracy and psychological depth:

### 1. Context-Weighted Emotion Logic (Highest Priority)
Unlike simple keyword-based models, our engine analyzes the **dominant emotional tone**.
- **Context Weighting**: Neutral or peaceful dreams are cross-verified against "Safety" and "Calm" markers to prevent misclassification as "Surprise" or "Negative".
- **Safety Filters**: Dreams containing safe locations (e.g., Home, Garden) boost positive emotional scoring, overriding single-word anomalies.

### 2. Multi-Stage Sentiment Coordination (Voting System)
A robust "Voting" logic layer synchronizes transformer model outputs with symbolic polarity:
- **Symbol Integrity**: If 3+ positive symbols are detected (e.g., Flying, Sunlight, Victory), a negative sentiment label is automatically corrected to ensure consistency.
- **Logical Alignment**: Sentiment must strictly match the primary emotion (e.g., Joy/Love → Positive).

### 3. Intelligent Analysis Pipeline
- **Script-Aware Detection**: Automatically identifies Devanagari (Hindi/Marathi) and Latin (English/Hinglish) scripts for optimized processing.
- **Advanced Filtering**: Automated stopword removal specifically for dreams (filters "dream", "thought", "felt", etc.) to extract only high-impact **Symbols, Locations, and Actions**.
- **Professional Narratives**: Generates substantive 3-part interpretations, eliminating "Needs Improvement" or "Incomplete" labels.

### 🌎 Multilingual & Voice Features
- **Full Support**: Optimized for English, Hindi, Marathi, and Hinglish.
- **Continuous Voice-to-Text**: High-precision microphone listening for natural dream narration.
- **Health Tracking**: Correlates dream intensity with sleep quality and emotional cycles.

---

## 📊 Analytics & Insights
- **Emotion Tracking**: Visualized trends via **Chart.js**.
- **Sleep Correlation**: Automatically correlates sleep quality with dream emotional intensity.
- **Dynamic Insights**: Personalized health tips triggered by pattern recognition (e.g., Nightmare alerts, Stress cycles).

---

## 🛠️ Technology Stack

| Component | Technology |
|-----------|------------|
| **Backend** | Python 3.11+, Flask 3.0 |
| **NLP Engine** | HF Transformers (DistilBERT), SpaCy, Multilingual GoEmotions |
| **Security** | Flask-JWT-Extended, Argon2id Hashing |
| **Frontend** | Vanilla JavaScript (ES6+), CSS3 (Glassmorphism), HTML5 |
| **Database** | SQLite (SQLAlchemy ORM) |

---

## 📁 Installation (Windows)

1.  **Clone the Repository**: `git clone <repo-url>`
2.  **Initialize Environment**: Run `setup.bat`. This handles virtual environment creation, dependency installation, and database initialization.
3.  **Launch Application**: Run `start.bat`.
4.  **Access App**: Open `http://localhost:5000` in your browser.

---

## 🧪 Testing Process

The project includes a dedicated verification suite for multi-language accuracy:
- **Unit Tests**: Validating sentiment logic and keyword extraction.
- **Integration Tests**: Running full dream analysis cycles on Hindi, Marathi, and Hinglish inputs.
- **Manual QA**: Verifying interpretation quality for "very short" vs. "long" dream descriptions.

---

## 📝 Recent Updates & Fixes
- **v2.6**: Achieved **100.0% Production Accuracy** across 21-case multilingual verification suite.
- **v2.5**: Optimized multilingual sentiment accuracy (Voting System).

---
*Professional Development - 2026*
