/**
 * Dream Decoder - Main Application
 * UI logic and event handling
 */

// ==========================================
// INITIALIZATION
// ==========================================

document.addEventListener('DOMContentLoaded', () => {
    console.log('🌙 Dream Decoder - Initializing...');

    // Check if running via file:// protocol
    if (window.location.protocol === 'file:') {
        showToast('error', 'App is running from a local file. Please use http://localhost:5000 to access the application properly.');
        // Add a visible warning to the page too
        const mainContent = document.querySelector('.main-content');
        if (mainContent) {
            const warning = document.createElement('div');
            warning.className = 'protocol-warning';
            warning.innerHTML = `
                <div class="card" style="border: 2px solid var(--color-error); margin-bottom: 20px;">
                    <div class="card-body">
                        <h3>⚠️ Connection Warning</h3>
                        <p>It looks like you opened the <code>index.html</code> file directly. This will prevent the AI from saving and analyzing your dreams.</p>
                        <p>Please use the <strong>start.bat</strong> script and open <strong>http://localhost:5000</strong> in your browser.</p>
                    </div>
                </div>
            `;
            mainContent.prepend(warning);
        }
    }

    // Initialize components
    initTabs();
    initForms();
    initDateDefaults();

    // Load initial data
    loadDreams();
    loadSleepRecords();

    // Check API health
    checkHealth();
});

/**
 * Check API health on startup
 */
async function checkHealth() {
    try {
        await healthCheck();
        console.log('✅ API is healthy');
    } catch (error) {
        console.error('❌ API health check failed:', error);
        showToast('error', 'Cannot connect to server. Make sure the backend is running.');
    }
}

// ==========================================
// TAB NAVIGATION
// ==========================================

function initTabs() {
    const tabBtns = document.querySelectorAll('.tab-btn');
    const tabPanels = document.querySelectorAll('.tab-panel');

    tabBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            const tabId = btn.dataset.tab;

            // Update buttons
            tabBtns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');

            // Update panels
            tabPanels.forEach(panel => {
                panel.classList.remove('active');
                if (panel.id === `${tabId}-panel`) {
                    panel.classList.add('active');
                }
            });

            // Load data for the tab
            onTabChange(tabId);
        });
    });
}

/**
 * Handle tab changes - load relevant data
 */
function onTabChange(tabId) {
    switch (tabId) {
        case 'journal':
            loadDreams();
            break;
        case 'sleep':
            loadSleepRecords();
            break;
        case 'analytics':
            loadAnalytics();
            break;
        case 'insights':
            loadInsights();
            break;
    }
}

// ==========================================
// FORM HANDLING
// ==========================================

function initForms() {
    // Dream form
    const dreamForm = document.getElementById('dream-form');
    if (dreamForm) {
        dreamForm.addEventListener('submit', handleDreamSubmit);
    }

    // Sleep form
    const sleepForm = document.getElementById('sleep-form');
    if (sleepForm) {
        sleepForm.addEventListener('submit', handleSleepSubmit);
    }

    // Quality slider
    const qualitySlider = document.getElementById('sleep-quality');
    const qualityValue = document.getElementById('quality-value');
    if (qualitySlider && qualityValue) {
        qualitySlider.addEventListener('input', () => {
            qualityValue.textContent = qualitySlider.value;
        });
    }

    // Period selector for analytics
    const periodSelect = document.getElementById('emotion-period');
    if (periodSelect) {
        periodSelect.addEventListener('change', () => {
            loadAnalytics();
        });
    }

    // Refresh insights button
    const refreshBtn = document.getElementById('refresh-insights');
    if (refreshBtn) {
        refreshBtn.addEventListener('click', () => {
            loadInsights();
        });
    }
}

/**
 * Set default dates
 */
function initDateDefaults() {
    const dateInput = document.getElementById('sleep-date');
    if (dateInput) {
        dateInput.value = new Date().toISOString().split('T')[0];
    }
}

// ==========================================
// DREAM HANDLING
// ==========================================

/**
 * Handle dream form submission
 */
