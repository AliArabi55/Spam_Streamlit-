import streamlit as st
import joblib

# Language dictionary
LANGUAGES = {
    "English": {
        "page_title": "🛡️ Spam Detector",
        "main_header": "🛡️ Spam Message Detector",
        "sub_header": "AI Technology for Text Message Classification",
        "project_info": "📊 Project Information",
        "project_goal": "🎯 Project Goal",
        "project_goal_desc": """This project uses artificial intelligence techniques to analyze text messages and classify them into:
- **Spam**: Unwanted or annoying messages
- **Ham**: Normal and useful messages""",
        "technologies": "🔧 Technologies Used",
        "technologies_list": """- **Machine Learning**: Machine learning algorithms
- **Natural Language Processing**: Natural language processing
- **Streamlit**: Interactive user interface
- **Python**: Main programming language""",
        "model_accuracy": "📈 Model Accuracy",
        "model_accuracy_desc": "The model is trained on thousands of messages and achieves high classification accuracy",
        "how_it_works": "🚀 How Does the Project Work?",
        "how_it_works_desc": """This project uses advanced machine learning techniques to analyze text message content. 
When you enter a message, the system:""",
        "how_it_works_steps": """<li>Analyzes the text and understands its content</li>
            <li>Extracts important features from the text</li>
            <li>Compares these features with pre-trained models</li>
            <li>Provides accurate classification of the message</li>""",
        "enter_message": "📝 Enter Message to Analyze",
        "message_placeholder": "Example: Congratulations! You've won a $1000 prize. Click the link to claim it...",
        "analyze_button": "🔍 Analyze Message",
        "tool_features": "✨ Tool Features",
        "features_list": """<li>Fast analysis</li>
            <li>High accuracy</li>
            <li>Easy to use</li>
            <li>Interactive interface</li>""",
        "spam_examples": "🛡️ Examples of Spam Messages",
        "spam_examples_list": """<li>Fake prize messages</li>
            <li>Suspicious financial offers</li>
            <li>Malicious links</li>
            <li>Personal information requests</li>""",
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
        "project_goal": "🎯 Projektziel",
        "project_goal_desc": """Dieses Projekt nutzt Techniken der künstlichen Intelligenz zur Analyse von Textnachrichten und klassifiziert sie in:
- **Spam**: Unerwünschte oder störende Nachrichten
- **Ham**: Normale und nützliche Nachrichten""",
        "technologies": "🔧 Verwendete Technologien",
        "technologies_list": """- **Machine Learning**: Algorithmen des maschinellen Lernens
- **Natural Language Processing**: Verarbeitung natürlicher Sprache
- **Streamlit**: Interaktive Benutzeroberfläche
- **Python**: Hauptprogrammiersprache""",
        "model_accuracy": "📈 Modellgenauigkeit",
        "model_accuracy_desc": "Das Modell ist auf Tausenden von Nachrichten trainiert und erreicht hohe Klassifizierungsgenauigkeit",
        "how_it_works": "🚀 Wie funktioniert das Projekt?",
        "how_it_works_desc": """Dieses Projekt verwendet fortschrittliche Machine-Learning-Techniken zur Analyse von Textnachrichteninhalten. 
Wenn Sie eine Nachricht eingeben, führt das System folgende Schritte aus:""",
        "how_it_works_steps": """<li>Analysiert den Text und versteht seinen Inhalt</li>
            <li>Extrahiert wichtige Merkmale aus dem Text</li>
            <li>Vergleicht diese Merkmale mit vortrainierten Modellen</li>
            <li>Bietet genaue Klassifizierung der Nachricht</li>""",
        "enter_message": "📝 Nachricht zur Analyse eingeben",
        "message_placeholder": "Beispiel: Glückwunsch! Sie haben einen 1000€ Preis gewonnen. Klicken Sie auf den Link, um ihn zu beanspruchen...",
        "analyze_button": "🔍 Nachricht analysieren",
        "tool_features": "✨ Tool-Funktionen",
        "features_list": """<li>Schnelle Analyse</li>
            <li>Hohe Genauigkeit</li>
            <li>Einfach zu bedienen</li>
            <li>Interaktive Oberfläche</li>""",
        "spam_examples": "🛡️ Beispiele für Spam-Nachrichten",
        "spam_examples_list": """<li>Gefälschte Preisnachrichten</li>
            <li>Verdächtige Finanzangebote</li>
            <li>Schädliche Links</li>
            <li>Anfragen nach persönlichen Informationen</li>""",
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

# Initialize session state for language
if 'language' not in st.session_state:
    st.session_state.language = 'English'

# Page configuration
st.set_page_config(
    page_title=LANGUAGES[st.session_state.language]["page_title"],
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 1rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    .sub-header {
        font-size: 1.2rem;
        color: #555;
        text-align: center;
        margin-bottom: 2rem;
    }
    .info-box {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
        margin: 1rem 0;
    }
    .result-spam {
        background: linear-gradient(90deg, #ff6b6b, #ee5a52);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        font-size: 1.2rem;
        font-weight: bold;
    }
    .result-ham {
        background: linear-gradient(90deg, #51cf66, #40c057);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        font-size: 1.2rem;
        font-weight: bold;
    }
    .feature-box {
        background: #f8f9fa;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #1f77b4;
        margin: 0.5rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Load the saved model and vectorizer
@st.cache_resource
def load_models():
    model = joblib.load("spam_classifier.pkl")
    vectorizer = joblib.load("vectorizer.pkl")
    return model, vectorizer

model, vectorizer = load_models()

# Get current language texts
texts = LANGUAGES[st.session_state.language]

# Main header
st.markdown(f'<h1 class="main-header">{texts["main_header"]}</h1>', unsafe_allow_html=True)
st.markdown(f'<p class="sub-header">{texts["sub_header"]}</p>', unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    # Language toggle
    st.markdown(f"### {texts['language_toggle']}")
    language_options = ["English", "Deutsch"]
    selected_language = st.selectbox(
        "",
        language_options,
        index=language_options.index(st.session_state.language),
        key="language_selector"
    )
    
    # Update language if changed
    if selected_language != st.session_state.language:
        st.session_state.language = selected_language
        st.rerun()
    
    st.markdown("---")
    st.header(texts["project_info"])
    
    st.markdown(f"""
    ### {texts["project_goal"]}
    {texts["project_goal_desc"]}
    """)
    
    st.markdown(f"""
    ### {texts["technologies"]}
    {texts["technologies_list"]}
    """)
    
    st.markdown(f"""
    ### {texts["model_accuracy"]}
    {texts["model_accuracy_desc"]}
    """)

# Main content area
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown(f"""
    <div class="info-box">
        <h3>{texts["how_it_works"]}</h3>
        <p>{texts["how_it_works_desc"]}</p>
        <ul>
            {texts["how_it_works_steps"]}
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # Input section
    st.markdown(f"### {texts['enter_message']}")
    user_input = st.text_area(
        texts["enter_message"].replace("📝 ", "").replace("### ", ""),
        height=120,
        placeholder=texts["message_placeholder"]
    )
    
    # Prediction section
    col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
    with col_btn2:
        predict_button = st.button(texts["analyze_button"], use_container_width=True)

with col2:
    st.markdown(f"""
    <div class="feature-box">
        <h4>{texts["tool_features"]}</h4>
        <ul>
            {texts["features_list"]}
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="feature-box">
        <h4>{texts["spam_examples"]}</h4>
        <ul>
            {texts["spam_examples_list"]}
        </ul>
    </div>
    """, unsafe_allow_html=True)

# Prediction logic
if predict_button:
    if user_input.strip() == "":
        st.warning(texts["enter_message_warning"])
    else:
        with st.spinner(texts["analyzing"]):
            # Transform the input text using the vectorizer
            vec = vectorizer.transform([user_input])
            # Predict using the model
            pred = model.predict(vec)[0]
            probability = model.predict_proba(vec)[0]
            
            # Display results
            st.markdown("---")
            st.markdown(f"### {texts['analysis_results']}")
            
            if pred == 1:
                st.markdown(f"""
                <div class="result-spam">
                    {texts["spam_warning"]} (Spam)
                    <br>{texts["confidence_level"]}: {probability[1]:.1%}
                </div>
                """, unsafe_allow_html=True)
                
                st.markdown(f"""
                ### {texts["spam_tips"]}
                {texts["spam_tips_list"]}
                """)
            else:
                st.markdown(f"""
                <div class="result-ham">
                    {texts["ham_result"]} (Ham)
                    <br>{texts["confidence_level"]}: {probability[0]:.1%}
                </div>
                """, unsafe_allow_html=True)
                
                st.markdown(f"""
                ### {texts["ham_tips"]}
                {texts["ham_tips_list"]}
                """)
            
            # Additional analysis
            st.markdown("---")
            col_stats1, col_stats2, col_stats3 = st.columns(3)
            
            with col_stats1:
                st.metric(texts["word_count"], len(user_input.split()))
            
            with col_stats2:
                st.metric(texts["char_count"], len(user_input))
            
            with col_stats3:
                confidence = max(probability[0], probability[1])
                st.metric(texts["confidence_level"], f"{confidence:.1%}")

# Footer
st.markdown("---")
st.markdown(f"""
<div style="text-align: center; color: #666; padding: 2rem;">
    <p>{texts["footer_text"]}</p>
</div>
""", unsafe_allow_html=True)
