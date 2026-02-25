"""
Dream Decoder - Advanced Insights & Analysis Generator
Generates dynamic, personalized insights based on dream and sleep patterns
"""
import random
from collections import Counter
from datetime import datetime, timedelta
from backend.models.dream import Dream
from backend.models.sleep import SleepRecord

from backend.services.translations import get_insight_template, get_translation

# Expanded Emotional Insights with Variations
EMOTIONAL_INSIGHTS = {
    'fear': {
        'insights': [
            "Fear-based dreams often reflect daytime anxiety or stress. Your subconscious may be processing unresolved worries.",
            "Recurring fear in dreams can be a sign that you're avoiding a challenging situation in your waking life.",
            "Nightmares with fear often serve as a release valve for accumulated emotional tension.",
            "Feeling afraid in dreams often mirrors a lack of control in some area of your daily routine."
        ],
        'recommendations': [
            "Practice 'Image Rehearsal': reimagine your fearful dream with a positive, empowering ending.",
            "Write down your top 3 worries 2 hours before bed to 'empty' your mind.",
            "Try 4-7-8 breathing (inhale 4s, hold 7s, exhale 8s) if you wake up from a scary dream.",
            "Limit news or intense media consumption 2 hours before sleep."
        ]
    },
    'sadness': {
        'insights': [
            "Sad dreams may indicate unprocessed grief or a need for emotional release. They can be part of the healing process.",
            "Persistent sadness in dreams might suggest you're not giving yourself enough space for self-care during the day.",
            "Emotional dreams involving sadness often help the brain regulate mood and process disappointment.",
            "Dreaming of sadness can sometimes be a reflection of seasonal changes or physical fatigue."
        ],
        'recommendations': [
            "Engage in 'Gratitude Journaling': write down three small wins before sleeping.",
            "Ensure you get at least 15 minutes of natural sunlight during the day.",
            "Connect with a close friend or family member for a brief, positive conversation.",
            "Listen to uplifting music or watch something lighthearted before bed."
        ]
    },
    'anger': {
        'insights': [
            "Anger in dreams often reflects suppressed frustrations from your waking life that haven't found an outlet.",
            "Vivid dreams of conflict can be your subconscious trying to 'work through' an argument or perceived injustice.",
            "Feeling angry while dreaming is often a safe way for your mind to process intense reactive emotions.",
            "Dream anger might be a signal that your personal boundaries are being tested in reality."
        ],
        'recommendations': [
            "Try a brief physical activity (like a quick walk or stretching) to release physical tension.",
            "Write an 'unsent letter' to express your frustrations fully before you sleep.",
            "Use progressive muscle relaxation to let go of physical 'anger armor' in your body.",
            "Create a 'cool down' ritual before bed—avoid heated debates or complex work."
        ]
    },
    'joy': {
        'insights': [
            "Joyful dreams indicate high emotional resilience and positive life experiences currently.",
            "Frequent happiness in dreams often results from feeling secure and appreciated in your daily life.",
            "Your subconscious is celebrating your recent successes and reflecting your inner contentment.",
            "Dreams of joy suggest you're in a phase of creative growth or emotional expansion."
        ],
        'recommendations': [
            "Keep doing what you're doing—your current sleep hygiene and mental habits are working!",
            "Take a moment to visualize these positive dream scenes when you feel stressed during the day.",
            "Maintain your social connections as they seem to be fueling your positive state.",
            "Consider tracking what specific daytime activities precede these joyful dreams."
        ]
    },
    'surprise': {
        'insights': [
            "Dreams of surprise often reflect your adaptability to unexpected changes in your life.",
            "Feeling startled or surprised in a dream suggests you're processing new information or a shift in perspective.",
            "Your mind is exploring 'what if' scenarios, preparing you for variety and change.",
            "Surprise in dreams can be a sign of a creative breakthrough or a sudden realization."
        ],
        'recommendations': [
            "Stay open to new ideas—your mind is clearly in an active, observant state.",
            "Try some light meditation to stay grounded amidst life's surprises.",
            "Journal about any recent 'aha!' moments you've had recently.",
            "Keep a flexible schedule where possible to match your mind's current adaptability."
        ]
    },
    'neutral': {
        'insights': [
            "Neutral dreams serve as a 'defragmentation' process for your brain, organizing information without intense emotional charge.",
            "Thinking or observing in a dream without strong emotion shows your brain is in a high-level troubleshooting mode.",
            "Ordinary dreams are essential for memory consolidation and preparing for the following day's tasks.",
            "Feeling 'just okay' in a dream indicates stability and a balanced emotional state."
        ],
        'recommendations': [
            "Try to record even the smallest details—these often contain the most interesting patterns.",
            "Consider if the 'neutral' events in your dream reflect your current routine.",
            "Maintain your current habits as they are providing a stable environment for your rest.",
            "Practice mindfulness to see if you can become more aware of subtle emotions in these dreams."
        ]
    }
}

