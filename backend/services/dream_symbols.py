"""
Dream Decoder - Comprehensive Multilingual Dream Symbol Database
Expanded symbol database with 30+ symbols across multiple categories
"""

# Comprehensive Multilingual Dream Symbols Database
DREAM_SYMBOLS = {
    # ========================================
    # WATER-RELATED SYMBOLS
    # ========================================
    
    'ocean': {
        'category': 'water',
        'emotion': 'neutral',
        'weight': 1,
        'polarity': 0,
        'en': {
            'keywords': ['ocean', 'sea', 'vast water', 'deep sea'],
            'meaning': 'vast emotions, collective unconscious, deep feelings',
            'interpretation': 'The ocean represents the vast expanse of your emotional world and the collective unconscious. A calm ocean indicates inner peace and emotional stability, while a stormy ocean suggests emotional turmoil or overwhelming feelings.'
        },
        'hi': {
            'keywords': ['समुद्र', 'सागर', 'महासागर'],
            'meaning': 'विशाल भावनाएं, सामूहिक अवचेतन, गहरी भावनाएं',
            'interpretation': 'समुद्र आपकी भावनात्मक दुनिया के विशाल विस्तार और सामूहिक अवचेतन का प्रतिनिधित्व करता है। शांत समुद्र आंतरिक शांति और भावनात्मक स्थिरता का संकेत देता है, जबकि तूफानी समुद्र भावनात्मक उथल-पुथल या भारी भावनाओं का सुझाव देता है।'
        },
        'mr': {
            'keywords': ['समुद्र', 'सागर', 'महासागर'],
            'meaning': 'विशाल भावना, सामूहिक अवचेतन, खोल भावना',
            'interpretation': 'समुद्र तुमच्या भावनिक जगाचा विस्तृत विस्तार आणि सामूहिक अवचेतन दर्शवतो. शांत समुद्र आंतरिक शांती आणि भावनिक स्थिरता दर्शवतो, तर वादळी समुद्र भावनिक गोंधळ किंवा जबरदस्त भावना सूचित करतो.'
        },
        'hinglish': {
            'keywords': ['samundar', 'ocean', 'sea', 'sagar'],
            'meaning': 'vast emotions, deep feelings',
            'interpretation': 'Ocean aapki emotional world ka vast expanse aur collective unconscious ko represent karta hai. Calm ocean inner peace aur emotional stability indicate karta hai, jabki stormy ocean emotional turmoil ya overwhelming feelings suggest karta hai.'
        }
    },
    
    'river': {
        'category': 'water',
        'emotion': 'neutral',
        'weight': 1,
        'polarity': 0,
        'en': {
            'keywords': ['river', 'stream', 'flowing water', 'current'],
            'meaning': 'life journey, flow of time, emotional progress',
            'interpretation': 'A river symbolizes the flow of your life journey and the passage of time. A smooth-flowing river suggests you are going with the flow, while a turbulent river may indicate obstacles or resistance in your path.'
        },
        'hi': {
            'keywords': ['नदी', 'धारा', 'बहता पानी'],
            'meaning': 'जीवन यात्रा, समय का प्रवाह, भावनात्मक प्रगति',
            'interpretation': 'नदी आपकी जीवन यात्रा के प्रवाह और समय के बीतने का प्रतीक है। सुचारू रूप से बहती नदी बताती है कि आप प्रवाह के साथ जा रहे हैं, जबकि अशांत नदी आपके रास्ते में बाधाओं या प्रतिरोध का संकेत दे सकती है।'
        },
        'mr': {
            'keywords': ['नदी', 'प्रवाह', 'वाहते पाणी'],
            'meaning': 'जीवन प्रवास, वेळेचा प्रवाह, भावनिक प्रगती',
            'interpretation': 'नदी तुमच्या जीवन प्रवासाचा प्रवाह आणि वेळ जाणे दर्शवते. सुरळीत वाहणारी नदी सूचित करते की तुम्ही प्रवाहासोबत जात आहात, तर अशांत नदी तुमच्या मार्गातील अडथळे किंवा प्रतिकार दर्शवू शकते.'
        },
        'hinglish': {
            'keywords': ['nadi', 'river', 'stream', 'behta paani'],
            'meaning': 'life journey, flow of time',
            'interpretation': 'River aapki life journey ke flow aur time ke passage ko symbolize karti hai. Smooth-flowing river suggest karti hai ki aap flow ke saath ja rahe hain, jabki turbulent river aapke path mein obstacles ya resistance indicate kar sakti hai.'
        }
    },
    
    'rain': {
        'category': 'water',
        'emotion': 'sadness',
        'weight': 1,
        'polarity': -1,
        'en': {
            'keywords': ['rain', 'rainfall', 'drizzle', 'downpour', 'raining'],
            'meaning': 'cleansing, renewal, sadness, release',
            'interpretation': 'Rain in dreams often symbolizes emotional release and cleansing. Gentle rain can represent renewal and growth, while heavy rain may indicate overwhelming emotions or a need for emotional catharsis.'
        },
        'hi': {
            'keywords': ['बारिश', 'वर्षा', 'बूंदाबांदी'],
            'meaning': 'सफाई, नवीनीकरण, उदासी, मुक्ति',
            'interpretation': 'स्वप्न में बारिश अक्सर भावनात्मक मुक्ति और सफाई का प्रतीक होती है। हल्की बारिश नवीनीकरण और विकास का प्रतिनिधित्व कर सकती है, जबकि भारी बारिश भारी भावनाओं या भावनात्मक विमोचन की आवश्यकता का संकेत दे सकती है।'
        },
        'mr': {
            'keywords': ['पाऊस', 'वर्षा', 'रिमझिम'],
            'meaning': 'शुद्धीकरण, नूतनीकरण, दुःख, मुक्ती',
            'interpretation': 'स्वप्नातील पाऊस अनेकदा भावनिक मुक्ती आणि शुद्धीकरण दर्शवतो. हलका पाऊस नूतनीकरण आणि वाढ दर्शवू शकतो, तर मुसळधार पाऊस जबरदस्त भावना किंवा भावनिक विमोचनाची गरज दर्शवू शकतो.'
        },
        'hinglish': {
            'keywords': ['barish', 'rain', 'varsha', 'baarish'],
            'meaning': 'cleansing, renewal, emotional release',
            'interpretation': 'Sapne mein barish emotional release aur cleansing ko symbolize karti hai. Gentle rain renewal aur growth represent kar sakti hai, jabki heavy rain overwhelming emotions ya emotional catharsis ki need indicate kar sakti hai.'
        }
    },
    
    'flood': {
        'category': 'water',
        'emotion': 'fear',
        'weight': 1,
        'polarity': -1,
        'en': {
            'keywords': ['flood', 'flooding', 'deluge', 'inundation', 'overflow'],
            'meaning': 'overwhelming emotions, loss of control, crisis',
            'interpretation': 'Floods in dreams represent being overwhelmed by emotions or circumstances. They often indicate feelings of being out of control or facing a crisis that threatens to engulf you.'
        },
        'hi': {
            'keywords': ['बाढ़', 'प्रलय', 'जलप्लावन'],
            'meaning': 'भारी भावनाएं, नियंत्रण खोना, संकट',
            'interpretation': 'स्वप्न में बाढ़ भावनाओं या परिस्थितियों से अभिभूत होने का प्रतिनिधित्व करती है। वे अक्सर नियंत्रण से बाहर होने या ऐसे संकट का सामना करने की भावनाओं का संकेत देते हैं जो आपको निगलने की धमकी देता है।'
        },
        'mr': {
            'keywords': ['पूर', 'जलप्रलय', 'पाणी भरणे'],
            'meaning': 'जबरदस्त भावना, नियंत्रण गमावणे, संकट',
            'interpretation': 'स्वप्नातील पूर भावनांनी किंवा परिस्थितींनी भारावून जाणे दर्शवतो. ते अनेकदा नियंत्रणाबाहेर जाणे किंवा तुम्हाला गिळंकृत करणाऱ्या संकटाचा सामना करणे दर्शवतात.'
        },
        'hinglish': {
            'keywords': ['baadh', 'flood', 'paani ka sailaab'],
            'meaning': 'overwhelming emotions, loss of control',
            'interpretation': 'Sapne mein baadh emotions ya circumstances se overwhelmed hone ko represent karti hai. Ye aksar control se bahar hone ya crisis face karne ki feelings indicate karti hai.'
        }
    },
    
    # ========================================
    # FLYING & FALLING SYMBOLS
    # ========================================
    
    'flying': {
        'category': 'movement',
        'emotion': 'joy',
        'weight': 3,
        'polarity': 1,
        'en': {
            'keywords': ['flying', 'float', 'soar', 'levitate', 'airborne', 'glide'],
            'meaning': 'freedom, ambition, escape, transcendence',
            'interpretation': 'Flying dreams often symbolize a desire for freedom or escape from limitations. They can represent high ambitions, confidence, and the ability to rise above problems. The ease of flight reflects your confidence level.'
        },
        'hi': {
            'keywords': ['उड़ना', 'उड़ान', 'तैरना', 'आकाश में', 'हवा में'],
            'meaning': 'स्वतंत्रता, महत्वाकांक्षा, पलायन, उत्कर्ष',
            'interpretation': 'उड़ने के सपने अक्सर स्वतंत्रता की इच्छा या सीमाओं से बचने का प्रतीक होते हैं। वे उच्च महत्वाकांक्षाओं, आत्मविश्वास और समस्याओं से ऊपर उठने की क्षमता का प्रतिनिधित्व कर सकते हैं। उड़ान की सहजता आपके आत्मविश्वास के स्तर को दर्शाती है।'
        },
        'mr': {
            'keywords': ['उडणे', 'उड्डाण', 'तरंगणे', 'आकाशात', 'हवेत'],
            'meaning': 'स्वातंत्र्य, महत्त्वाकांक्षा, सुटका, उत्कर्ष',
            'interpretation': 'उडण्याची स्वप्ने अनेकदा स्वातंत्र्याची इच्छा किंवा मर्यादांपासून सुटका दर्शवतात. ती उच्च महत्त्वाकांक्षा, आत्मविश्वास आणि समस्यांवर मात करण्याची क्षमता दर्शवू शकतात. उड्डाणाची सहजता तुमच्या आत्मविश्वासाची पातळी दर्शवते.'
        },
        'hinglish': {
            'keywords': ['udna', 'flying', 'udaan', 'flight', 'hawa mein', 'aasman mein'],
            'meaning': 'freedom, high ambitions, confidence',
            'interpretation': 'Udne ke sapne freedom ki ichha ya limitations se escape ko symbolize karte hain. Ye high ambitions, confidence aur problems se upar uthne ki ability represent kar sakte hain. Flight ki ease aapke confidence level ko reflect karti hai.'
        }
    },
    
    'falling': {
        'category': 'movement',
        'emotion': 'fear',
        'weight': 1,
        'polarity': -1,
        'en': {
            'keywords': ['falling', 'drop', 'plunge', 'descend', 'tumble', 'crash'],
            'meaning': 'loss of control, anxiety, insecurity, failure',
            'interpretation': 'Falling dreams often reflect feelings of losing control or anxiety about a situation in your waking life. They can indicate insecurity, fear of failure, or feeling unsupported. The landing (or lack thereof) is significant.'
        },
        'hi': {
            'keywords': ['गिरना', 'पतन', 'नीचे गिरना', 'गिरते हुए'],
            'meaning': 'नियंत्रण खोना, चिंता, असुरक्षा, विफलता',
            'interpretation': 'गिरने के सपने अक्सर नियंत्रण खोने की भावनाओं या आपके जागते जीवन में किसी स्थिति के बारे में चिंता को दर्शाते हैं। वे असुरक्षा, विफलता के डर, या असमर्थित महसूस करने का संकेत दे सकते हैं। उतरना (या इसकी कमी) महत्वपूर्ण है।'
        },
        'mr': {
            'keywords': ['पडणे', 'खालून', 'खाली', 'पडलो', 'पडण्याची', 'पडल्यासारखे'],
            'meaning': 'नियंत्रण गमावणे, असुरक्षितता, चिंता',
            'interpretation': 'पडण्याची स्वप्ने अनेकदा नियंत्रण गमावण्याची भावना किंवा तुमच्या जागृत जीवनातील परिस्थितीबद्दल चिंता दर्शवतात. ती असुरक्षितता, अपयशाची भीती किंवा असमर्थित वाटणे दर्शवू शकतात. उतरणे (किंवा त्याची कमतरता) महत्त्वाचे आहे.'
        },
        'hinglish': {
            'keywords': ['girna', 'falling', 'neeche girna', 'drop', 'girte hue'],
            'meaning': 'loss of control, anxiety, insecurity',
            'interpretation': 'Girne ke sapne control khone ki feelings ya aapke waking life mein kisi situation ke baare mein anxiety ko reflect karte hain. Ye insecurity, failure ke dar ya unsupported feel karne ko indicate kar sakte hain.'
        }
    },
    
    # ========================================
    # ANIMAL SYMBOLS
    # ========================================
    
    'dog': {
        'category': 'animal',
        'emotion': 'love',
        'weight': 1,
        'polarity': 1,
        'en': {
            'keywords': ['dog', 'puppy', 'canine', 'hound'],
            'meaning': 'loyalty, friendship, protection, unconditional love',
            'interpretation': 'Dogs in dreams typically represent loyalty, friendship, and protection. A friendly dog suggests trust and companionship, while an aggressive dog may indicate betrayal or feeling threatened by someone close to you.'
        },
        'hi': {
            'keywords': ['कुत्ता', 'पिल्ला', 'श्वान'],
            'meaning': 'वफादारी, दोस्ती, सुरक्षा, बिना शर्त प्यार',
            'interpretation': 'स्वप्न में कुत्ते आमतौर पर वफादारी, दोस्ती और सुरक्षा का प्रतिनिधित्व करते हैं। एक दोस्ताना कुत्ता विश्वास और साहचर्य का सुझाव देता है, जबकि एक आक्रामक कुत्ता विश्वासघात या आपके करीबी किसी व्यक्ति से खतरा महसूस करने का संकेत दे सकता है।'
        },
        'mr': {
            'keywords': ['कुत्रा', 'पिल्लू', 'श्वान'],
            'meaning': 'निष्ठा, मैत्री, संरक्षण, बिनशर्त प्रेम',
            'interpretation': 'स्वप्नातील कुत्रे सामान्यत: निष्ठा, मैत्री आणि संरक्षण दर्शवतात. मैत्रीपूर्ण कुत्रा विश्वास आणि सहवास सूचित करतो, तर आक्रमक कुत्रा विश्वासघात किंवा तुमच्या जवळच्या कोणाकडून धोका वाटणे दर्शवू शकतो.'
        },
        'hinglish': {
            'keywords': ['kutta', 'dog', 'puppy', 'pillaa'],
            'meaning': 'loyalty, friendship, protection',
            'interpretation': 'Sapne mein kutte loyalty, friendship aur protection ko represent karte hain. Friendly dog trust aur companionship suggest karta hai, jabki aggressive dog betrayal ya kisi close person se threat feel karne ko indicate kar sakta hai.'
        }
    },
    
    'cat': {
        'category': 'animal',
        'emotion': 'neutral',
        'weight': 1,
        'polarity': 0,
        'en': {
            'keywords': ['cat', 'kitten', 'feline', 'kitty'],
            'meaning': 'independence, mystery, feminine energy, intuition',
            'interpretation': 'Cats in dreams often symbolize independence, mystery, and feminine energy. They can represent your intuitive side or a need for independence. A cat\'s behavior in the dream provides additional meaning.'
        },
        'hi': {
            'keywords': ['बिल्ली', 'बिल्ली का बच्चा'],
            'meaning': 'स्वतंत्रता, रहस्य, स्त्री ऊर्जा, अंतर्ज्ञान',
            'interpretation': 'स्वप्न में बिल्लियाँ अक्सर स्वतंत्रता, रहस्य और स्त्री ऊर्जा का प्रतीक होती हैं। वे आपके सहज पक्ष या स्वतंत्रता की आवश्यकता का प्रतिनिधित्व कर सकती हैं। सपने में बिल्ली का व्यवहार अतिरिक्त अर्थ प्रदान करता है।'
        },
        'mr': {
            'keywords': ['मांजर', 'मांजराचे पिल्लू'],
            'meaning': 'स्वातंत्र्य, गूढता, स्त्री ऊर्जा, अंतर्ज्ञान',
            'interpretation': 'स्वप्नातील मांजरी अनेकदा स्वातंत्र्य, गूढता आणि स्त्री ऊर्जा दर्शवतात. त्या तुमची सहज बाजू किंवा स्वातंत्र्याची गरज दर्शवू शकतात. स्वप्नातील मांजरीचे वर्तन अतिरिक्त अर्थ देते.'
        },
        'hinglish': {
            'keywords': ['billi', 'cat', 'kitten'],
            'meaning': 'independence, mystery, intuition',
            'interpretation': 'Sapne mein billiyan independence, mystery aur feminine energy ko symbolize karti hain. Ye aapki intuitive side ya independence ki need represent kar sakti hain.'
        }
    },
    
    'bird': {
        'category': 'animal',
        'emotion': 'joy',
        'weight': 1,
        'polarity': 1,
        'en': {
            'keywords': ['bird', 'birds', 'flying bird', 'flock', 'eagle', 'dove', 'crow'],
            'meaning': 'freedom, perspective, spiritual messages, aspirations',
            'interpretation': 'Birds in dreams often represent freedom, higher perspective, and spiritual messages. Flying birds suggest liberation and aspirations, while caged birds may indicate feeling trapped or restricted.'
        },
        'hi': {
            'keywords': ['पक्षी', 'चिड़िया', 'पंछी', 'उड़ता पक्षी', 'झुंड'],
            'meaning': 'स्वतंत्रता, दृष्टिकोण, आध्यात्मिक संदेश, आकांक्षाएं',
            'interpretation': 'स्वप्न में पक्षी अक्सर स्वतंत्रता, उच्च दृष्टिकोण और आध्यात्मिक संदेशों का प्रतिनिधित्व करते हैं। उड़ते पक्षी मुक्ति और आकांक्षाओं का सुझाव देते हैं, जबकि पिंजरे में बंद पक्षी फंसे हुए या प्रतिबंधित महसूस करने का संकेत दे सकते हैं।'
        },
        'mr': {
            'keywords': ['पक्षी', 'चिमणी', 'उडणारा पक्षी', 'कळप'],
            'meaning': 'स्वातंत्र्य, दृष्टीकोन, आध्यात्मिक संदेश, आकांक्षा',
            'interpretation': 'स्वप्नातील पक्षी अनेकदा स्वातंत्र्य, उच्च दृष्टीकोन आणि आध्यात्मिक संदेश दर्शवतात. उडणारे पक्षी मुक्ती आणि आकांक्षा सूचित करतात, तर पिंजऱ्यातील पक्षी अडकलेले किंवा प्रतिबंधित वाटणे दर्शवू शकतात.'
        },
        'hinglish': {
            'keywords': ['pakshi', 'bird', 'chidiya', 'udta pakshi'],
            'meaning': 'freedom, higher perspective, aspirations',
            'interpretation': 'Sapne mein pakshi freedom, higher perspective aur spiritual messages ko represent karte hain. Flying birds liberation aur aspirations suggest karte hain, jabki caged birds trapped ya restricted feel karne ko indicate kar sakte hain.'
        }
    },
    
    'spider': {
        'category': 'animal',
        'emotion': 'fear',
        'weight': 1,
        'polarity': -1,
        'en': {
            'keywords': ['spider', 'spiders', 'web', 'tarantula', 'arachnid'],
            'meaning': 'creativity, patience, feeling trapped, feminine power',
            'interpretation': 'Spiders in dreams can represent creativity and patience (weaving a web), but also feeling trapped or manipulated. They may symbolize a controlling person or situation in your life, or your own creative power.'
        },
        'hi': {
            'keywords': ['मकड़ी', 'जाला', 'मकड़ियां'],
            'meaning': 'रचनात्मकता, धैर्य, फंसा हुआ महसूस करना, स्त्री शक्ति',
            'interpretation': 'स्वप्न में मकड़ियां रचनात्मकता और धैर्य (जाला बुनना) का प्रतिनिधित्व कर सकती हैं, लेकिन फंसे हुए या हेरफेर किए गए महसूस करने का भी। वे आपके जीवन में एक नियंत्रित करने वाले व्यक्ति या स्थिति, या आपकी अपनी रचनात्मक शक्ति का प्रतीक हो सकते हैं।'
        },
        'mr': {
            'keywords': ['कोळी', 'जाळे', 'कोळ्या'],
            'meaning': 'सर्जनशीलता, संयम, अडकलेले वाटणे, स्त्री शक्ती',
            'interpretation': 'स्वप्नातील कोळी सर्जनशीलता आणि संयम (जाळे विणणे) दर्शवू शकतात, परंतु अडकलेले किंवा हाताळलेले वाटणे देखील. त्या तुमच्या जीवनातील नियंत्रण करणारी व्यक्ती किंवा परिस्थिती किंवा तुमची स्वतःची सर्जनशील शक्ती दर्शवू शकतात.'
        },
        'hinglish': {
            'keywords': ['makdi', 'spider', 'jaala', 'web'],
            'meaning': 'creativity, feeling trapped, manipulation',
            'interpretation': 'Sapne mein makdi creativity aur patience ko represent kar sakti hai, lekin trapped ya manipulated feel karne ko bhi. Ye aapke life mein controlling person ya situation ko symbolize kar sakti hai.'
        }
    },
    
    'snake': {
        'category': 'animal',
        'emotion': 'fear',
        'weight': 1,
        'polarity': -1,
        'en': {
            'keywords': ['snake', 'serpent', 'cobra', 'viper', 'python', 'snakes'],
            'meaning': 'transformation, healing, hidden fears, betrayal',
            'interpretation': 'Snakes can represent transformation and healing (shedding skin), but also hidden fears, threats, or betrayal. The context and your feelings in the dream are important. In some cultures, snakes are sacred and represent wisdom.'
        },
        'hi': {
            'keywords': ['सांप', 'नाग', 'सर्प', 'कोबरा', 'अजगर'],
            'meaning': 'परिवर्तन, उपचार, छिपे हुए डर, विश्वासघात',
            'interpretation': 'सांप परिवर्तन और उपचार (त्वचा छोड़ना) का प्रतिनिधित्व कर सकते हैं, लेकिन छिपे हुए डर, खतरों या विश्वासघात का भी। सपने में संदर्भ और आपकी भावनाएं महत्वपूर्ण हैं। कुछ संस्कृतियों में, सांप पवित्र हैं और ज्ञान का प्रतिनिधित्व करते हैं।'
        },
        'mr': {
            'keywords': ['साप', 'सर्प', 'नाग', 'कोब्रा', 'अजगर', 'विषारी'],
            'meaning': 'लपलेले भीती, परिवर्तन, विश्वासघात',
            'interpretation': 'साप परिवर्तन आणि उपचार (कातडी सोडणे) दर्शवू शकतात, परंतु लपलेली भीती, धोके किंवा विश्वासघात देखील. स्वप्नातील संदर्भ आणि तुमच्या भावना महत्त्वाच्या आहेत. काही संस्कृतींमध्ये, साप पवित्र आहेत आणि ज्ञान दर्शवतात.'
        },
        'hinglish': {
            'keywords': ['saanp', 'snake', 'naag', 'serpent', 'cobra'],
            'meaning': 'transformation, hidden fears, betrayal',
            'interpretation': 'Saanp transformation aur healing ko represent kar sakte hain, lekin hidden fears, threats ya betrayal ko bhi. Dream mein context aur aapki feelings important hain.'
        }
    },
    
    # ========================================
    # DARKNESS & DEATH SYMBOLS
    # ========================================
    
    'darkness': {
        'category': 'environment',
        'emotion': 'fear',
        'weight': 1,
        'polarity': -1,
        'en': {
            'keywords': ['darkness', 'dark', 'night', 'shadow', 'blackness', 'pitch black'],
            'meaning': 'unknown, fear, unconscious, mystery',
            'interpretation': 'Darkness in dreams often represents the unknown, your unconscious mind, or aspects of yourself you haven\'t acknowledged. It can indicate fear of the unknown or unexplored potential. The feeling in the darkness matters - peaceful or frightening.'
        },
        'hi': {
            'keywords': ['अंधेरा', 'अंधकार', 'रात', 'छाया', 'काला'],
            'meaning': 'अज्ञात, भय, अचेतन, रहस्य',
            'interpretation': 'स्वप्न में अंधेरा अक्सर अज्ञात, आपके अचेतन मन, या आपके उन पहलुओं का प्रतिनिधित्व करता है जिन्हें आपने स्वीकार नहीं किया है। यह अज्ञात के डर या अनदेखी क्षमता का संकेत दे सकता है। अंधेरे में भावना मायने रखती है - शांतिपूर्ण या भयावह।'
        },
        'mr': {
            'keywords': ['अंधार', 'काळोख', 'रात्र', 'सावली', 'काळा', 'अंधारमय', 'अंधारलेलं'],
            'meaning': 'अज्ञात, भीती, अचेतन, गूढता',
            'interpretation': 'स्वप्नातील अंधार अनेकदा अज्ञात, तुमचे अचेतन मन किंवा तुम्ही मान्य केलेले नसलेले पैलू दर्शवतो. ते अज्ञाताची भीती किंवा न शोधलेली क्षमता दर्शवू शकते. अंधारातील भावना महत्त्वाची आहे - शांत की भयावह.'
        },
        'hinglish': {
            'keywords': ['andhera', 'darkness', 'dark', 'raat', 'shadow'],
            'meaning': 'unknown, fear, unconscious mind',
            'interpretation': 'Sapne mein andhera unknown, aapke unconscious mind ya aapke unacknowledged aspects ko represent karta hai. Ye unknown ka dar ya unexplored potential indicate kar sakta hai.'
        }
    },
    
    'death': {
        'category': 'life_event',
        'emotion': 'sadness',
        'weight': 1,
        'polarity': -1,
        'en': {
            'keywords': ['death', 'dying', 'dead', 'funeral', 'grave', 'corpse', 'cemetery'],
            'meaning': 'transformation, endings, new beginnings, change',
            'interpretation': 'Death in dreams rarely predicts actual death. Instead, it often symbolizes the end of one phase and the beginning of another, representing transformation and change. It can indicate letting go of old patterns or relationships.'
        },
        'hi': {
            'keywords': ['मृत्यु', 'मरना', 'मृत', 'अंतिम संस्कार', 'कब्र', 'शव', 'कब्रिस्तान'],
            'meaning': 'परिवर्तन, समाप्ति, नई शुरुआत, बदलाव',
            'interpretation': 'स्वप्न में मृत्यु शायद ही कभी वास्तविक मृत्यु की भविष्यवाणी करती है। इसके बजाय, यह अक्सर एक चरण के अंत और दूसरे की शुरुआत का प्रतीक है, जो परिवर्तन और बदलाव का प्रतिनिधित्व करता है। यह पुराने पैटर्न या रिश्तों को छोड़ने का संकेत दे सकता है।'
        },
        'mr': {
            'keywords': ['मृत्यू', 'मरणे', 'मृत', 'अंत्यसंस्कार', 'कबर', 'प्रेत', 'स्मशान'],
            'meaning': 'परिवर्तन, समाप्ती, नवीन सुरुवात, बदल',
            'interpretation': 'स्वप्नातील मृत्यू क्वचितच वास्तविक मृत्यूची भविष्यवाणी करतो. त्याऐवजी, ते अनेकदा एका टप्प्याचा शेवट आणि दुसऱ्याची सुरुवात दर्शवते, परिवर्तन आणि बदल दर्शवते. ते जुने नमुने किंवा नातेसंबंध सोडणे दर्शवू शकते.'
        },
        'hinglish': {
            'keywords': ['maut', 'death', 'marna', 'dying', 'funeral', 'kabar'],
            'meaning': 'transformation, change, new beginning',
            'interpretation': 'Sapne mein maut actual death ko predict nahi karti. Instead, ye ek phase ka end aur dusre ki beginning ko symbolize karti hai, transformation aur change ko represent karti hai.'
        }
    },
    
    # ========================================
    # STRESS & ANXIETY SYMBOLS
    # ========================================
    
    'chase': {
        'category': 'action',
        'emotion': 'fear',
        'weight': 1,
        'polarity': -1,
        'en': {
            'keywords': ['chased', 'chasing', 'running away', 'pursued', 'escape', 'fleeing'],
            'meaning': 'avoidance, fear, running from problems, stress',
            'interpretation': 'Being chased in dreams often represents avoiding something in your waking life - a problem, emotion, or responsibility. The pursuer often symbolizes an aspect of yourself or a situation you\'re trying to escape. Facing the pursuer can lead to resolution.'
        },
        'hi': {
            'keywords': ['पीछा', 'भागना', 'पीछा किया जा रहा', 'भागते हुए'],
            'meaning': 'टालना, भय, समस्याओं से भागना, तनाव',
            'interpretation': 'स्वप्न में पीछा किया जाना अक्सर आपके जागते जीवन में किसी चीज़ से बचने का प्रतिनिधित्व करता है - एक समस्या, भावना, या जिम्मेदारी। पीछा करने वाला अक्सर आपके एक पहलू या ऐसी स्थिति का प्रतीक होता है जिससे आप बचने की कोशिश कर रहे हैं। पीछा करने वाले का सामना करने से समाधान हो सकता है।'
        },
        'mr': {
            'keywords': ['पाठलाग', 'पळणे', 'पाठलाग केला जात आहे', 'पळत असणे'],
            'meaning': 'टाळणे, भीती, समस्यांपासून पळणे, ताण',
            'interpretation': 'स्वप्नात पाठलाग केला जाणे अनेकदा तुमच्या जागृत जीवनात काहीतरी टाळणे दर्शवते - समस्या, भावना किंवा जबाबदारी. पाठलाग करणारा अनेकदा तुमचा एक पैलू किंवा अशी परिस्थिती दर्शवतो ज्यापासून तुम्ही सुटण्याचा प्रयत्न करत आहात.'
        },
        'hinglish': {
            'keywords': ['chase', 'pichha', 'bhaagna', 'running away', 'escape'],
            'meaning': 'avoidance, fear, running from problems',
            'interpretation': 'Sapne mein chase hona aapke waking life mein kisi cheez se avoid karne ko represent karta hai - problem, emotion ya responsibility. Pursuer aksar aapka ek aspect ya aisi situation symbolize karta hai jisse aap escape karne ki koshish kar rahe hain.'
        }
    },
    
    'exam': {
        'category': 'situation',
        'emotion': 'fear',
        'weight': 1,
        'polarity': -1,
        'en': {
            'keywords': ['exam', 'test', 'examination', 'quiz', 'unprepared', 'failing'],
            'meaning': 'performance anxiety, being judged, feeling unprepared',
            'interpretation': 'Exam dreams often reflect anxiety about being tested or judged in waking life. They commonly appear when facing challenges or feeling unprepared for a situation. These dreams highlight self-doubt and fear of failure.'
        },
        'hi': {
            'keywords': ['परीक्षा', 'टेस्ट', 'इम्तिहान', 'तैयार नहीं', 'फेल'],
            'meaning': 'प्रदर्शन चिंता, आंका जाना, अप्रस्तुत महसूस करना',
            'interpretation': 'परीक्षा के सपने अक्सर जागते जीवन में परीक्षण या आंके जाने की चिंता को दर्शाते हैं। वे आमतौर पर तब दिखाई देते हैं जब चुनौतियों का सामना करना पड़ता है या किसी स्थिति के लिए अप्रस्तुत महसूस करना पड़ता है। ये सपने आत्म-संदेह और विफलता के डर को उजागर करते हैं।'
        },
        'mr': {
            'keywords': ['परीक्षा', 'टेस्ट', 'इम्तिहान', 'तयार नाही', 'नापास'],
            'meaning': 'कामगिरीची चिंता, न्याय केला जाणे, तयार नसल्याची भावना',
            'interpretation': 'परीक्षेची स्वप्ने अनेकदा जागृत जीवनात परीक्षण किंवा न्याय केल्या जाण्याची चिंता दर्शवतात. ती सामान्यत: आव्हानांना तोंड देताना किंवा परिस्थितीसाठी तयार नसल्याची भावना असताना दिसतात.'
        },
        'hinglish': {
            'keywords': ['exam', 'pariksha', 'test', 'unprepared', 'fail'],
            'meaning': 'performance anxiety, being judged',
            'interpretation': 'Exam ke sapne waking life mein tested ya judged hone ki anxiety ko reflect karte hain. Ye commonly tab appear hote hain jab challenges face kar rahe ho ya kisi situation ke liye unprepared feel kar rahe ho.'
        }
    },
    
    'teeth_falling': {
        'category': 'body',
        'emotion': 'fear',
        'weight': 1,
        'polarity': -1,
        'en': {
            'keywords': ['teeth falling', 'losing teeth', 'teeth crumbling', 'tooth loss'],
            'meaning': 'anxiety, loss of control, communication issues, aging',
            'interpretation': 'Losing teeth in dreams often relates to anxiety about appearance, communication, or loss of power. It can represent fear of aging, concerns about how others perceive you, or difficulty expressing yourself. Very common stress dream.'
        },
        'hi': {
            'keywords': ['दांत गिरना', 'दांत टूटना', 'दांत खोना'],
            'meaning': 'चिंता, नियंत्रण खोना, संचार समस्याएं, बुढ़ापा',
            'interpretation': 'स्वप्न में दांत खोना अक्सर उपस्थिति, संचार, या शक्ति के नुकसान के बारे में चिंता से संबंधित है। यह बुढ़ापे के डर, दूसरों द्वारा आपको कैसे देखा जाता है इसकी चिंता, या खुद को व्यक्त करने में कठिनाई का प्रतिनिधित्व कर सकता है। बहुत आम तनाव सपना।'
        },
        'mr': {
            'keywords': ['दात पडणे', 'दात तुटणे', 'दात गमावणे'],
            'meaning': 'चिंता, नियंत्रण गमावणे, संवाद समस्या, वृद्धत्व',
            'interpretation': 'स्वप्नात दात गमावणे अनेकदा देखावा, संवाद किंवा शक्ती गमावण्याबद्दल चिंतेशी संबंधित आहे. ते वृद्धत्वाची भीती, इतर तुम्हाला कसे पाहतात याबद्दल चिंता किंवा स्वतःला व्यक्त करण्यात अडचण दर्शवू शकते.'
        },
        'hinglish': {
            'keywords': ['daant girna', 'teeth falling', 'daant tootna'],
            'meaning': 'anxiety, loss of control, communication issues',
            'interpretation': 'Sapne mein daant girna appearance, communication ya power ke loss ke baare mein anxiety se related hai. Ye aging ka dar, dusre aapko kaise perceive karte hain iska concern ya khud ko express karne mein difficulty represent kar sakta hai.'
        }
    },
    
    'late': {
        'category': 'situation',
        'emotion': 'fear',
        'weight': 1,
        'polarity': -1,
        'en': {
            'keywords': ['late', 'missing', 'delayed', 'running late', 'missed'],
            'meaning': 'anxiety, missed opportunities, time pressure, stress',
            'interpretation': 'Dreams about being late often reflect anxiety about missing opportunities or not meeting expectations. They can indicate feeling overwhelmed by responsibilities or fear of disappointing others. Common during stressful periods.'
        },
        'hi': {
            'keywords': ['देर', 'लेट', 'छूट गया', 'देर से'],
            'meaning': 'चिंता, छूटे अवसर, समय का दबाव, तनाव',
            'interpretation': 'देर होने के बारे में सपने अक्सर अवसरों को खोने या अपेक्षाओं को पूरा न करने की चिंता को दर्शाते हैं। वे जिम्मेदारियों से अभिभूत महसूस करने या दूसरों को निराश करने के डर का संकेत दे सकते हैं। तनावपूर्ण अवधि के दौरान आम।'
        },
        'mr': {
            'keywords': ['उशीर', 'लेट', 'चुकले', 'उशीरा'],
            'meaning': 'चिंता, चुकलेल्या संधी, वेळेचा दबाव, ताण',
            'interpretation': 'उशीर होण्याबद्दलची स्वप्ने अनेकदा संधी चुकवणे किंवा अपेक्षा पूर्ण न करण्याची चिंता दर्शवतात. ती जबाबदाऱ्यांनी भारावून जाणे किंवा इतरांना निराश करण्याची भीती दर्शवू शकतात.'
        },
        'hinglish': {
            'keywords': ['late', 'der', 'missed', 'choot gaya'],
            'meaning': 'anxiety, missed opportunities, time pressure',
            'interpretation': 'Late hone ke sapne opportunities miss karne ya expectations meet na karne ki anxiety ko reflect karte hain. Ye responsibilities se overwhelmed feel karne ya dusron ko disappoint karne ke dar ko indicate kar sakte hain.'
        }
    },
    
    # ========================================
    # ADDITIONAL COMMON SYMBOLS
    # ========================================
    
    'house': {
        'category': 'place',
        'emotion': 'neutral',
        'weight': 1,
        'polarity': 0,
        'en': {
            'keywords': ['house', 'home', 'building', 'room', 'apartment', 'mansion'],
            'meaning': 'self, psyche, security, different life aspects',
            'interpretation': 'A house in dreams often represents yourself or your psyche. Different rooms can symbolize different aspects of your personality or life. The condition of the house reflects your current state of mind.'
        },
        'hi': {
            'keywords': ['घर', 'मकान', 'इमारत', 'कमरा', 'अपार्टमेंट'],
            'meaning': 'स्वयं, मानसिकता, सुरक्षा, विभिन्न जीवन पहलू',
            'interpretation': 'स्वप्न में घर अक्सर आपके या आपकी मानसिकता का प्रतिनिधित्व करता है। विभिन्न कमरे आपके व्यक्तित्व या जीवन के विभिन्न पहलुओं का प्रतीक हो सकते हैं। घर की स्थिति आपकी वर्तमान मानसिक स्थिति को दर्शाती है।'
        },
        'mr': {
            'keywords': ['घर', 'इमारत', 'खोली', 'अपार्टमेंट'],
            'meaning': 'स्वतः, मानसिकता, सुरक्षा, विविध जीवन पैलू',
            'interpretation': 'स्वप्नातील घर अनेकदा स्वतःचे किंवा तुमच्या मानसिकतेचे प्रतिनिधित्व करते. वेगवेगळ्या खोल्या तुमच्या व्यक्तिमत्त्वाच्या किंवा जीवनाच्या वेगवेगळ्या पैलूंचे प्रतीक असू शकतात.'
        },
        'hinglish': {
            'keywords': ['ghar', 'house', 'home', 'makaan', 'room', 'kamra'],
            'meaning': 'self, personality, security',
            'interpretation': 'Sapne mein ghar aapke ya aapki psyche ko represent karta hai. Different rooms aapki personality ya life ke different aspects ko symbolize kar sakte hain.'
        }
    },
    
    'fire': {
        'category': 'element',
        'emotion': 'anger',
        'weight': 1,
        'polarity': -1,
        'en': {
            'keywords': ['fire', 'flame', 'burn', 'blaze', 'inferno', 'burning'],
            'meaning': 'passion, anger, transformation, destruction, purification',
            'interpretation': 'Fire can symbolize passion and energy, but also anger and destruction. It represents powerful emotions and transformative forces. Controlled fire suggests harnessed passion, while out-of-control fire indicates overwhelming emotions.'
        },
        'hi': {
            'keywords': ['आग', 'अग्नि', 'ज्वाला', 'जलना', 'धधकती आग'],
            'meaning': 'जुनून, क्रोध, परिवर्तन, विनाश, शुद्धिकरण',
            'interpretation': 'आग जुनून और ऊर्जा का प्रतीक हो सकती है, लेकिन क्रोध और विनाश का भी। यह शक्तिशाली भावनाओं और परिवर्तनकारी शक्तियों का प्रतिनिधित्व करती है। नियंत्रित आग दोहन किए गए जुनून का सुझाव देती है, जबकि बेकाबू आग भारी भावनाओं का संकेत देती है।'
        },
        'mr': {
            'keywords': ['आग', 'अग्नी', 'ज्वाला', 'जळणे', 'धगधगती आग'],
            'meaning': 'उत्कटता, राग, परिवर्तन, विनाश, शुद्धीकरण',
            'interpretation': 'आग उत्कटता आणि ऊर्जा दर्शवू शकते, परंतु राग आणि विनाश देखील. ते शक्तिशाली भावना आणि परिवर्तनकारी शक्तींचे प्रतिनिधित्व करते. नियंत्रित आग दोहन केलेली उत्कटता सूचित करते, तर अनियंत्रित आग जबरदस्त भावना दर्शवते.'
        },
        'hinglish': {
            'keywords': ['aag', 'fire', 'agni', 'flame', 'jalna', 'burning'],
            'meaning': 'passion, anger, transformation',
            'interpretation': 'Aag passion aur energy ko symbolize kar sakti hai, lekin anger aur destruction ko bhi. Ye powerful emotions aur transformative forces ko represent karti hai.'
        }
    },

    'speed': {
        'category': 'movement',
        'emotion': 'joy',
        'weight': 2,
        'polarity': 1,
        'en': {
            'keywords': ['speed', 'fast', 'racing', 'rapid', 'quick'],
            'meaning': 'progress, life momentum, rapid change',
            'interpretation': 'Speed in dreams often represents rapid progress or the quick pace of your life. It suggests a feeling of momentum and moving forward quickly toward your goals.'
        },
        'hi': {
            'keywords': ['गति', 'तेज', 'रफ्तार'],
            'meaning': 'प्रगति, जीवन गति, तेजी से बदलाव',
            'interpretation': 'स्वप्न में गति अक्सर तेजी से प्रगति या आपके जीवन की तेज गति का प्रतिनिधित्व करती है। यह गति की भावना और आपके लक्ष्यों की ओर तेजी से आगे बढ़ने का सुझाव देती है।'
        },
        'mr': {
            'keywords': ['वेग', 'वेगवान', 'गती'],
            'meaning': 'प्रगती, जीवन गती, जलद बदल',
            'interpretation': 'स्वप्नातील वेग अनेकदा जलद प्रगती किंवा तुमच्या जीवनाचा वेगवान वेग दर्शवतो.'
        },
        'hinglish': {
            'keywords': ['speed', 'raftaar', 'tez', 'fast'],
            'meaning': 'progress, life momentum',
            'interpretation': 'Speed sapne mein rapid progress ya life ki fast pace ko represent karti hai. Ye momentum aur goals ki taraf tezi se badhne ka suggestion deti hai.'
        }
    },

    'city': {
        'category': 'place',
        'emotion': 'neutral',
        'weight': 2,
        'polarity': 1,
        'en': {
            'keywords': ['city', 'town', 'urban', 'buildings', 'skyscraper'],
            'meaning': 'social life, career, community, perspective shift',
            'interpretation': 'A city represents your social environment, career ambitions, and community. A small city may suggest a shift in perspective or focusing on a specific social circle.'
        },
        'hi': {
            'keywords': ['शहर', 'नगर', 'कस्बा'],
            'meaning': 'सामाजिक जीवन, करियर, समुदाय, दृष्टिकोण परिवर्तन',
            'interpretation': 'एक शहर आपके सामाजिक वातावरण, करियर की आकांक्षाओं और समुदाय का प्रतिनिधित्व करता है।'
        },
        'mr': {
            'keywords': ['शहर', 'नगर'],
            'meaning': 'सामाजिक जीवन, करिअर, समुदाय',
            'interpretation': 'शहर तुमच्या सामाजिक वातावरणाचे प्रतिनिधित्व करते.'
        },
        'hinglish': {
            'keywords': ['shahar', 'city', 'town', 'basti'],
            'meaning': 'social life, career, perspective shift',
            'interpretation': 'City aapke social environment aur career ambitions ko represent karti hai. Small city perspective shift ya specific social circle par focus suggest karti hai.'
        }
    },

    # ========================================
    # GROWTH, PEACE & ACHIEVEMENT
    # ========================================

    'garden': {
        'category': 'nature',
        'emotion': 'joy',
        'weight': 2,
        'polarity': 1,
        'en': {
            'keywords': ['garden', 'park', 'greenery', 'flowers', 'planting'],
            'meaning': 'inner growth, peace, potential, cultivation',
            'interpretation': 'A garden symbolizes your inner growth and personal potential. It suggests a time of peace and the need to nurture your own development and well-being.'
        },
        'hi': {
            'keywords': ['बगीचा', 'बाग', 'फुलवारी', 'हरियाली'],
            'meaning': 'आंतरिक विकास, शांति, क्षमता',
            'interpretation': 'बगीचा आपके आंतरिक विकास और व्यक्तिगत क्षमता का प्रतीक है।'
        },
        'mr': {
            'keywords': ['बाग', 'बगीचा', 'हिरवळ'],
            'meaning': 'आंतरिक विकास, शांती, क्षमता',
            'interpretation': 'बाग तुमच्या आंतरिक विकासाचे प्रतीक आहे.'
        },
        'hinglish': {
            'keywords': ['bagicha', 'garden', 'park', 'hariyali'],
            'meaning': 'growth, peace, potential',
            'interpretation': 'Garden aapki inner growth aur potential ko symbolize karta hai. Ye shanti aur self-care suggest karta hai.'
        }
    },

    'light': {
        'category': 'nature',
        'emotion': 'joy',
        'weight': 2,
        'polarity': 1,
        'en': {
            'keywords': ['light', 'brightness', 'glow', 'shining', 'sunlight'],
            'meaning': 'clarity, hope, spiritual awareness, truth',
            'interpretation': 'Light in dreams represents clarity, hope, and understanding. It suggests that you are moving toward the truth or gaining a better perspective on a situation.'
        },
        'hi': {
            'keywords': ['प्रकाश', 'रोशनी', 'चमक', 'धूप'],
            'meaning': 'स्पष्टता, आशा, सच्चाई',
            'interpretation': 'सपनों में प्रकाश स्पष्टता, आशा और समझ का प्रतिनिधित्व करता है।'
        },
        'mr': {
            'keywords': ['प्रकाश', 'उजेड', 'चकाकी'],
            'meaning': 'स्पष्टता, आशा, सत्य',
            'interpretation': 'स्वप्नातील प्रकाश स्पष्टता, आशा आणि समज दर्शवतो.'
        },
        'hinglish': {
            'keywords': ['roshni', 'light', 'chamak', 'prakash'],
            'meaning': 'clarity, hope, truth',
            'interpretation': 'Light clarity aur hope ko represent karti hai. Ye suggest karta hai ki aap kisi situation ko better samajh rahe hain.'
        }
    },

    'achievement': {
        'category': 'action',
        'emotion': 'joy',
        'weight': 3,
        'polarity': 1,
        'en': {
            'keywords': ['win', 'success', 'trophy', 'passed', 'award', 'graduating', 'victory'],
            'meaning': 'self-confidence, goal attainment, recognition',
            'interpretation': 'Achievement symbols reflect your self-confidence and the successful attainment of your goals. They suggest that your efforts are paying off.'
        },
        'hi': {
            'keywords': ['जीत', 'सफलता', 'पुरस्कार', 'विजय'],
            'meaning': 'आत्मविश्वास, लक्ष्य प्राप्ति, पहचान',
            'interpretation': 'उपलब्धि के प्रतीक आपके आत्मविश्वास और आपके लक्ष्यों की सफल प्राप्ति को दर्शाते हैं।'
        },
        'mr': {
            'keywords': ['विजय', 'यश', 'पुरस्कार', 'यशस्वी'],
            'meaning': 'आत्मविश्वास, ध्येय प्राप्ती',
            'interpretation': 'यशस्वी होण्याची चिन्हे तुमच्या आत्मविश्वासाचे प्रतिबिंब आहेत.'
        },
        'hinglish': {
            'keywords': ['win', 'jeet', 'success', 'award', 'victory'],
            'meaning': 'confidence, goal attainment',
            'interpretation': 'Achievement symbols aapke confidence aur goals ki success ko reflect karte hain. Aapke efforts pay off ho rahe hain.'
        }
    },

    'safety': {
        'category': 'other',
        'emotion': 'joy',
        'weight': 2,
        'polarity': 1,
        'en': {
            'keywords': ['safe', 'secure', 'shelter', 'protection'],
            'meaning': 'emotional security, comfort, inner peace',
            'interpretation': 'Feeling safe or finding shelter suggests a need for emotional security and comfort in your waking life. It reflects a state of inner peace.'
        },
        'hi': {
            'keywords': ['सुरक्षित', 'सुरक्षा', 'आश्रय'],
            'meaning': 'भावनात्मक सुरक्षा, आराम, शांति',
            'interpretation': 'सुरक्षित महसूस करना आपके जागृत जीवन में भावनात्मक सुरक्षा और आराम की आवश्यकता का सुझाव देता है।'
        },
        'mr': {
            'keywords': ['सुरक्षित', 'सुरक्षा', 'निवारा'],
            'meaning': 'भावनिक सुरक्षा, आराम, शांती',
            'interpretation': 'सुरक्षित वाटणे तुमच्या जागृत जीवनात भावनिक सुरक्षिततेची गरज सूचित करते.'
        },
        'hinglish': {
            'keywords': ['safe', 'surakshit', 'protection'],
            'meaning': 'security, comfort, peace',
            'interpretation': 'Safe feel karna emotional security aur comfort ka suggestion hai. Ye inner peace ko reflect karta hai.'
        }
    },

    # ========================================
    # LITERAL SENTIMENT & OBJECTS
    # ========================================
    
    'joy_literal': {
        'category': 'emotion_literal',
        'emotion': 'joy',
        'weight': 3,
        'polarity': 1,
        'en': {'keywords': ['happy', 'joy', 'excited', 'wonderful', 'amazing'], 'meaning': 'direct happiness', 'interpretation': 'Literal joy.'},
        'hi': {'keywords': ['खुश', 'खुशी', 'आनंद', 'प्रसन्न'], 'meaning': 'सीधी खुशी', 'interpretation': 'सच्ची खुशी।'},
        'mr': {'keywords': ['आनंदी', 'आनंद', 'खुश', 'मजा'], 'meaning': 'थेट आनंद', 'interpretation': 'आनंददायी अनुभव।'},
        'hinglish': {'keywords': ['happy', 'khush', 'mazza', 'amazing', 'achha'], 'meaning': 'direct joy', 'interpretation': 'Happy feeling.'}
    },

    'fear_literal': {
        'category': 'emotion_literal',
        'emotion': 'fear',
        'weight': 3,
        'polarity': -1,
        'en': {'keywords': ['fear', 'scared', 'afraid', 'terrified', 'anxious'], 'meaning': 'direct fear', 'interpretation': 'Literal fear.'},
        'hi': {'keywords': ['डर', 'भय', 'घबराया', 'चिंता'], 'meaning': 'सीधा डर', 'interpretation': 'डर का अनुभव।'},
        'mr': {'keywords': ['भीती', 'घाबरलो', 'चिंता', 'घाबरणे'], 'meaning': 'थेट भीती', 'interpretation': 'भीतीचा अनुभव।'},
        'hinglish': {'keywords': ['dar', 'scared', 'darr', 'anxious', 'tension', 'bhiti', 'ghabra', 'ghabraya'], 'meaning': 'direct fear', 'interpretation': 'Fear feeling.'}
    },

    'car': {
        'category': 'object',
        'emotion': 'neutral',
        'weight': 1,
        'polarity': 0,
        'en': {'keywords': ['car', 'vehicle', 'automobile'], 'meaning': 'life direction, movement', 'interpretation': 'A car often represents your drive and direction in life.'},
        'hi': {'keywords': ['गाड़ी', 'कार', 'वाहन'], 'meaning': 'जीवन की दिशा', 'interpretation': 'गाड़ी अक्सर जीवन में आपकी गति का प्रतिनिधित्व करती है।'},
        'mr': {'keywords': ['गाडी', 'कार', 'वाहन'], 'meaning': 'जीवन प्रवास', 'interpretation': 'गाडी तुमच्या जीवनातील प्रवासाचे प्रतीक आहे।'},
        'hinglish': {'keywords': ['gadi', 'car', 'gaadi', 'vehicle'], 'meaning': 'life direction', 'interpretation': 'Car life direction aur movement symbolize karti hai.'}
    }
}