async function handleDreamSubmit(e) {
    e.preventDefault();

    const contentInput = document.getElementById('dream-content');
    const submitBtn = document.getElementById('submit-dream');
    const content = contentInput.value.trim();

    if (!content) {
        showToast('warning', 'Please describe your dream first.');
        return;
    }

    // Disable button during processing
    submitBtn.disabled = true;
    submitBtn.innerHTML = '<span class="btn-icon">⏳</span><span>Analyzing...</span>';

    try {
        // Create dream with analysis
        const dream = await createDream(content);

        // Show success
        showToast('success', 'Dream saved and analyzed!');

        // Show analysis preview
        showAnalysisPreview(dream);

        // Clear form
        contentInput.value = '';

        // Reload dreams list
        loadDreams();

    } catch (error) {
        showToast('error', `Failed to save dream: ${error.message}`);
    } finally {
        submitBtn.disabled = false;
        submitBtn.innerHTML = '<span class="btn-icon">🧠</span><span>Analyze & Save</span>';
    }
}

/**
 * Show analysis preview after saving
 */
function showAnalysisPreview(dream) {
    const preview = document.getElementById('analysis-preview');
    const content = preview.querySelector('.analysis-content');

    if (!preview || !content) return;

    const sentiment = dream.sentiment || 'neutral';
    const sentimentClass = `sentiment-${sentiment}`;
    const primaryEmotion = dream.primary_emotion || dream.emotion || 'neutral';
    const emotionEmoji = getEmotionEmoji(primaryEmotion);

    content.innerHTML = `
        <div class="analysis-row">
            <span class="analysis-label">Sentiment:</span>
            <span class="analysis-value ${sentimentClass}">
                ${capitalize(sentiment)} (${Math.round((dream.sentiment_score || 0) * 100)}% confident)
            </span>
        </div>
        <div class="analysis-row">
            <span class="analysis-label">Emotion:</span>
            <span class="analysis-value">
                ${emotionEmoji} ${capitalize(primaryEmotion)}
            </span>
        </div>
        ${dream.keywords && dream.keywords.length > 0 ? `
        <div class="analysis-row">
            <span class="analysis-label">Keywords:</span>
            <span class="analysis-value">
                ${dream.keywords.slice(0, 5).map(k => `<span class="keyword-tag">${k}</span>`).join(' ')}
            </span>
        </div>
        ` : ''}
        ${dream.analysis && dream.analysis.summary ? `
        <div class="analysis-row" style="flex-direction: column; align-items: flex-start;">
            <span class="analysis-label">Summary:</span>
            <span class="analysis-value" style="margin-top: 8px;">
                ${dream.analysis.summary}
            </span>
        </div>
        ` : ''}
    `;

    preview.classList.remove('hidden');

    // Hide after 10 seconds
    setTimeout(() => {
        preview.classList.add('hidden');
    }, 10000);
}

/**
 * Load and display dreams list
 */
async function loadDreams() {
    const container = document.getElementById('dreams-list');
    const countEl = document.getElementById('dream-count');

    if (!container) return;

    try {
        const response = await getDreams(50, 0);
        const dreams = response.dreams || [];

        // Update count
        if (countEl) {
            countEl.textContent = `${response.total} dream${response.total !== 1 ? 's' : ''}`;
        }

        if (dreams.length === 0) {
            container.innerHTML = `
                <div class="empty-state">
                    <span class="empty-icon">🌟</span>
                    <p>No dreams recorded yet</p>
                    <p class="hint">Start your journey by recording your first dream!</p>
                </div>
            `;
            return;
        }

        container.innerHTML = dreams.map(dream => renderDreamItem(dream)).join('');

        // Add click handlers for dream items (opens modal)
        container.querySelectorAll('.dream-item').forEach(item => {
            item.addEventListener('click', (e) => {
                // Don't open modal if clicking delete button
                if (e.target.closest('.btn-delete')) return;

                const dreamData = {
                    id: item.dataset.id,
                    content: item.dataset.content,
                    emotion: item.dataset.emotion || 'neutral',
                    sentiment: item.dataset.sentiment || 'neutral',
                    keywords: item.dataset.keywords ? item.dataset.keywords.split(',') : [],
                    date: item.dataset.date || ''
                };
                openDreamModal(dreamData);
            });
        });

        // Add delete handlers
        container.querySelectorAll('.btn-delete').forEach(btn => {
            btn.addEventListener('click', async (e) => {
                e.stopPropagation(); // Prevent modal from opening
                const id = btn.dataset.id;
                if (confirm('Are you sure you want to delete this dream?')) {
                    try {
                        await deleteDream(id);
                        showToast('success', 'Dream deleted');
                        loadDreams();
                    } catch (error) {
                        showToast('error', 'Failed to delete dream');
                    }
                }
            });
        });

    } catch (error) {
        container.innerHTML = `
            <div class="empty-state">
                <span class="empty-icon">⚠️</span>
                <p>Failed to load dreams</p>
                <p class="hint">${error.message}</p>
            </div>
        `;
    }
}

