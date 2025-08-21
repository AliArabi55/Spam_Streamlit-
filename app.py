import subprocess
import sys

# تأكد من تثبيت joblib
subprocess.check_call([sys.executable, "-m", "pip", "install", "joblib"])

import streamlit as st
import joblib
from styles import apply_custom_styles, configure_page
from languages import LANGUAGES

# إعداد الصفحة والأنماط
configure_page()
apply_custom_styles()

# Initialize session state for language
if 'language' not in st.session_state:
    st.session_state.language = 'English'

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
    
    # Model Accuracy Section
    st.markdown(f"""
    <div class="accuracy-box">
        <h3>{texts["model_accuracy"]}</h3>
        <p>{texts["model_accuracy_desc"]}</p>
    </div>
    """, unsafe_allow_html=True)

# Main content area
col1, col2 = st.columns([3, 2])

with col1:
    # Input section
    st.markdown(f"## {texts['enter_message']}")
    user_input = st.text_area(
        "",
        height=150,
        placeholder=texts["message_placeholder"],
        key="message_input"
    )
    
    # Analyze button
    analyze_button = st.button(texts["analyze_button"], use_container_width=True, type="primary")
    
    # Prediction logic
    if analyze_button:
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
                        {texts["spam_warning"]} 
                        <br><strong>{texts["confidence_level"]}: {probability[1]:.1%}</strong>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    st.markdown(f"""
                    ### {texts["spam_tips"]}
                    {texts["spam_tips_list"]}
                    """)
                else:
                    st.markdown(f"""
                    <div class="result-ham">
                        {texts["ham_result"]} 
                        <br><strong>{texts["confidence_level"]}: {probability[0]:.1%}</strong>
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

with col2:
    # Examples section
    st.markdown(f"## {texts['try_examples']}")
    
    # Ham Examples
    with st.expander(texts["ham_examples"], expanded=False):
        st.markdown(f"""
        <div class="example-box">
            <pre style="color: #2c3e50; font-family: 'Segoe UI', Arial, sans-serif; white-space: pre-wrap; margin: 0;">{texts["ham_examples_list"]}</pre>
        </div>
        """, unsafe_allow_html=True)
    
    # Spam Examples
    with st.expander(texts["spam_examples"], expanded=False):
        st.markdown(f"""
        <div class="spam-example-box">
            <pre style="color: #721c24; font-family: 'Segoe UI', Arial, sans-serif; white-space: pre-wrap; margin: 0;">{texts["spam_examples_list"]}</pre>
        </div>
        """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown(f"""
<div style="text-align: center; color: #666; padding: 2rem;">
    <p>{texts["footer_text"]}</p>
</div>
""", unsafe_allow_html=True)
