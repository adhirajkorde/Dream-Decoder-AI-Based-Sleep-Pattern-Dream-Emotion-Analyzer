/**
 * Dream Decoder - Internationalization (i18n) System
 * Frontend localization for English, Hindi, Marathi, and Hinglish
 */

// Translation dictionary
const translations = {
    en: {
        // App Header
        app_name: 'Dream Decoder',
        tagline: 'Advanced Dream Analysis & Insights',

        // Navigation
        nav_journal: 'Dream Journal',
        nav_sleep: 'Sleep Log',
        nav_analytics: 'Analytics',
        nav_insights: 'Insights',

        // Buttons
        btn_submit: 'Submit',
        btn_save: 'Save Dream',
        btn_delete: 'Delete',
        btn_cancel: 'Cancel',
        btn_logout: 'Logout',
        btn_delete_account: 'Delete Account',
        btn_login: 'Log In',
        btn_signup: 'Sign Up',
        btn_save_sleep: 'Save Sleep Record',

        // Auth Page
        auth_welcome: 'Welcome Back',
        auth_create_account: 'Create Account',
        auth_username: 'Username',
        auth_email: 'Email',
        auth_password: 'Password',
        auth_confirm_password: 'Confirm Password',
        auth_username_placeholder: 'Enter your username or email',
        auth_email_placeholder: 'Enter your email',
        auth_password_placeholder: 'Enter your password',
        auth_confirm_password_placeholder: 'Re-enter your password',
        auth_signup_username_hint: 'Choose a username (3-20 characters)',
        auth_username_hint: 'Letters, numbers, and underscores only',
        auth_password_hint: '8+ chars, with upper, lower, and numbers',
        auth_logging_in: 'Logging in...',
        auth_creating_account: 'Creating account...',
        auth_no_account: "Don't have an account?",
        auth_has_account: 'Already have an account?',
        auth_to_signup: 'Sign up here',
        auth_to_login: 'Log in here',

        // Dream Journal
        label_dream_content: 'Describe Your Dream',
        placeholder_dream: 'I dreamed that...',
        analyzing_dream: 'Analyzing your dream...',
        dream_saved: 'Dream saved successfully!',
        no_dreams: 'No dreams recorded yet. Start by adding your first dream!',

        // Sleep Log
        label_date: 'Date',
        label_duration: 'Duration (hours)',
        label_quality: 'Sleep Quality',
        label_notes: 'Notes',
        placeholder_notes: 'Any notes about your sleep...',
        sleep_saved: 'Sleep record saved!',
        no_sleep: 'No sleep records yet.',
        avg_quality: 'Avg Quality',
        avg_duration: 'Avg Duration',
        hours: 'hours',

        // Analysis
        sentiment: 'Sentiment',
        emotion: 'Emotion',
        keywords: 'Keywords',
        interpretation: 'Interpretation',
        overall_meaning: 'Overall Meaning',
        final_insight: 'Final Insight',

        // Messages
        msg_loading: 'Loading...',
        msg_error: 'An error occurred',
        msg_success: 'Success!',

        // Emotions
        emotion_joy: 'Joy',
        emotion_sadness: 'Sadness',
        emotion_fear: 'Fear',
        emotion_anger: 'Anger',
        emotion_surprise: 'Surprise',
        emotion_love: 'Love',
        emotion_neutral: 'Neutral',

        // Language Switcher
        language: 'Language',
        lang_en: 'English',
        lang_hi: 'Hindi',
        lang_mr: 'Marathi',
        lang_hinglish: 'Hinglish'
    },

    hi: {
        // App Header
        app_name: 'ड्रीम डिकोडर',
        tagline: 'एआई-संचालित स्वप्न विश्लेषण',

        // Navigation
        nav_journal: 'स्वप्न डायरी',
        nav_sleep: 'नींद रिकॉर्ड',
        nav_analytics: 'विश्लेषण',
        nav_insights: 'अंतर्दृष्टि',

        // Buttons
        btn_submit: 'जमा करें',
        btn_save: 'स्वप्न सहेजें',
        btn_delete: 'हटाएं',
        btn_cancel: 'रद्द करें',
        btn_logout: 'लॉग आउट',
        btn_delete_account: 'खाता हटाएं',
        btn_save_sleep: 'नींद रिकॉर्ड सहेजें',

        // Dream Journal
        label_dream_content: 'अपना स्वप्न बताएं',
        placeholder_dream: 'मैंने सपना देखा कि...',
        analyzing_dream: 'आपके स्वप्न का विश्लेषण हो रहा है...',
        dream_saved: 'स्वप्न सफलतापूर्वक सहेजा गया!',
        no_dreams: 'अभी तक कोई स्वप्न दर्ज नहीं। अपना पहला स्वप्न जोड़कर शुरू करें!',

        // Sleep Log
        label_date: 'तारीख',
        label_duration: 'अवधि (घंटे)',
        label_quality: 'नींद की गुणवत्ता',
        label_notes: 'टिप्पणियाँ',
        placeholder_notes: 'आपकी नींद के बारे में कोई टिप्पणी...',
        sleep_saved: 'नींद रिकॉर्ड सहेजा गया!',
        no_sleep: 'अभी तक कोई नींद रिकॉर्ड नहीं।',
        avg_quality: 'औसत गुणवत्ता',
        avg_duration: 'औसत अवधि',
        hours: 'घंटे',

        // Analysis
        sentiment: 'भावना',
        emotion: 'भाव',
        keywords: 'मुख्य शब्द',
        interpretation: 'व्याख्या',
        overall_meaning: 'समग्र अर्थ',
        final_insight: 'अंतिम अंतर्दृष्टि',

        // Messages
        msg_loading: 'लोड हो रहा है...',
        msg_error: 'एक त्रुटि हुई',
        msg_success: 'सफल!',

        // Emotions
        emotion_joy: 'खुशी',
        emotion_sadness: 'उदासी',
        emotion_fear: 'डर',
        emotion_anger: 'गुस्सा',
        emotion_surprise: 'आश्चर्य',
        emotion_love: 'प्यार',
        emotion_neutral: 'तटस्थ',

        // Language Switcher
        language: 'भाषा',
        lang_en: 'English',
        lang_hi: 'हिंदी',
        lang_mr: 'मराठी',
        lang_hinglish: 'Hinglish'
    },

    mr: {
        // App Header
        app_name: 'ड्रीम डीकोडर',
        tagline: 'एआय-चालित स्वप्न विश्लेषण',

        // Navigation
        nav_journal: 'स्वप्न नोंदवही',
        nav_sleep: 'झोप नोंद',
        nav_analytics: 'विश्लेषण',
        nav_insights: 'अंतर्दृष्टी',

        // Buttons
        btn_submit: 'सबमिट करा',
        btn_save: 'स्वप्न जतन करा',
        btn_delete: 'हटवा',
        btn_cancel: 'रद्द करा',
        btn_logout: 'लॉग आउट',
        btn_delete_account: 'खाते हटवा',
        btn_save_sleep: 'झोप नोंद जतन करा',

        // Dream Journal
        label_dream_content: 'तुमचे स्वप्न सांगा',
        placeholder_dream: 'मी स्वप्न पाहिले की...',
        analyzing_dream: 'तुमच्या स्वप्नाचे विश्लेषण होत आहे...',
        dream_saved: 'स्वप्न यशस्वीरित्या जतन केले!',
        no_dreams: 'अद्याप कोणतेही स्वप्न नोंदवलेले नाही। तुमचे पहिले स्वप्न जोडून सुरुवात करा!',

        // Sleep Log
        label_date: 'तारीख',
        label_duration: 'कालावधी (तास)',
        label_quality: 'झोपेची गुणवत्ता',
        label_notes: 'टिपा',
        placeholder_notes: 'तुमच्या झोपेबद्दल काही टिपा...',
        sleep_saved: 'झोप नोंद जतन केली!',
        no_sleep: 'अद्याप कोणतेही झोप नोंद नाही।',
        avg_quality: 'सरासरी गुणवत्ता',
        avg_duration: 'सरासरी कालावधी',
        hours: 'तास',

        // Analysis
        sentiment: 'भावना',
        emotion: 'भाव',
        keywords: 'मुख्य शब्द',
        interpretation: 'व्याख्या',
        overall_meaning: 'एकूण अर्थ',
        final_insight: 'अंतिम अंतर्दृष्टी',

        // Messages
        msg_loading: 'लोड होत आहे...',
        msg_error: 'त्रुटी झाली',
        msg_success: 'यशस्वी!',

        // Emotions
        emotion_joy: 'आनंद',
        emotion_sadness: 'दुःख',
        emotion_fear: 'भीती',
        emotion_anger: 'राग',
        emotion_surprise: 'आश्चर्य',
        emotion_love: 'प्रेम',
        emotion_neutral: 'तटस्थ',

        // Language Switcher
        language: 'भाषा',
        lang_en: 'English',
        lang_hi: 'हिंदी',
        lang_mr: 'मराठी',
        lang_hinglish: 'Hinglish'
    },

    hinglish: {
        // App Header
        app_name: 'Dream Decoder',
        tagline: 'Sapno Ka Advanced Analysis',

        // Navigation
        nav_journal: 'Dream Journal',
        nav_sleep: 'Sleep Log',
        nav_analytics: 'Analytics',
        nav_insights: 'Insights',

        // Buttons
        btn_submit: 'Submit Karo',
        btn_save: 'Dream Save Karo',
        btn_delete: 'Delete Karo',
        btn_cancel: 'Cancel Karo',
        btn_logout: 'Logout',
        btn_delete_account: 'Account Delete Karo',
        btn_save_sleep: 'Sleep Record Save Karo',

        // Dream Journal
        label_dream_content: 'Apna Dream Batao',
        placeholder_dream: 'Maine sapna dekha ki...',
        analyzing_dream: 'Aapke dream ka analysis ho raha hai...',
        dream_saved: 'Dream successfully save ho gaya!',
        no_dreams: 'Abhi tak koi dream record nahi. Apna pehla dream add karke start karo!',

        // Sleep Log
        label_date: 'Date',
        label_duration: 'Duration (hours)',
        label_quality: 'Sleep Quality',
        label_notes: 'Notes',
        placeholder_notes: 'Aapki sleep ke baare mein koi notes...',
        sleep_saved: 'Sleep record save ho gaya!',
        no_sleep: 'Abhi tak koi sleep record nahi.',
        avg_quality: 'Avg Quality',
        avg_duration: 'Avg Duration',
        hours: 'hours',

        // Analysis
        sentiment: 'Sentiment',
        emotion: 'Emotion',
        keywords: 'Keywords',
        interpretation: 'Interpretation',
        overall_meaning: 'Overall Meaning',
        final_insight: 'Final Insight',

        // Messages
        msg_loading: 'Load ho raha hai...',
        msg_error: 'Error hua',
        msg_success: 'Success!',

        // Emotions
        emotion_joy: 'Khushi',
        emotion_sadness: 'Udasi',
        emotion_fear: 'Dar',
        emotion_anger: 'Gussa',
        emotion_surprise: 'Surprise',
        emotion_love: 'Pyaar',
        emotion_neutral: 'Neutral',

        // Language Switcher
        language: 'Language',
        lang_en: 'English',
        lang_hi: 'Hindi',
        lang_mr: 'Marathi',
        lang_hinglish: 'Hinglish'
    }
};

