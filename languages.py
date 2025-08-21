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
        "spam_examples_list": """
        
1. "Free entry in 2 a wkly comp to win FA Cup final tkts 21st May 2005. Text FA to 87121 to receive entry question(std txt rate)T\&C's apply 08452810075over18's"

2. "URGENT! You have won a 1 week FREE membership in our £100,000 Prize Jackpot! Txt the word: CLAIM to No: 81010 T\&C [www.dbuk.net](http://www.dbuk.net) LCCLTD POBOX 4403LDNW1A7RW18"

3. "WINNER!! As a valued network customer you have been selected to receive a £900 prize reward! To claim call 09061701461. Claim code KL341. Valid 12 hours only."

4. "Had your mobile 11 months or more? U R entitled to Update to the latest colour mobiles with camera for Free! Call The Mobile Update Co FREE on 08002986030"

5. "SIX chances to win CASH! From 100 to 20,000 pounds txt> CSH11 and send to 87575. Cost 150p/day, 6days, 16+ TsandCs apply Reply HL 4 info"

6. "URGENT! You have won a 1 week FREE membership in our £100,000 Prize Jackpot! Txt the word: CLAIM to No: 81010 T\&C [www.dbuk.net](http://www.dbuk.net) LCCLTD POBOX 4403LDNW1A7RW18"

7. "XXXMobileMovieClub: To use your credit, click the WAP link in the next txt message or click here>> [http://wap](http://wap). [https://www.google.com/url?sa=E\&source=gmail\&q=xxxmobilemovieclub.com?n=QJKGIGHJJGCBL](https://www.google.com/url?sa=E&source=gmail&q=xxxmobilemovieclub.com?n=QJKGIGHJJGCBL)"

8. "England v Macedonia - dont miss the goals/team news. Txt ur national team to 87077 eg ENGLAND to 87077 Try\:WALES, SCOTLAND 4txt/£1.20 POBOXox36504W45WQ 16+"

9. "Thanks for your subscription to Ringtone UK your mobile will be charged £5/month Please confirm by replying YES or NO. If you reply NO you will not be charged"

10. "Rodger Burns - MSG = We tried to call you re your reply to our sms for a free nokia mobile + free camcorder. Please call now 08000930705 for delivery tomorrow"

         
         """,
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
        "spam_examples_list": """
  
1. "Kostenloser Eintritt in einen wöchentlichen Wettbewerb, um Tickets für das FA-Cup-Finale am 21. Mai 2005 zu gewinnen. Sende FA an 87121, um die Teilnahmefrage zu erhalten (Standard-SMS-Gebühr). AGB gelten 08452810075 ab 18 Jahren."

2. "DRINGEND! Sie haben eine 1-wöchige KOSTENLOSE Mitgliedschaft in unserem £100.000 Preis-Jackpot gewonnen! Senden Sie das Wort: CLAIM an Nr.: 81010 AGB [www.dbuk.net](http://www.dbuk.net) LCCLTD POBOX 4403LDNW1A7RW18."

3. "GEWINNER!! Als geschätzter Netzwerkkunde wurden Sie ausgewählt, eine £900-Preisbelohnung zu erhalten! Um Ihren Gewinn zu beanspruchen, rufen Sie 09061701461 an. Anspruchscode KL341. Nur 12 Stunden gültig."

4. "Haben Sie Ihr Handy seit 11 Monaten oder länger? Sie haben Anspruch auf ein Upgrade auf die neuesten Farb-Handys mit Kamera – KOSTENLOS! Rufen Sie die Mobile Update Co KOSTENLOS an unter 08002986030."

5. "SECHS Chancen, BARGELD zu gewinnen! Von 100 bis 20.000 Pfund. Senden Sie CSH11 an 87575. Kosten 150p/Tag, 6 Tage, ab 16+. AGB gelten. Antworten Sie mit HL für Infos."

6. "DRINGEND! Sie haben eine 1-wöchige KOSTENLOSE Mitgliedschaft in unserem £100.000 Preis-Jackpot gewonnen! Senden Sie das Wort: CLAIM an Nr.: 81010 AGB [www.dbuk.net](http://www.dbuk.net) LCCLTD POBOX 4403LDNW1A7RW18."

7. "XXXMobileMovieClub: Um Ihr Guthaben zu nutzen, klicken Sie auf den WAP-Link in der nächsten SMS oder klicken Sie hier >> [http://wap](http://wap). [https://www.google.com/url?sa=E\&source=gmail\&q=xxxmobilemovieclub.com?n=QJKGIGHJJGCBL](https://www.google.com/url?sa=E&source=gmail&q=xxxmobilemovieclub.com?n=QJKGIGHJJGCBL)."

8. "England gegen Mazedonien – verpassen Sie nicht die Tore/Team-News. Senden Sie Ihr Nationalteam an 87077, z. B. ENGLAND an 87077. Probieren Sie: WALES, SCOTLAND. 4 SMS/£1.20 POBOXox36504W45WQ ab 16 Jahren."

9. "Danke für Ihr Abonnement bei Ringtone UK. Ihr Handy wird mit £5/Monat belastet. Bitte bestätigen Sie mit JA oder NEIN. Wenn Sie NEIN antworten, wird Ihnen nichts berechnet."

10. "Rodger Burns – NACHRICHT = Wir haben versucht, Sie bezüglich Ihrer Antwort auf unsere SMS für ein kostenloses Nokia-Handy + kostenlosen Camcorder anzurufen. Bitte rufen Sie jetzt 08000930705 an für die Lieferung morgen."


         """,
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