/**
 * Render a single dream item
 */
function renderDreamItem(dream) {
    const emotionEmoji = getEmotionEmoji(dream.primary_emotion);
    const date = formatDateTime(dream.created_at);
    const keywords = (dream.keywords || []).slice(0, 4);
    const keywordsStr = (dream.keywords || []).join(',');

    return `
        <div class="dream-item" 
             data-id="${dream.id}"
             data-content="${escapeHtml(dream.content).replace(/"/g, '&quot;')}"
             data-emotion="${dream.primary_emotion || 'neutral'}"
             data-sentiment="${dream.sentiment || 'neutral'}"
             data-keywords="${keywordsStr}"
             data-date="${date}">
            <div class="dream-item-header">
                <span class="dream-date">${date}</span>
                <span class="dream-emotion">${emotionEmoji} ${capitalize(dream.primary_emotion || 'neutral')}</span>
            </div>
            <p class="dream-content">${escapeHtml(dream.content)}</p>
            ${keywords.length > 0 ? `
            <div class="dream-keywords">
                ${keywords.map(k => `<span class="keyword-tag">${k}</span>`).join('')}
            </div>
            ` : ''}
            <div class="dream-actions">
                <button class="btn-delete" data-id="${dream.id}" title="Delete dream">🗑️</button>
            </div>
        </div>
    `;
}

// ==========================================
// DREAM MODAL
// ==========================================

/**
 * Open dream detail modal
 */
