/**
 * Dream Decoder - Charts Module
 * Handles all Chart.js visualizations
 */

// Chart instances (for updating)
let emotionChart = null;
let sleepChart = null;
let emotionPieChart = null;

// Emotion colors
const EMOTION_COLORS = {
    joy: '#fbbf24',
    sadness: '#60a5fa',
    fear: '#a78bfa',
    anger: '#f87171',
    surprise: '#f472b6',
    love: '#fb7185',
    neutral: '#6b6980'
};

// Chart.js global defaults
Chart.defaults.color = '#a8a6b8';
Chart.defaults.borderColor = 'rgba(167, 139, 250, 0.1)';
Chart.defaults.font.family = "'Inter', sans-serif";

/**
 * Initialize or update the emotion trends chart
 */
function renderEmotionChart(trendData) {
    const ctx = document.getElementById('emotion-chart');
    if (!ctx) return;

    // Process data for the chart
    const labels = trendData.map(d => formatDate(d.date));
    const datasets = [];

    // Collect all emotions across all days
    const allEmotions = new Set();
    trendData.forEach(day => {
        Object.keys(day.emotions || {}).forEach(e => allEmotions.add(e));
    });

    // Create a dataset for each emotion
    allEmotions.forEach(emotion => {
        datasets.push({
            label: capitalize(emotion),
            data: trendData.map(d => (d.emotions && d.emotions[emotion]) || 0),
            borderColor: EMOTION_COLORS[emotion] || '#6b6980',
            backgroundColor: `${EMOTION_COLORS[emotion] || '#6b6980'}33`,
            fill: true,
            tension: 0.4,
            pointRadius: 4,
            pointHoverRadius: 6,
        });
    });

    // If no data, show placeholder
    if (datasets.length === 0) {
        datasets.push({
            label: 'Dreams',
            data: trendData.map(d => d.count || 0),
            borderColor: '#a78bfa',
            backgroundColor: 'rgba(167, 139, 250, 0.2)',
            fill: true,
            tension: 0.4,
        });
    }

    const config = {
        type: 'line',
        data: { labels, datasets },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    position: 'top',
                    labels: {
                        boxWidth: 12,
                        padding: 15,
                    }
                },
                tooltip: {
                    mode: 'index',
                    intersect: false,
                    backgroundColor: 'rgba(26, 24, 37, 0.95)',
                    titleColor: '#f1f0f5',
                    bodyColor: '#a8a6b8',
                    borderColor: 'rgba(167, 139, 250, 0.3)',
                    borderWidth: 1,
                    padding: 12,
                    cornerRadius: 8,
                }
            },
            scales: {
                y: {
                    beginAtZero: true,
                    ticks: { stepSize: 1 },
                    grid: { color: 'rgba(167, 139, 250, 0.05)' }
                },
                x: {
                    grid: { display: false }
                }
            },
            interaction: {
                mode: 'nearest',
                axis: 'x',
                intersect: false
            }
        }
    };

    if (emotionChart) {
        emotionChart.data = config.data;
        emotionChart.update();
    } else {
        emotionChart = new Chart(ctx, config);
    }
}

/**
 * Initialize or update the sleep quality chart
 */
function renderSleepChart(sleepData) {
    const ctx = document.getElementById('sleep-chart');
    if (!ctx) return;

    const labels = sleepData.map(d => formatDate(d.date));

    const config = {
        type: 'bar',
        data: {
            labels,
            datasets: [
                {
                    label: 'Sleep Quality',
                    data: sleepData.map(d => d.quality),
                    backgroundColor: 'rgba(167, 139, 250, 0.6)',
                    borderColor: '#a78bfa',
                    borderWidth: 2,
                    borderRadius: 6,
                    yAxisID: 'y',
                },
                {
                    label: 'Hours Slept',
                    data: sleepData.map(d => d.duration),
                    type: 'line',
                    borderColor: '#60a5fa',
                    backgroundColor: 'rgba(96, 165, 250, 0.2)',
                    fill: true,
                    tension: 0.4,
                    yAxisID: 'y1',
                }
            ]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    position: 'top',
                    labels: { boxWidth: 12, padding: 15 }
                },
                tooltip: {
                    backgroundColor: 'rgba(26, 24, 37, 0.95)',
                    titleColor: '#f1f0f5',
                    bodyColor: '#a8a6b8',
                    borderColor: 'rgba(167, 139, 250, 0.3)',
                    borderWidth: 1,
                    padding: 12,
                    cornerRadius: 8,
                }
            },
            scales: {
                y: {
                    type: 'linear',
                    position: 'left',
                    min: 0,
                    max: 10,
                    title: {
                        display: true,
                        text: 'Quality (1-10)',
                        color: '#a78bfa'
                    },
                    grid: { color: 'rgba(167, 139, 250, 0.05)' }
                },
                y1: {
                    type: 'linear',
                    position: 'right',
                    min: 0,
                    max: 12,
                    title: {
                        display: true,
                        text: 'Hours',
                        color: '#60a5fa'
                    },
                    grid: { display: false }
                },
                x: {
                    grid: { display: false }
                }
            }
        }
    };

    if (sleepChart) {
        sleepChart.data = config.data;
        sleepChart.update();
    } else {
        sleepChart = new Chart(ctx, config);
    }
}