# Dream Category Specific Insights
CATEGORY_INSIGHTS = {
    'nightmare': {
        'insight': "Nightmares are common during periods of high stress or transition. They are your brain's way of 'stress-testing' difficult emotions.",
        'recommendation': "Establish a very consistent, calming 'wind-down' routine. Low lights and soft music for 30 mins before bed is key."
    },
    'lucid': {
        'insight': "Lucid dreaming shows a high level of self-awareness and cognitive control. It's an excellent state for creative problem-solving.",
        'recommendation': "Try setting a 'creative intention' before sleep if you become lucid—ask your subconscious for a solution to a problem."
    },
    'recurring': {
        'insight': "Recurring dreams mean your subconscious is really trying to get your attention on a specific unresolved theme.",
        'recommendation': "Focus on the *last* thing that happens in the dream. That's often where the 'stuck' point is. Try to imagine a different ending."
    }
}

def generate_insights(user_id, days=7, language='en'):
    """
    Generate advanced, dynamic insights based on dream and sleep data.
    """
    print(f"[Insights] Generating insights for user {user_id} over {days} days in {language}")
    dreams = Dream.get_recent(user_id, days)
    sleep_records = SleepRecord.get_recent(user_id, days)
    
    analysis = {
        'insights': [],
        'recommendations': [],
        'health_tips': [],
        'stats': get_empty_stats(),
        'period_days': days
    }
    
    if not dreams:
        analysis['insights'].append({
            'type': 'info',
            'title': get_insight_template(language, 'unlock_title'),
            'message': get_insight_template(language, 'unlock_message')
        })
        return analysis
    
    # 1. Emotional Distribution Analysis
    emotions = [d.primary_emotion for d in dreams if d.primary_emotion]
    emotion_counts = Counter(emotions)
    
    if emotion_counts:
        top_emotion, count = emotion_counts.most_common(1)[0]
        perc = round(count / len(dreams) * 100)
        
        # Localized Emotion Name
        translated_emotion = get_translation(language, f'emotion_{top_emotion}', top_emotion.capitalize())
        
        # Dynamic Message using template
        msg = get_insight_template(language, 'emotion_focus_msg', perc=perc, emotion=translated_emotion)
        if perc > 60:
            msg += get_insight_template(language, 'strong_pattern')
        
        analysis['insights'].append({
            'type': 'emotion',
            'title': get_insight_template(language, 'emotion_focus_title', emotion=translated_emotion),
            'message': msg,
            'data': dict(emotion_counts)
        })
        
        # Add emotion-specific content (localized later if needed)
        if top_emotion in EMOTIONAL_INSIGHTS:
            data = EMOTIONAL_INSIGHTS[top_emotion]
            analysis['health_tips'].append({
                'category': 'emotional',
                'title': f'Navigating {translated_emotion}',
                'insight': random.choice(data['insights']),
                'tips': random.sample(data['recommendations'], min(3, len(data['recommendations'])))
            })

    # 2. Dream Category Analysis
    all_categories = []
    for d in dreams:
        if hasattr(d, 'categories') and d.categories:
            all_categories.extend(d.categories)
    
    cat_counts = Counter(all_categories)
    for cat, count in cat_counts.items():
        if cat in CATEGORY_INSIGHTS and count >= 1:
            analysis['insights'].append({
                'type': 'category',
                'title': f'Type: {cat.capitalize()}',
                'message': f"You've experienced {count} {cat} dream(s) recently. {CATEGORY_INSIGHTS[cat]['insight']}"
            })
            analysis['recommendations'].append({
                'priority': 'medium',
                'title': f'Handle {cat.capitalize()} Dreams',
                'message': CATEGORY_INSIGHTS[cat]['recommendation']
            })

    # 3. Sentiment & Stress Patterns
    sentiments = Counter([d.sentiment for d in dreams if d.sentiment])
    neg_count = sentiments.get('negative', 0)
    neg_p = round(neg_count / len(dreams) * 100) if dreams else 0
    
    if neg_p > 50:
        analysis['insights'].append({
            'type': 'warning',
            'title': get_insight_template(language, 'high_intensity_title'),
            'message': get_insight_template(language, 'high_intensity_msg', perc=neg_p)
        })
        analysis['recommendations'].append({
            'priority': 'high',
            'title': get_insight_template(language, 'mental_unloading_title'),
            'message': get_insight_template(language, 'mental_unloading_msg')
        })

    # 4. Sleep & Dream Correlation
    if sleep_records:
        avg_q = sum(r.quality_rating for r in sleep_records if r.quality_rating) / len(sleep_records)
        avg_d = sum(r.duration_hours for r in sleep_records) / len(sleep_records)
        
        if avg_q < 5 and neg_p > 40:
            analysis['insights'].append({
                'type': 'sleep',
                'title': get_insight_template(language, 'sleep_cycle_title'),
                'message': get_insight_template(language, 'sleep_cycle_msg')
            })
            
        if avg_d < 6.5:
            analysis['recommendations'].append({
                'priority': 'high',
                'title': get_insight_template(language, 'length_priority_title'),
                'message': get_insight_template(language, 'length_priority_msg', avg_d=round(avg_d, 1))
            })

    # 5. Keyword/Symbol Trend Analysis
    all_keywords = [kw for d in dreams for kw in (d.keywords or [])]
    kw_counts = Counter(all_keywords)
    if kw_counts:
        top_kw, kw_count = kw_counts.most_common(1)[0]
        if kw_count > 1:
            analysis['insights'].append({
                'type': 'themes',
                'title': get_insight_template(language, 'symbol_theme_title', symbol=top_kw.capitalize()),
                'message': get_insight_template(language, 'symbol_theme_msg', symbol=top_kw, count=kw_count)
            })

    # 6. Sentiment Balance
    pos_dreams = sentiments.get('positive', 0)
    if pos_dreams > 0 and pos_dreams >= len(dreams) / 2:
        analysis['insights'].append({
            'type': 'positive',
            'title': get_insight_template(language, 'vitality_title'),
            'message': get_insight_template(language, 'vitality_msg')
        })

    # 7. Weekly Summary Stats
    analysis['stats'] = {
        'total_dreams': len(dreams),
        'total_sleep_records': len(sleep_records),
        'emotion_breakdown': dict(emotion_counts),
        'sentiment_breakdown': dict(sentiments),
        'avg_sleep_quality': round(avg_q, 1) if sleep_records else None,
        'avg_sleep_duration': round(avg_d, 1) if sleep_records else None,
        'top_keywords': [kw for kw, _ in kw_counts.most_common(12)]
    }
    
    return analysis
    
    return analysis