function openDreamModal(dream) {
    const modal = document.getElementById('dream-modal');
    if (!modal) return;

    // Health insights for emotions
    const healthInsights = {
        fear: 'Fear-based dreams often reflect daytime anxiety or unresolved stress. Consider relaxation techniques like deep breathing before bed.',
        sadness: 'Sad dreams may indicate unprocessed emotions. Journaling during the day can help you work through these feelings.',
        anger: 'Anger in dreams often reflects suppressed frustrations. Physical exercise and creative outlets can provide healthy release.',
        joy: 'Joyful dreams indicate emotional balance! Your subconscious is reflecting positive life experiences and contentment.',
        surprise: 'Dreams of surprise often relate to unexpected changes in your life. Embrace adaptability and stay open to new experiences.',
        love: 'Dreams of love reflect your emotional connections. Nurture your relationships and express gratitude to loved ones.'
    };

    // Populate modal
    document.getElementById('modal-date').textContent = dream.date;
    document.getElementById('modal-dream-text').textContent = dream.content;
    document.getElementById('modal-emotion').innerHTML = `${getEmotionEmoji(dream.emotion)} ${capitalize(dream.emotion)}`;

    // Sentiment
    const sentimentEl = document.getElementById('modal-sentiment');
    const sentiment = dream.sentiment || 'neutral';
    sentimentEl.textContent = capitalize(sentiment);
    sentimentEl.className = `modal-sentiment ${sentiment}`;

    // Keywords
    const keywordsEl = document.getElementById('modal-keywords');
    if (dream.keywords && dream.keywords.length > 0) {
        keywordsEl.innerHTML = dream.keywords
            .filter(k => k.trim())
            .map(k => `<span class="keyword-tag">${k}</span>`)
            .join('');
    } else {
        keywordsEl.innerHTML = '<span style="color: var(--color-text-muted);">No keywords extracted</span>';
    }

    // Health insight
    const healthSection = document.getElementById('modal-health-section');
    const healthInsightEl = document.getElementById('modal-health-insight');
    const emotionKey = (dream.emotion || 'neutral').toLowerCase();
    const insight = healthInsights[emotionKey];

    if (insight) {
        healthInsightEl.textContent = insight;
        healthSection.style.display = 'block';
    } else {
        healthSection.style.display = 'none';
    }

    // Show modal
    modal.classList.remove('hidden');

    // Fetch full dream details for interpretation
    const fetchFullDetails = async () => {
        try {
            const fullDream = await getDream(dream.id);
            if (fullDream && fullDream.interpretation) {
                renderInterpretation(fullDream.interpretation);
            }
        } catch (error) {
            console.error('Failed to fetch dream interpretation:', error);
        }
    };
    fetchFullDetails();

    function renderInterpretation(ip) {
        const elementsEl = document.getElementById('modal-elements');
        const overallEl = document.getElementById('modal-overall-interpretation');
        const finalEl = document.getElementById('modal-final-insight');
        const interpSection = document.getElementById('modal-interpretation-section');

        if (!ip || (!ip.numbered_elements?.length && !ip.overall_interpretation)) {
            if (interpSection) interpSection.style.display = 'none';
            return;
        }

        if (interpSection) interpSection.style.display = 'block';

        // Render Numbered Elements
        if (ip.numbered_elements && ip.numbered_elements.length > 0) {
            elementsEl.innerHTML = ip.numbered_elements.map(el => `
                <div class="interpretation-element">
                    <div class="element-header">
                        <span class="element-number">${escapeHtml(el.number)}</span>
                        <span class="element-text">${escapeHtml(el.element)}</span>
                    </div>
                    <div class="element-body">
                        <div class="element-insight">
                            <strong>Symbolic Meaning:</strong>
                            <p>${escapeHtml(el.symbolic_meaning)}</p>
                        </div>
                        <div class="element-insight">
                            <strong>Subconscious Insight:</strong>
                            <p>${escapeHtml(el.subconscious_insight)}</p>
                        </div>
                    </div>
                </div>
            `).join('');
        } else {
            elementsEl.innerHTML = '';
        }

        // Render Overall
        if (ip.overall_interpretation) {
            overallEl.innerHTML = `
                <div class="overall-interpretation">
                    <h5>Overall Interpretation</h5>
                    <p>${escapeHtml(ip.overall_interpretation)}</p>
                </div>
            `;
        } else {
            overallEl.innerHTML = '';
        }

        // Render Final
        if (ip.final_insight) {
            finalEl.innerHTML = `
                <div class="final-insight">
                    <p><em>${escapeHtml(ip.final_insight)}</em></p>
                </div>
            `;
        } else {
            finalEl.innerHTML = '';
        }
    }

    // Close handlers
    const closeModal = () => modal.classList.add('hidden');

    document.getElementById('close-modal').onclick = closeModal;
    modal.querySelector('.modal-overlay').onclick = closeModal;

    // Close on escape key
    const escHandler = (e) => {
        if (e.key === 'Escape') {
            closeModal();
            document.removeEventListener('keydown', escHandler);
        }
    };
    document.addEventListener('keydown', escHandler);
}

// ==========================================
// SLEEP HANDLING
// ==========================================

/**
 * Handle sleep form submission
 */
async function handleSleepSubmit(e) {
    e.preventDefault();

    const form = e.target;
    const formData = new FormData(form);

    const data = {
        date: formData.get('date'),
        duration_hours: parseFloat(formData.get('duration_hours')),
        wakeups: parseInt(formData.get('wakeups')) || 0,
        quality_rating: parseInt(formData.get('quality_rating')),
        notes: formData.get('notes') || ''
    };

    if (!data.date || !data.duration_hours) {
        showToast('warning', 'Please fill in required fields.');
        return;
    }

    try {
        await createSleepRecord(data);
        showToast('success', 'Sleep record saved!');

        // Reset form
        form.reset();
        initDateDefaults();
        document.getElementById('quality-value').textContent = '5';

        // Reload records
        loadSleepRecords();

    } catch (error) {
        showToast('error', `Failed to save: ${error.message}`);
    }
}

/**
 * Load and display sleep records
 */
async function loadSleepRecords() {
    const container = document.getElementById('sleep-list');
    const avgQuality = document.getElementById('avg-quality');
    const avgDuration = document.getElementById('avg-duration');

    if (!container) return;

    try {
        const response = await getRecentSleep(30);
        const records = response.records || [];

        // Update stats
        if (avgQuality) {
            avgQuality.textContent = response.averages?.quality
                ? `${response.averages.quality}/10`
                : '-';
        }
        if (avgDuration) {
            avgDuration.textContent = response.averages?.duration
                ? `${response.averages.duration}h`
                : '-';
        }

        if (records.length === 0) {
            container.innerHTML = `
                <div class="empty-state">
                    <span class="empty-icon">🛏️</span>
                    <p>No sleep records yet</p>
                </div>
            `;
            return;
        }

        container.innerHTML = records.map(record => renderSleepItem(record)).join('');

    } catch (error) {
        container.innerHTML = `
            <div class="empty-state">
                <span class="empty-icon">⚠️</span>
                <p>Failed to load sleep records</p>
            </div>
        `;
    }
}

