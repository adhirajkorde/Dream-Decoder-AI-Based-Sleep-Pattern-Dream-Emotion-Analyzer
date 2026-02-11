"""
Dream Decoder - Insights Generator
Generates personalized insights and health recommendations based on dream and sleep patterns
"""
from collections import Counter
from datetime import datetime, timedelta
from backend.models.dream import Dream
from backend.models.sleep import SleepRecord


# Health recommendations database
HEALTH_TIPS = {
    'fear': {
        'title': '🧘 Managing Anxiety & Fear',
        'tips': [
            'Practice progressive muscle relaxation before bed',
            'Try 4-7-8 breathing: inhale 4 sec, hold 7 sec, exhale 8 sec',
            'Write down worries 2 hours before bedtime to clear your mind',
            'Limit caffeine intake after 2 PM',
            'Consider chamomile tea or lavender aromatherapy'
        ],
        'insight': 'Fear-based dreams often reflect daytime anxiety or stress. Your subconscious may be processing unresolved worries.'
    },
    'sadness': {
        'title': '💙 Emotional Wellness',
        'tips': [
            'Practice gratitude journaling - write 3 good things from your day',
            'Ensure adequate sunlight exposure (15-30 min daily)',
            'Connect with friends or loved ones regularly',
            'Light exercise like walking can boost mood naturally',
            'Consider speaking with a counselor if sadness persists'
        ],
        'insight': 'Sad dreams may indicate unprocessed emotions or grief. They can actually be healing as your mind works through feelings.'
    },
    'anger': {
        'title': '🔥 Releasing Tension',
        'tips': [
            'Physical exercise helps release pent-up frustration',
            'Practice mindfulness to observe anger without reacting',
            'Write unsent letters to express frustrations safely',
            'Take a warm bath or shower before bed to relax muscles',
            'Avoid screens and heated discussions 1 hour before sleep'
        ],
        'insight': 'Anger in dreams often reflects suppressed frustrations. Physical activity and creative outlets can provide healthy release.'
    },
    'joy': {
        'title': '✨ Maintaining Positivity',
        'tips': [
            'Continue your current wellness practices - they\'re working!',
            'Share your positive dreams with others',
            'Use dream journaling to track what makes you happy',
            'Build on positive themes for visualization exercises',
            'Celebrate small wins in your daily life'
        ],
        'insight': 'Joyful dreams indicate emotional balance and positive life experiences. Your subconscious is reflecting contentment!'
    }
}

SLEEP_HEALTH_TIPS = {
    'poor_quality': {
        'title': '🛏️ Improve Sleep Quality',
        'tips': [
            'Keep bedroom temperature between 60-67°F (15-19°C)',
            'Use blackout curtains or an eye mask',
            'Remove electronic devices from the bedroom',
            'Maintain consistent sleep and wake times',
            'Invest in a comfortable mattress and pillows',
            'Use white noise or earplugs if needed'
        ]
    },
    'short_duration': {
        'title': '⏰ Getting Enough Sleep',
        'tips': [
            'Adults need 7-9 hours of sleep per night',
            'Set a bedtime alarm 30 minutes before target sleep time',
            'Avoid naps longer than 20 minutes after 2 PM',
            'Create a relaxing pre-sleep routine',
            'Limit alcohol - it disrupts sleep quality later in the night'
        ]
    },
    'many_wakeups': {
        'title': '💤 Reducing Night Wakeups',
        'tips': [
            'Avoid liquids 2 hours before bedtime',
            'Check for sleep apnea if you snore frequently',
            'Keep room completely dark (even small lights affect sleep)',
            'Consider a weighted blanket for comfort',
            'Avoid large meals close to bedtime'
        ]
    },
    'negative_dreams': {
        'title': '🌙 Reducing Nightmares',
        'tips': [
            'Practice Image Rehearsal Therapy: reimagine bad dreams with positive endings',
            'Keep a dream journal to identify triggers',
            'Avoid scary movies, news, or games before bed',
            'Create a calm bedtime routine with relaxation',
            'Consider speaking with a therapist if nightmares persist'
        ]
    }
}