# Symbol categories for classification
SYMBOL_CATEGORIES = {
    'water': ['ocean', 'river', 'rain', 'flood'],
    'movement': ['flying', 'falling'],
    'animal': ['dog', 'cat', 'bird', 'spider', 'snake'],
    'environment': ['darkness'],
    'life_event': ['death'],
    'action': ['chase'],
    'situation': ['exam', 'late'],
    'body': ['teeth_falling'],
    'place': ['house'],
    'element': ['fire'],
    'emotion_literal': ['joy_literal', 'fear_literal'],
    'object': ['car']
}


# Emotion-based symbol grouping
EMOTION_SYMBOLS = {
    'fear': ['falling', 'flood', 'spider', 'snake', 'darkness', 'chase', 'exam', 'teeth_falling', 'late', 'fear_literal'],
    'joy': ['flying', 'bird', 'joy_literal'],
    'love': ['dog'],
    'sadness': ['rain', 'death'],
    'anger': ['fire'],
    'neutral': ['ocean', 'river', 'cat', 'house', 'car']
}


def get_symbol_data(symbol_key, lang_code='en'):
    """Get symbol data for a specific language."""
    symbol = DREAM_SYMBOLS.get(symbol_key, {})
    return symbol.get(lang_code, symbol.get('en', {}))