/**
 * Render a single sleep record
 */
function renderSleepItem(record) {
    const date = formatDate(record.date);
    const qualityPercent = ((record.quality_rating || 5) / 10) * 100;

    return `
        <div class="sleep-item">
            <span class="sleep-item-date">${date}</span>
            <div class="sleep-item-stats">
                <span>💤 ${record.duration_hours}h</span>
                <span>🔔 ${record.wakeups || 0} wakeups</span>
                <div class="sleep-quality-bar">
                    <div class="sleep-quality-fill" style="width: ${qualityPercent}%"></div>
                </div>
            </div>
        </div>
    `;
}

// ==========================================
// ANALYTICS
// ==========================================

/**
 * Load analytics data and render charts
 */
async function loadAnalytics() {
    const periodSelect = document.getElementById('emotion-period');
    const days = periodSelect ? parseInt(periodSelect.value) : 30;

    try {
        // Get trends data
        const trends = await getTrends(days);

        // Render emotion trends chart
        if (trends.emotions) {
            renderEmotionChart(trends.emotions);
        }

        // Render sleep chart
        if (trends.sleep) {
            renderSleepChart(trends.sleep);
        }

        // Get insights for additional data
        const insights = await getInsights(days);

        // Render emotion pie chart
        if (insights.stats && insights.stats.emotion_breakdown) {
            const breakdown = insights.stats.emotion_breakdown;
            if (Object.keys(breakdown).length > 0) {
                renderEmotionPieChart(breakdown);
            }
        }

        // Render keywords cloud
        if (insights.stats && insights.stats.top_keywords) {
            renderKeywordsCloud(insights.stats.top_keywords);
        }

    } catch (error) {
        console.error('Failed to load analytics:', error);
    }
}

// ==========================================
// INSIGHTS
// ==========================================

/**
 * Load and display insights
 */
async function loadInsights() {
    const insightsList = document.getElementById('insights-list');
    const recommendationsList = document.getElementById('recommendations-list');
    const healthTipsList = document.getElementById('health-tips-list');
    const totalDreams = document.getElementById('total-dreams');
    const totalSleep = document.getElementById('total-sleep');
    const topEmotion = document.getElementById('top-emotion');

    if (!insightsList) return;

    // Show loading state
    insightsList.innerHTML = `
        <div class="loading-state">
            <span class="loading-icon">⏳</span>
            <p>Analyzing your patterns...</p>
        </div>
    `;

    try {
        const data = await getInsights(7);

        // Render insights
        if (data.insights && data.insights.length > 0) {
            insightsList.innerHTML = data.insights.map(insight => renderInsight(insight)).join('');
        } else {
            insightsList.innerHTML = `
                <div class="empty-state small">
                    <p>No insights yet. Record more dreams!</p>
                </div>
            `;
        }

        // Render health tips (NEW!)
        if (healthTipsList) {
            if (data.health_tips && data.health_tips.length > 0) {
                healthTipsList.innerHTML = data.health_tips.map(tip => renderHealthTip(tip)).join('');
            } else {
                healthTipsList.innerHTML = `
                    <div class="empty-state small">
                        <p>Keep journaling to receive personalized health tips!</p>
                    </div>
                `;
            }
        }

        // Render recommendations
        if (recommendationsList) {
            if (data.recommendations && data.recommendations.length > 0) {
                recommendationsList.innerHTML = data.recommendations.map(rec => renderRecommendation(rec)).join('');
            } else {
                recommendationsList.innerHTML = `
                    <div class="empty-state small">
                        <p>Keep journaling for personalized tips!</p>
                    </div>
                `;
            }
        }

        // Update quick stats
        if (data.stats) {
            if (totalDreams) totalDreams.textContent = data.stats.total_dreams || 0;
            if (totalSleep) totalSleep.textContent = data.stats.total_sleep_records || 0;
            if (topEmotion) {
                const emotions = data.stats.emotion_breakdown || {};
                const top = Object.entries(emotions).sort((a, b) => b[1] - a[1])[0];
                topEmotion.textContent = top ? capitalize(top[0]) : '-';
            }
        }

    } catch (error) {
        insightsList.innerHTML = `
            <div class="empty-state small">
                <span class="empty-icon">⚠️</span>
                <p>Failed to load insights</p>
            </div>
        `;
    }
}

