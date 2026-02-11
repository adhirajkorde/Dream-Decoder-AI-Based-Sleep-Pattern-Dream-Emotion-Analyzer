# 🌙 Dream Decoder

**AI-Powered Dream Journal & Analysis Platform**

Dream Decoder is an intelligent dream journaling application that uses Natural Language Processing (NLP) to analyze your dreams, detect emotions, extract themes, and provide personalized health insights.

---

## ✨ Features

### 🧠 AI Dream Analysis
- **Emotion Detection** - Identifies emotions (Joy, Fear, Sadness, Anger, Surprise, Love) using DistilBERT transformer model
- **Sentiment Analysis** - Classifies dreams as Positive, Negative, or Neutral
- **Keyword Extraction** - Extracts key themes and entities using SpaCy NLP
- **Dream Theme Categorization** - Groups dreams into themes (Adventure, Relationships, Work, etc.)

### 📊 Analytics Dashboard
- Emotion trends over time (line charts)
- Sleep quality tracking
- Emotion breakdown (pie chart)
- Top recurring dream themes

### 🏥 Health & Wellness
- Personalized health tips based on dream patterns
- Sleep improvement recommendations
- Emotion-specific wellness advice
- Nightmare reduction techniques

### 😴 Sleep Tracking
- Log sleep duration, quality, and wake-ups
- Track correlations between sleep and dream content
- Monitor sleep patterns over time

---

## 🛠️ Technology Stack

| Component | Technology |
|-----------|------------|
| **Backend** | Python 3.11+, Flask 3.0 |
| **Database** | SQLite |
| **NLP/AI** | HuggingFace Transformers, SpaCy |
| **Emotion Model** | DistilBERT (bhadresh-savani/distilbert-base-uncased-emotion) |
| **Frontend** | Vanilla HTML, CSS, JavaScript |
| **Charts** | Chart.js |
| **Theme** | Midnight Voyage (Custom Dark Theme) |

---

## 📁 Project Structure

```
Dream-Decoder/
├── backend/
│   ├── app.py                     # Flask app entry point
│   ├── config.py                  # Configuration settings
│   ├── database/
│   │   └── db.py                  # SQLite initialization
│   ├── models/
│   │   ├── dream.py               # Dream model (CRUD)
│   │   └── sleep.py               # Sleep record model
│   ├── routes/
│   │   ├── dreams.py              # Dream API endpoints
│   │   ├── sleep.py               # Sleep API endpoints
│   │   ├── analysis.py            # Text analysis endpoint
│   │   └── insights.py            # Insights & trends APIs
│   └── services/
│       ├── nlp_engine.py          # Main NLP orchestrator
│       ├── emotion_analyzer.py    # Emotion detection (DistilBERT)
│       ├── sentiment_analyzer.py  # Sentiment classification
│       ├── keyword_extractor.py   # SpaCy keyword extraction
│       └── insights_generator.py  # Pattern analysis & health tips
├── frontend/
│   ├── index.html                 # Main UI
│   ├── css/
│   │   └── styles.css             # Midnight Voyage theme
│   └── js/
│       ├── api.js                 # API client
│       ├── charts.js              # Chart.js visualizations
│       └── app.js                 # Main application logic
├── data/
│   └── dream_decoder.db           # SQLite database (auto-created)
├── venv/                          # Python virtual environment
├── requirements.txt               # Python dependencies
├── setup.bat                      # First-time setup script
├── start.bat                      # Start server script
├── reset_db.bat                   # Database reset script
└── README.md                      # This file
```

---

## 🚀 Quick Start

### Prerequisites
- Python 3.11 or higher
- Internet connection (for first-time model download)

### Installation

**Option 1: Using Batch Files (Windows)**
```
1. Double-click setup.bat (first time only)
2. Double-click start.bat
3. Open http://localhost:5000
```

**Option 2: Manual Setup**
```bash
# Navigate to project folder
cd Dream-Decoder

# Create virtual environment
python -m venv venv

# Activate virtual environment
.\venv\Scripts\activate   # Windows
source venv/bin/activate  # Linux/Mac

# Install dependencies
pip install -r requirements.txt

# Download SpaCy model
python -m spacy download en_core_web_sm

# Run the application
python backend\app.py
```

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/health` | Health check |
| `GET` | `/api/dreams` | Get all dreams |
| `POST` | `/api/dreams` | Create & analyze dream |
| `DELETE` | `/api/dreams/:id` | Delete a dream |
| `GET` | `/api/sleep` | Get sleep records |
| `POST` | `/api/sleep` | Log sleep record |
| `POST` | `/api/analysis/text` | Analyze text (ad-hoc) |
| `GET` | `/api/insights` | Get insights & health tips |
| `GET` | `/api/insights/trends` | Get trend data for charts |

---

## 🎨 UI Design

The application uses a custom **"Midnight Voyage"** color theme:

| Color | Hex | Usage |
|-------|-----|-------|
| Midnight Blue | `#2F4157` | Primary backgrounds |
| Ocean Mist | `#577C8E` | Buttons, accents |
| Salted Foam | `#DAE4EA` | Highlights, text |

---

## 🏗️ How It Was Built

### 1. Backend Architecture
- **Flask** serves as the web framework with RESTful API design
- **SQLite** provides lightweight, file-based data persistence
- **Model-Route-Service** pattern for clean separation of concerns

### 2. NLP Pipeline
```
Dream Text → Emotion Analyzer → Sentiment Analyzer → Keyword Extractor → Theme Categorizer
                    ↓                   ↓                    ↓
             DistilBERT           TextBlob              SpaCy NER
```

### 3. Health Insights Engine
- Analyzes dream patterns over configurable time periods
- Maps emotions to evidence-based wellness recommendations
- Correlates sleep quality with dream content

### 4. Frontend Design
- Single-page application with tab-based navigation
- Responsive CSS Grid layouts
- Real-time API integration
- Chart.js for data visualization

---

## 📈 Sample Workflow

1. **Record a Dream** → Type your dream in the journal
2. **AI Analysis** → Emotion, sentiment, and keywords are detected
3. **View Details** → Click any dream for detailed analysis popup
4. **Track Patterns** → Analytics show trends over time
5. **Get Tips** → Personalized health recommendations based on patterns

---

## 🔮 Future Enhancements

- [ ] User authentication & profiles
- [ ] Dream image generation with AI
- [ ] Wearable device integration (sleep data)
- [ ] Export dreams to PDF
- [ ] Dream sharing & community
- [ ] Mobile app (React Native)
- [ ] Voice-to-text dream logging

---

## 📝 License

This project was created for educational/demonstration purposes.


---

*Last Updated: January 2026*