def get_symbol_category(symbol_key):
    """Get the category of a symbol."""
    symbol = DREAM_SYMBOLS.get(symbol_key, {})
    return symbol.get('category', 'other')


def get_symbol_emotion(symbol_key):
    """Get the primary emotion associated with a symbol."""
    symbol = DREAM_SYMBOLS.get(symbol_key, {})
    return symbol.get('emotion', 'neutral')


def find_symbols_in_text(text, lang_code='en'):
    """Find dream symbols in text for a specific language."""
    if not text:
        return []
    
    text_lower = text.lower()
    found_symbols = []
    seen_symbols = set()
    
    # Check both the detected language and Hinglish if the script is Latin (en)
    langs_to_check = [lang_code]
    if lang_code == 'en' and 'hinglish' not in langs_to_check:
        langs_to_check.append('hinglish')
    
    for symbol_key, symbol_data in DREAM_SYMBOLS.items():
        if symbol_key in seen_symbols:
            continue
            
        # Try each applicable language
        for current_lang in langs_to_check:
            lang_data = symbol_data.get(current_lang, {})
            if not lang_data and current_lang == lang_code:
                lang_data = symbol_data.get('en', {}) # Final fallback
                
            keywords = lang_data.get('keywords', [])
            
            for keyword in keywords:
                if keyword.lower() in text_lower:
                    found_symbols.append({
                        'symbol': symbol_key,
                        'keyword': keyword,
                        'meaning': lang_data.get('meaning', ''),
                        'interpretation': lang_data.get('interpretation', ''),
                        'category': symbol_data.get('category', 'other'),
                        'emotion': symbol_data.get('emotion', 'neutral'),
                        'weight': symbol_data.get('weight', 1),
                        'polarity': symbol_data.get('polarity', 0)
                    })
                    seen_symbols.add(symbol_key)
                    break
            
            if symbol_key in seen_symbols:
                break
    
    return found_symbols


def get_symbols_by_category(category):
    """Get all symbols in a specific category."""
    return SYMBOL_CATEGORIES.get(category, [])


def get_symbols_by_emotion(emotion):
    """Get all symbols associated with a specific emotion."""
    return EMOTION_SYMBOLS.get(emotion, [])
