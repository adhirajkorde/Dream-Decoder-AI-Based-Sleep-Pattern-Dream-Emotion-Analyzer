/**
 * Dream Decoder - API Client
 * Handles all API communication with the backend
 */

const API_BASE = '';  // Same origin, no prefix needed

/**
 * Make an API request with error handling
 */
async function apiRequest(endpoint, options = {}) {
    const url = `${API_BASE}${endpoint}`;

    const defaultOptions = {
        headers: {
            'Content-Type': 'application/json',
        },
    };

    const config = { ...defaultOptions, ...options };

    try {
        const response = await fetch(url, config);

        let data;
        const contentType = response.headers.get('content-type');
        if (contentType && contentType.includes('application/json')) {
            data = await response.json();
        } else {
            const text = await response.text();
            console.error('Non-JSON response received:', text.substring(0, 200));
            throw new Error(`Server returned non-JSON response (${response.status}). Please check if the backend is running correctly.`);
        }

        if (!response.ok) {
            throw new Error(data.error || `HTTP error! status: ${response.status}`);
        }

        return data;
    } catch (error) {
        console.error(`API Error (${endpoint}):`, error);

        // Handle network errors (Failed to fetch)
        if (error.message === 'Failed to fetch') {
            throw new Error('Could not connect to the server. Please ensure the backend is running and you are not opening the file directly (use http://localhost:5000).');
        }

        throw error;
    }
}

// ==========================================
// DREAMS API
// ==========================================

/**
 * Create a new dream entry
 */
async function createDream(content) {
    return apiRequest('/api/dreams', {
        method: 'POST',
        body: JSON.stringify({ content }),
    });
}

/**
 * Get all dreams with pagination
 */
async function getDreams(limit = 50, offset = 0) {
    return apiRequest(`/api/dreams?limit=${limit}&offset=${offset}`);
}

/**
 * Get a specific dream by ID
 */
async function getDream(id) {
    return apiRequest(`/api/dreams/${id}`);
}

/**
 * Delete a dream
 */
async function deleteDream(id) {
    return apiRequest(`/api/dreams/${id}`, {
        method: 'DELETE',
    });
}

/**
 * Get recent dreams
 */
async function getRecentDreams(days = 7) {
    return apiRequest(`/api/dreams/recent?days=${days}`);
}

// ==========================================
// SLEEP API
// ==========================================

/**
 * Create a new sleep record
 */
async function createSleepRecord(data) {
    return apiRequest('/api/sleep', {
        method: 'POST',
        body: JSON.stringify(data),
    });
}

/**
 * Get all sleep records
 */
async function getSleepRecords(limit = 50, offset = 0) {
    return apiRequest(`/api/sleep?limit=${limit}&offset=${offset}`);
}

/**
 * Get recent sleep records with stats
 */
async function getRecentSleep(days = 7) {
    return apiRequest(`/api/sleep/recent?days=${days}`);
}

/**
 * Get sleep statistics
 */
async function getSleepStats(days = 7) {
    return apiRequest(`/api/sleep/stats?days=${days}`);
}

/**
 * Delete a sleep record
 */
async function deleteSleepRecord(id) {
    return apiRequest(`/api/sleep/${id}`, {
        method: 'DELETE',
    });
}

// ==========================================
// ANALYSIS API
// ==========================================

/**
 * Analyze text without saving
 */
async function analyzeText(text) {
    return apiRequest('/api/analyze', {
        method: 'POST',
        body: JSON.stringify({ text }),
    });
}

// ==========================================
// INSIGHTS API
// ==========================================

/**
 * Get personalized insights
 */
async function getInsights(days = 7) {
    return apiRequest(`/api/insights?days=${days}`);
}

/**
 * Get trend data for charts
 */
async function getTrends(days = 30) {
    return apiRequest(`/api/trends?days=${days}`);
}

// ==========================================
// HEALTH CHECK
// ==========================================

/**
 * Check if API is healthy
 */
async function healthCheck() {
    return apiRequest('/api/health');
}
/**
 * Escape HTML to prevent XSS
 */
function escapeHtml(text) {
    if (text === null || text === undefined) return '';
    const div = document.createElement('div');
    div.textContent = String(text);
    return div.innerHTML;
}