/**
 * Render a health tip section
 */
function renderHealthTip(tip) {
    const categoryIcons = {
        emotional: '💭',
        sleep: '🛏️'
    };
    const icon = categoryIcons[tip.category] || '💡';

    return `
        <div class="health-tip-card">
            <div class="health-tip-header">
                <span class="health-tip-icon">${icon}</span>
                <h4>${escapeHtml(tip.title)}</h4>
            </div>
            ${tip.insight ? `<p class="health-tip-insight">${escapeHtml(tip.insight)}</p>` : ''}
            <ul class="health-tip-list">
                ${tip.tips.map(t => `<li>${escapeHtml(t)}</li>`).join('')}
            </ul>
        </div>
    `;
}

/**
 * Render a recommendation item
 */
function renderRecommendation(rec) {
    const priorityClass = rec.priority === 'high' ? 'priority-high' :
        rec.priority === 'medium' ? 'priority-medium' : '';
    return `
        <div class="recommendation-item ${priorityClass}">
            <h4>${escapeHtml(rec.title)}</h4>
            <p>${escapeHtml(rec.message)}</p>
        </div>
    `;
}

/**
 * Render a single insight
 */
function renderInsight(insight) {
    const iconMap = {
        emotion: '🎭',
        warning: '⚠️',
        positive: '🌟',
        sleep: '😴',
        themes: '🔮',
        info: '💡'
    };

    const icon = iconMap[insight.type] || '💡';

    return `
        <div class="insight-item type-${insight.type}">
            <span class="insight-icon">${icon}</span>
            <div class="insight-content">
                <h4>${escapeHtml(insight.title)}</h4>
                <p>${escapeHtml(insight.message)}</p>
            </div>
        </div>
    `;
}

// ==========================================
// TOAST NOTIFICATIONS
// ==========================================

/**
 * Show a toast notification
 */
function showToast(type, message) {
    const container = document.getElementById('toast-container');
    if (!container) return;

    const iconMap = {
        success: '✅',
        error: '❌',
        warning: '⚠️',
        info: '💡'
    };

    const toast = document.createElement('div');
    toast.className = `toast ${type}`;
    toast.innerHTML = `
        <span class="toast-icon">${iconMap[type] || '💡'}</span>
        <span class="toast-message">${escapeHtml(message)}</span>
        <button class="toast-close">&times;</button>
    `;

    container.appendChild(toast);

    // Close on click
    toast.querySelector('.toast-close').addEventListener('click', () => {
        toast.remove();
    });

    // Auto-remove after 5 seconds
    setTimeout(() => {
        if (toast.parentNode) {
            toast.remove();
        }
    }, 5000);
}

// ==========================================
// HELPER FUNCTIONS
// ==========================================

// ==========================================
// VOICE TO TEXT
// ==========================================

const voiceBtn = document.getElementById('voice-btn');
let recognition = null;

if ('webkitSpeechRecognition' in window || 'SpeechRecognition' in window) {
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    recognition = new SpeechRecognition();
    recognition.continuous = false;
    recognition.interimResults = false;
    recognition.lang = 'en-US';

    recognition.onstart = () => {
        voiceBtn.classList.add('recording');
        voiceBtn.innerHTML = '<span class="voice-icon">🛑</span>';
        showToast('info', 'Listening... Speak now.');
    };

    recognition.onend = () => {
        voiceBtn.classList.remove('recording');
        voiceBtn.innerHTML = '<span class="voice-icon">🎤</span>';
    };

    recognition.onresult = (event) => {
        const transcript = event.results[0][0].transcript;
        const dreamContent = document.getElementById('dream-content');
        if (dreamContent) {
            const currentVal = dreamContent.value.trim();
            dreamContent.value = currentVal ? `${currentVal} ${transcript}` : transcript;
            // Trigger input event to auto-resize if needed
            dreamContent.dispatchEvent(new Event('input'));
        }
    };

    recognition.onerror = (event) => {
        console.error('Speech recognition error:', event.error);
        showToast('error', `Speech recognition error: ${event.error}`);
    };
}