def get_dream_analysis(dream_id):
    """Get detailed analysis for a specific dream with health context."""
    dream = Dream.get_by_id(dream_id)
    if not dream:
        return None
    
    analysis = {
        'dream': dream.to_dict(),
        'emotional_insight': None,
        'health_tips': []
    }
    
    # Get emotional insight
    emotion = dream.primary_emotion
    if emotion and emotion in EMOTIONAL_INSIGHTS:
        data = EMOTIONAL_INSIGHTS[emotion]
        analysis['emotional_insight'] = random.choice(data['insights'])
        analysis['health_tips'] = random.sample(data['recommendations'], min(3, len(data['recommendations'])))
    
    # Add sentiment context
    if dream.sentiment == 'negative':
        analysis['sentiment_context'] = 'This dream had a negative emotional tone. Consider the scenarios that triggered these feelings.'
    elif dream.sentiment == 'positive':
        analysis['sentiment_context'] = 'This dream had a positive emotional tone! Your subconscious is reflecting good energy.'
    else:
        analysis['sentiment_context'] = 'This dream had a neutral emotional tone.'
    
    return analysis


def get_trends(user_id, days=30):
    """
    Get trend data for charts.
    """
    print(f"[Trends] Fetching trends for user {user_id} over {days} days")
    dreams = Dream.get_recent(user_id, days)
    sleep_records = SleepRecord.get_recent(user_id, days)
    
    # Group dreams by date and pre-calculate emotion counts
    dream_by_date = {}
    for dream in dreams:
        # Parse the created_at date
        if isinstance(dream.created_at, str):
            date_str = dream.created_at.split('T')[0] if 'T' in dream.created_at else dream.created_at.split(' ')[0]
        else:
            date_str = dream.created_at.strftime('%Y-%m-%d')
        
        if date_str not in dream_by_date:
            dream_by_date[date_str] = {
                'count': 0,
                'emotions': {}
            }
        
        day_data = dream_by_date[date_str]
        day_data['count'] += 1
        if dream.primary_emotion:
            emo = dream.primary_emotion
            day_data['emotions'][emo] = day_data['emotions'].get(emo, 0) + 1
    
    # Group sleep by date
    sleep_by_date = {r.date: r for r in sleep_records}
    
    # Generate date range
    today = datetime.now().date()
    dates = [(today - timedelta(days=i)).isoformat() for i in range(days)]
    dates.reverse()
    
    # Build trend data
    emotion_trends = []
    sleep_trends = []
    
    for date in dates:
        # Emotion data
        day_data = dream_by_date.get(date, {'count': 0, 'emotions': {}})
        emotion_trends.append({
            'date': date,
            'count': day_data['count'],
            'emotions': day_data['emotions']
        })
        
        # Sleep data
        sleep_record = sleep_by_date.get(date)
        sleep_data = {
            'date': date,
            'quality': sleep_record.quality_rating if sleep_record else None,
            'duration': sleep_record.duration_hours if sleep_record else None,
            'wakeups': sleep_record.wakeups if sleep_record else None
        }
        sleep_trends.append(sleep_data)
    
    return {
        'emotions': emotion_trends,
        'sleep': sleep_trends,
        'period_days': days
    }


def get_empty_stats():
    return {
        'total_dreams': 0,
        'total_sleep_records': 0,
        'emotion_breakdown': {},
        'sentiment_breakdown': {},
        'avg_sleep_quality': None,
        'avg_sleep_duration': None,
        'top_keywords': []
    }
