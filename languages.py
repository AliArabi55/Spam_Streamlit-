"""
ملف النصوص واللغات المتعددة
Multilingual text file
"""

# Language dictionary
LANGUAGES = {
    "English": {
        "page_title": "🛡️ Spam Detector",
        "main_header": "🛡️ Spam Message Detector",
        "sub_header": "AI Technology for Text Message Classification",
        "project_info": "📊 Project Information",
        "model_accuracy": "📈 Model Performance",
        "model_accuracy_desc": """**Accuracy: 97%**
        
**Spam Classification:**
- Precision: 1.00
- Recall: 0.75  
- F1-score: 0.86

**Ham Classification:**
- Precision: 0.96
- Recall: 1.00
- F1-score: 0.98""",
        "enter_message": "📝 Enter Message to Analyze",
        "message_placeholder": "Type your message here to check if it's spam or not...",
        "analyze_button": "🔍 Analyze Message",
        "ham_examples": "✅ Ham Examples (Expected Normal Messages)",
        "ham_examples_list": """1. "Are we still meeting for lunch tomorrow?"
2. "Please call me when you arrive."
3. "Happy birthday! Wishing you all the best."
4. "Don't forget to bring your notebook for class."
5. "Can you send me the report before 5 pm?"
6. "Thanks for helping me with the project yesterday."
7. "The meeting has been moved to 3 PM today."
8. "Could you pick up some groceries on your way home?"
9. "I'll be running about 10 minutes late."
10. "Great job on the presentation today!" """,
        "spam_examples": "🚨 Spam Examples (Expected Spam Messages)",
        "spam_examples_list": """1. "Congratulations! You have won a free lottery ticket. Claim now!"
2. "URGENT! Your account will be suspended unless you verify immediately."
3. "You've been selected for a $1000 Walmart gift card."
4. "Win a brand new iPhone by clicking this link."
5. "Get cheap loans instantly, no credit check required."
6. "WINNER! You've won $5000! Text STOP to claim your prize!"
7. "Your credit card has been compromised. Click here to secure it."
8. "Free vacation to Hawaii! Limited time offer, act now!"
9. "Make $500 per day working from home! No experience needed."
10. "ALERT: Suspicious activity on your account. Verify now or lose access!" """,
        "try_examples": "💡 Try These Examples",
        "enter_message_warning": "⚠️ Please enter a message first.",
        "analyzing": "🔄 Analyzing message...",
        "analysis_results": "📊 Analysis Results",
        "spam_warning": "🚨 Warning: This is a spam message",
        "confidence_level": "Confidence Level",
        "spam_tips": "⚠️ Tips for dealing with spam messages:",
        "spam_tips_list": """- Don't click on suspicious links
- Don't share your personal information
- Delete the message immediately
- Report the message if possible""",
        "ham_result": "✅ This is a normal and safe message",
        "ham_tips": "✅ Message is safe:",
        "ham_tips_list": """- You can read the content safely
- The message contains no spam content
- You can interact with it normally""",
        "word_count": "Word Count",
        "char_count": "Character Count",
        "footer_text": """🔬 This project was developed using modern artificial intelligence techniques
to help protect users from spam and harmful messages""",
        "language_toggle": "🌐 Language"
    },
    "Deutsch": {
        "page_title": "🛡️ Spam-Detektor",
        "main_header": "🛡️ Spam-Nachrichten-Detektor",
        "sub_header": "KI-Technologie für die Klassifizierung von Textnachrichten",
        "project_info": "📊 Projektinformationen",
        "model_accuracy": "📈 Modellleistung",
        "model_accuracy_desc": """**Genauigkeit: 97%**
        
**Spam-Klassifizierung:**
- Präzision: 1.00
- Recall: 0.75
- F1-Score: 0.86

**Ham-Klassifizierung:**
- Präzision: 0.96
- Recall: 1.00
- F1-Score: 0.98""",
        "enter_message": "📝 Nachricht zur Analyse eingeben",
        "message_placeholder": "Geben Sie hier Ihre Nachricht ein, um zu prüfen, ob es sich um Spam handelt...",
        "analyze_button": "🔍 Nachricht analysieren",
        "ham_examples": "✅ Ham-Beispiele (Erwartete normale Nachrichten)",
        "ham_examples_list": """1. "Treffen wir uns immer noch morgen zum Mittagessen?"
2. "Bitte ruf mich an, wenn du ankommst."
3. "Alles Gute zum Geburtstag! Ich wünsche dir alles Beste."
4. "Vergiss nicht, dein Notizbuch für den Unterricht mitzubringen."
5. "Kannst du mir den Bericht vor 17 Uhr schicken?"
6. "Danke, dass du mir gestern bei dem Projekt geholfen hast."
7. "Das Meeting wurde auf 15 Uhr heute verlegt."
8. "Könntest du auf dem Heimweg Lebensmittel einkaufen?"
9. "Ich werde etwa 10 Minuten zu spät kommen."
10. "Großartige Arbeit bei der Präsentation heute!" """,
        "spam_examples": "🚨 Spam-Beispiele (Erwartete Spam-Nachrichten)",
        "spam_examples_list": """1. "Glückwunsch! Sie haben ein kostenloses Lotterielos gewonnen. Jetzt einlösen!"
2. "DRINGEND! Ihr Konto wird gesperrt, es sei denn, Sie verifizieren sofort."
3. "Sie wurden für eine 1000€ Walmart-Geschenkkarte ausgewählt."
4. "Gewinnen Sie ein brandneues iPhone, indem Sie auf diesen Link klicken."
5. "Erhalten Sie günstige Kredite sofort, keine Bonitätsprüfung erforderlich."
6. "GEWINNER! Sie haben 5000€ gewonnen! Senden Sie STOP um Ihren Preis zu beanspruchen!"
7. "Ihre Kreditkarte wurde kompromittiert. Klicken Sie hier, um sie zu sichern."
8. "Kostenloser Urlaub nach Hawaii! Zeitlich begrenztes Angebot, handeln Sie jetzt!"
9. "Verdienen Sie 500€ pro Tag von zu Hause! Keine Erfahrung erforderlich."
10. "ALARM: Verdächtige Aktivitäten auf Ihrem Konto. Jetzt verifizieren oder Zugang verlieren!" """,
        "try_examples": "💡 Probieren Sie diese Beispiele aus",
        "enter_message_warning": "⚠️ Bitte geben Sie zuerst eine Nachricht ein.",
        "analyzing": "🔄 Nachricht wird analysiert...",
        "analysis_results": "📊 Analyseergebnisse",
        "spam_warning": "🚨 Warnung: Dies ist eine Spam-Nachricht",
        "confidence_level": "Vertrauensniveau",
        "spam_tips": "⚠️ Tipps zum Umgang mit Spam-Nachrichten:",
        "spam_tips_list": """- Klicken Sie nicht auf verdächtige Links
- Teilen Sie Ihre persönlichen Informationen nicht
- Löschen Sie die Nachricht sofort
- Melden Sie die Nachricht, wenn möglich""",
        "ham_result": "✅ Dies ist eine normale und sichere Nachricht",
        "ham_tips": "✅ Nachricht ist sicher:",
        "ham_tips_list": """- Sie können den Inhalt sicher lesen
- Die Nachricht enthält keinen Spam-Inhalt
- Sie können normal damit interagieren""",
        "word_count": "Wortanzahl",
        "char_count": "Zeichenanzahl",
        "footer_text": """🔬 Dieses Projekt wurde mit modernen KI-Techniken entwickelt
um Benutzer vor Spam und schädlichen Nachrichten zu schützen""",
        "language_toggle": "🌐 Sprache"
    }
}