if (voiceBtn) {
    voiceBtn.addEventListener('click', () => {
        if (!recognition) {
            showToast('warning', 'Speech recognition is not supported in your browser.');
            return;
        }

        if (voiceBtn.classList.contains('recording')) {
            recognition.stop();
        } else {
            recognition.start();
        }
    });
}

// ==========================================
// PDF EXPORT
// ==========================================

async function handlePdfExport(dreamId) {
    const btn = document.getElementById('btn-export-pdf');
    const originalHtml = btn.innerHTML;

    try {
        btn.disabled = true;
        btn.innerHTML = '<span class="btn-icon">⏳</span><span>Generating...</span>';

        // Open the export URL in a new tab or trigger download
        const exportUrl = `${API_BASE}/api/dreams/${dreamId}/export`;

        // Use a hidden anchor to trigger download
        const a = document.createElement('a');
        a.href = exportUrl;
        a.download = `dream_export_${dreamId}.pdf`;
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);

        showToast('success', 'PDF generation started!');
    } catch (error) {
        console.error('Failed to export PDF:', error);
        showToast('error', 'Failed to generate PDF. Is the backend running?');
    } finally {
        setTimeout(() => {
            btn.disabled = false;
            btn.innerHTML = originalHtml;
        }, 2000);
    }
}

// ==========================================
// IMAGE GENERATION (PLACEHOLDER)
// ==========================================

function handleImageGenerationPlaceholder(dream) {
    const modalBody = document.querySelector('.modal-body');
    const existingPlaceholder = document.querySelector('.image-placeholder-container');

    if (existingPlaceholder) {
        existingPlaceholder.remove();
        return;
    }

    const placeholder = document.createElement('div');
    placeholder.className = 'image-placeholder-container';
    placeholder.innerHTML = `
        <span class="image-placeholder-icon">🖼️</span>
        <div class="image-placeholder-text">AI Image Generation coming soon!</div>
        <div class="image-placeholder-hint">Visualizing your dream: "${dream.content.substring(0, 50)}..."</div>
        <div class="image-placeholder-hint" style="margin-top: 10px;">
            > [!TIP]<br>
            We'll integrate Google Gemini for visual storytelling in the next update.
        </div>
    `;

    modalBody.appendChild(placeholder);
    placeholder.scrollIntoView({ behavior: 'smooth' });
}

// Update openDreamModal to handle buttons
const originalOpenDreamModal = openDreamModal;
openDreamModal = function (dream) {
    if (!dream) return;
    originalOpenDreamModal(dream);

    const exportBtn = document.getElementById('btn-export-pdf');
    const generateBtn = document.getElementById('btn-generate-image');

    if (exportBtn) {
        exportBtn.onclick = () => handlePdfExport(dream.id);
    }

    if (generateBtn) {
        generateBtn.onclick = () => handleImageGenerationPlaceholder(dream);
    }
};

/**
 * Format date for display
 */
function formatDate(dateStr) {
    if (!dateStr) return '';
    const date = new Date(dateStr);
    return date.toLocaleDateString('en-US', {
        weekday: 'short',
        month: 'short',
        day: 'numeric'
    });
}

/**
 * Format datetime for display
 */
function formatDateTime(dateStr) {
    if (!dateStr) return '';
    const date = new Date(dateStr);
    return date.toLocaleDateString('en-US', {
        month: 'short',
        day: 'numeric',
        hour: 'numeric',
        minute: '2-digit'
    });
}


/**
 * Capitalize first letter of a string
 */
function capitalize(str) {
    if (!str) return '';
    return str.charAt(0).toUpperCase() + str.slice(1).toLowerCase();
}

/**
 * Get emoji for an emotion
 */
function getEmotionEmoji(emotion) {
    const emojiMap = {
        joy: '😊',
        sadness: '😢',
        anger: '😠',
        fear: '😨',
        surprise: '😲',
        love: '❤️',
        neutral: '😐',
        disgust: '🤢',
        anticipation: '🤔',
        trust: '🤝'
    };
    return emojiMap[emotion?.toLowerCase()] || '🌙';
}