def generate_insights(days=7):
    """
    Generate insights based on recent dreams and sleep data.
    
    Args:
        days: Number of days to analyze (default 7)
        
    Returns:
        dict containing insights, health tips, and recommendations
    """
    dreams = Dream.get_recent(days)
    sleep_records = SleepRecord.get_recent(days)
    
    insights = []
    recommendations = []
    health_tips = []
    
    if not dreams:
        insights.append({
            'type': 'info',
            'title': 'Start Your Dream Journal',
            'message': 'Record your first dream to begin receiving personalized insights!'
        })
        return {
            'insights': insights,
            'recommendations': recommendations,
            'health_tips': health_tips,
            'stats': get_empty_stats()
        }
    
    # Analyze emotions
    emotion_counts = Counter()
    sentiment_counts = Counter()
    all_keywords = []
    
    for dream in dreams:
        if dream.primary_emotion:
            emotion_counts[dream.primary_emotion] += 1
        if dream.sentiment:
            sentiment_counts[dream.sentiment] += 1
        if dream.keywords:
            all_keywords.extend(dream.keywords)
    
    # Most common emotion
    if emotion_counts:
        top_emotion, count = emotion_counts.most_common(1)[0]
        percentage = round(count / len(dreams) * 100)
        
        insights.append({
            'type': 'emotion',
            'title': f'Dominant Emotion: {top_emotion.title()}',
            'message': f'{percentage}% of your dreams in the last {days} days expressed {top_emotion}.',
            'data': dict(emotion_counts)
        })
        
        # Get health tips for this emotion
        if top_emotion in HEALTH_TIPS:
            tip_data = HEALTH_TIPS[top_emotion]
            health_tips.append({
                'category': 'emotional',
                'emotion': top_emotion,
                'title': tip_data['title'],
                'insight': tip_data['insight'],
                'tips': tip_data['tips']
            })
    
    # Sentiment analysis
    if sentiment_counts:
        negative_count = sentiment_counts.get('negative', 0)
        positive_count = sentiment_counts.get('positive', 0)
        
        if negative_count > positive_count and negative_count > len(dreams) * 0.5:
            insights.append({
                'type': 'warning',
                'title': 'Many Negative Dreams',
                'message': f'You\'ve had {negative_count} negative dreams recently. This might indicate stress or anxiety.'
            })
            # Add nightmare reduction tips
            health_tips.append({
                'category': 'sleep',
                'title': SLEEP_HEALTH_TIPS['negative_dreams']['title'],
                'tips': SLEEP_HEALTH_TIPS['negative_dreams']['tips']
            })
        elif positive_count > negative_count:
            insights.append({
                'type': 'positive',
                'title': 'Positive Dream Trend!',
                'message': f'Great news! {positive_count} of your recent dreams had positive vibes.'
            })
    
    # Keyword themes
    if all_keywords:
        keyword_counts = Counter(all_keywords)
        top_keywords = keyword_counts.most_common(5)
        
        insights.append({
            'type': 'themes',
            'title': 'Recurring Themes',
            'message': 'These themes appear frequently in your dreams:',
            'data': [{'keyword': kw, 'count': c} for kw, c in top_keywords]
        })
    
    # Sleep quality analysis
    if sleep_records:
        avg_quality = sum(r.quality_rating for r in sleep_records if r.quality_rating) / len(sleep_records)
        avg_duration = sum(r.duration_hours for r in sleep_records) / len(sleep_records)
        total_wakeups = sum(r.wakeups for r in sleep_records if r.wakeups)
        avg_wakeups = total_wakeups / len(sleep_records)
        
        # Low quality sleep
        if avg_quality < 5:
            insights.append({
                'type': 'sleep',
                'title': 'Low Sleep Quality Detected',
                'message': f'Your average sleep quality is {avg_quality:.1f}/10. This may be affecting your dreams and overall health.'
            })
            health_tips.append({
                'category': 'sleep',
                'title': SLEEP_HEALTH_TIPS['poor_quality']['title'],
                'tips': SLEEP_HEALTH_TIPS['poor_quality']['tips']
            })
        
        # Short sleep duration
        if avg_duration < 6:
            insights.append({
                'type': 'warning',
                'title': 'Insufficient Sleep Duration',
                'message': f'You\'re averaging {avg_duration:.1f} hours per night. Adults need 7-9 hours for optimal health.'
            })
            health_tips.append({
                'category': 'sleep',
                'title': SLEEP_HEALTH_TIPS['short_duration']['title'],
                'tips': SLEEP_HEALTH_TIPS['short_duration']['tips']
            })
        
        # Many wakeups
        if avg_wakeups >= 2:
            insights.append({
                'type': 'info',
                'title': 'Frequent Night Wakeups',
                'message': f'You\'re waking up an average of {avg_wakeups:.1f} times per night.'
            })
            health_tips.append({
                'category': 'sleep',
                'title': SLEEP_HEALTH_TIPS['many_wakeups']['title'],
                'tips': SLEEP_HEALTH_TIPS['many_wakeups']['tips']
            })
        
        # Positive sleep feedback
        if avg_quality >= 7 and avg_duration >= 7:
            insights.append({
                'type': 'positive',
                'title': 'Great Sleep Health! 🌟',
                'message': 'You\'re getting quality sleep with enough duration. Keep up the good work!'
            })
    
    # Generate general recommendations
    recommendations = generate_recommendations(emotion_counts, sentiment_counts, sleep_records)
    
    # Calculate stats
    stats = {
        'total_dreams': len(dreams),
        'total_sleep_records': len(sleep_records),
        'emotion_breakdown': dict(emotion_counts),
        'sentiment_breakdown': dict(sentiment_counts),
        'avg_sleep_quality': SleepRecord.get_average_quality(days),
        'avg_sleep_duration': SleepRecord.get_average_duration(days),
        'top_keywords': [kw for kw, _ in Counter(all_keywords).most_common(10)]
    }
    
    return {
        'insights': insights,
        'recommendations': recommendations,
        'health_tips': health_tips,
        'stats': stats,
        'period_days': days
    }