// Current language
let currentLanguage = 'en';

/**
 * Initialize i18n system
 */
function initI18n() {
    // Force language to English for standard interface as per requirement
    currentLanguage = 'en';
    localStorage.setItem('app_language', 'en');

    // Apply translations
    applyTranslations();
}

/**
 * Get translation for a key
 */
function t(key, defaultValue = '') {
    const lang = translations[currentLanguage] || translations['en'];
    return lang[key] || defaultValue || key;
}

/**
 * Change language
 */
async function changeLanguage(langCode) {
    if (!translations[langCode]) {
        console.error(`Language ${langCode} not supported`);
        return;
    }

    currentLanguage = langCode;
    localStorage.setItem('app_language', langCode);

    // Update user preference on server
    try {
        await authService.updateLanguage(langCode);
    } catch (error) {
        console.error('Failed to update language preference:', error);
    }

    // Apply translations
    applyTranslations();
}

/**
 * Apply translations to all elements with data-i18n attribute
 */
function applyTranslations() {
    // Update all elements with data-i18n attribute
    document.querySelectorAll('[data-i18n]').forEach(element => {
        const key = element.getAttribute('data-i18n');
        const translation = t(key);

        if (element.tagName === 'INPUT' || element.tagName === 'TEXTAREA') {
            if (element.hasAttribute('placeholder')) {
                element.placeholder = translation;
            } else {
                element.value = translation;
            }
        } else {
            element.textContent = translation;
        }
    });

    // Update all elements with data-i18n-placeholder attribute
    document.querySelectorAll('[data-i18n-placeholder]').forEach(element => {
        const key = element.getAttribute('data-i18n-placeholder');
        element.placeholder = t(key);
    });

    // Update language selector
    const langSelector = document.getElementById('languageSelector');
    if (langSelector) {
        langSelector.value = currentLanguage;
    }
}

/**
 * Get current language
 */
function getCurrentLanguage() {
    return currentLanguage;
}