/**
 * Initialize or update the emotion pie chart
 */
function renderEmotionPieChart(emotionBreakdown) {
    const ctx = document.getElementById('emotion-pie-chart');
    if (!ctx) return;

    const labels = Object.keys(emotionBreakdown).map(capitalize);
    const data = Object.values(emotionBreakdown);
    const colors = Object.keys(emotionBreakdown).map(e => EMOTION_COLORS[e] || '#6b6980');

    const config = {
        type: 'doughnut',
        data: {
            labels,
            datasets: [{
                data,
                backgroundColor: colors,
                borderColor: 'rgba(26, 24, 37, 0.8)',
                borderWidth: 2,
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    position: 'right',
                    labels: {
                        boxWidth: 12,
                        padding: 15,
                        generateLabels: function (chart) {
                            const data = chart.data;
                            if (data.labels.length && data.datasets.length) {
                                const total = data.datasets[0].data.reduce((a, b) => a + b, 0);
                                return data.labels.map((label, i) => {
                                    const value = data.datasets[0].data[i];
                                    const percentage = Math.round((value / total) * 100);
                                    return {
                                        text: `${label} (${percentage}%)`,
                                        fillStyle: data.datasets[0].backgroundColor[i],
                                        strokeStyle: data.datasets[0].borderColor,
                                        lineWidth: data.datasets[0].borderWidth,
                                        index: i
                                    };
                                });
                            }
                            return [];
                        }
                    }
                },
                tooltip: {
                    backgroundColor: 'rgba(26, 24, 37, 0.95)',
                    titleColor: '#f1f0f5',
                    bodyColor: '#a8a6b8',
                    borderColor: 'rgba(167, 139, 250, 0.3)',
                    borderWidth: 1,
                    padding: 12,
                    cornerRadius: 8,
                    callbacks: {
                        label: function (context) {
                            const total = context.dataset.data.reduce((a, b) => a + b, 0);
                            const percentage = Math.round((context.raw / total) * 100);
                            return `${context.label}: ${context.raw} dreams (${percentage}%)`;
                        }
                    }
                }
            },
            cutout: '60%',
        }
    };

    if (emotionPieChart) {
        emotionPieChart.data = config.data;
        emotionPieChart.update();
    } else {
        emotionPieChart = new Chart(ctx, config);
    }
}

/**
 * Render keywords cloud
 */
function renderKeywordsCloud(keywords) {
    const container = document.getElementById('keywords-cloud');
    if (!container) return;

    if (!keywords || keywords.length === 0) {
        container.innerHTML = `
            <div class="empty-state small">
                <p>Record more dreams to see themes</p>
            </div>
        `;
        return;
    }

    // Assign sizes based on position (first ones are more frequent)
    const html = keywords.map((keyword, index) => {
        let sizeClass = '';
        if (index < 3) sizeClass = 'large';
        else if (index < 7) sizeClass = 'medium';

        return `<span class="keyword-cloud-item ${sizeClass}">${escapeHtml(keyword)}</span>`;
    }).join('');

    container.innerHTML = html;
}

// ==========================================
// HELPER FUNCTIONS
// ==========================================

/**
 * Format date for display
 */
function formatDate(dateStr) {
    if (!dateStr) return '';
    const date = new Date(dateStr);
    if (isNaN(date.getTime())) return dateStr; // Return original string if invalid
    return date.toLocaleDateString('en-US', { month: 'short', day: 'numeric' });
}

/**
 * Capitalize first letter
 */
function capitalize(str) {
    if (!str) return '';
    return str.charAt(0).toUpperCase() + str.slice(1);
}