def generate_recommendations(emotion_counts, sentiment_counts, sleep_records):
    """Generate personalized recommendations based on analysis."""
    recommendations = []
    
    # Based on emotions
    top_emotions = emotion_counts.most_common(2)
    for emotion, _ in top_emotions:
        if emotion == 'fear':
            recommendations.append({
                'priority': 'high',
                'title': '🧘 Relaxation Before Bed',
                'message': 'Try 10 minutes of deep breathing or meditation before sleep to calm anxiety.'
            })
        elif emotion == 'sadness':
            recommendations.append({
                'priority': 'medium',
                'title': '📝 Daytime Journaling',
                'message': 'Write about your feelings during the day to process emotions before they appear in dreams.'
            })
        elif emotion == 'anger':
            recommendations.append({
                'priority': 'high',
                'title': '🏃 Physical Activity',
                'message': 'Exercise earlier in the day to release tension and promote calmer sleep.'
            })
    
    # Based on sentiment
    negative_count = sentiment_counts.get('negative', 0)
    positive_count = sentiment_counts.get('positive', 0)
    
    if negative_count > positive_count:
        recommendations.append({
            'priority': 'high',
            'title': '📵 Digital Detox',
            'message': 'Avoid news, social media, and work emails at least 1 hour before bed.'
        })
    
    # Based on sleep
    if sleep_records:
        avg_quality = sum(r.quality_rating for r in sleep_records if r.quality_rating) / len(sleep_records)
        
        if avg_quality < 6:
            recommendations.append({
                'priority': 'high',
                'title': '🌡️ Sleep Environment',
                'message': 'Optimize your bedroom: keep it cool (65°F), dark, and quiet.'
            })
    
    # Always include a positive recommendation
    recommendations.append({
        'priority': 'low',
        'title': '📖 Consistent Dream Logging',
        'message': 'Record dreams immediately upon waking for more accurate tracking and better insights.'
    })
    
    return recommendations


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
    if emotion and emotion in HEALTH_TIPS:
        tip_data = HEALTH_TIPS[emotion]
        analysis['emotional_insight'] = tip_data['insight']
        analysis['health_tips'] = tip_data['tips'][:3]  # Top 3 tips
    
    # Add sentiment context
    if dream.sentiment == 'negative':
        analysis['sentiment_context'] = 'This dream had a negative emotional tone. Consider the scenarios that triggered these feelings.'
    elif dream.sentiment == 'positive':
        analysis['sentiment_context'] = 'This dream had a positive emotional tone! Your subconscious is reflecting good energy.'
    else:
        analysis['sentiment_context'] = 'This dream had a neutral emotional tone.'
    
    return analysis


def get_empty_stats():
    """Return empty stats structure."""
    return {
        'total_dreams': 0,
        'total_sleep_records': 0,
        'emotion_breakdown': {},
        'sentiment_breakdown': {},
        'avg_sleep_quality': None,
        'avg_sleep_duration': None,
        'top_keywords': []
    }


def get_trends(days=30):
    """
    Get trend data for charts.
    
    Args:
        days: Number of days to analyze
        
    Returns:
        dict with daily emotion and sleep trend data
    """
    dreams = Dream.get_recent(days)
    sleep_records = SleepRecord.get_recent(days)
    
    # Group dreams by date
    dream_by_date = {}
    for dream in dreams:
        # Parse the created_at date
        if isinstance(dream.created_at, str):
            date_str = dream.created_at.split('T')[0] if 'T' in dream.created_at else dream.created_at.split(' ')[0]
        else:
            date_str = dream.created_at.strftime('%Y-%m-%d')
        
        if date_str not in dream_by_date:
            dream_by_date[date_str] = []
        dream_by_date[date_str].append(dream)
    
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
        day_dreams = dream_by_date.get(date, [])
        emotion_data = {
            'date': date,
            'count': len(day_dreams),
            'emotions': {}
        }
        for dream in day_dreams:
            if dream.primary_emotion:
                emotion_data['emotions'][dream.primary_emotion] = \
                    emotion_data['emotions'].get(dream.primary_emotion, 0) + 1
        emotion_trends.append(emotion_data)
        
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
