"""
ملف الأنماط والتصميم للتطبيق
Styles and Design file for the application
"""

import streamlit as st

def apply_custom_styles():
    """تطبيق الأنماط المخصصة للتطبيق"""
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
        .accuracy-box {
            background: linear-gradient(135deg, #74b9ff 0%, #0984e3 100%);
            padding: 1.5rem;
            border-radius: 10px;
            color: white;
            margin: 1rem 0;
        }
        .example-box {
            background: #1e1e1e;
            padding: 1.5rem;
            border-radius: 8px;
            border-left: 4px solid #28a745;
            margin: 0.5rem 0;
            box-shadow: 0 2px 4px rgba(0,0,0,0.3);
        }
        .example-box pre {
            color: #ffffff !important;
            font-family: 'Segoe UI', Arial, sans-serif !important;
            font-size: 14px;
            line-height: 1.6;
            margin: 0;
            white-space: pre-wrap;
            background: transparent;
        }
        .spam-example-box {
            background: #1e1e1e;
            padding: 1.5rem;
            border-radius: 8px;
            border-left: 4px solid #dc3545;
            margin: 0.5rem 0;
            box-shadow: 0 2px 4px rgba(0,0,0,0.3);
        }
        .spam-example-box pre {
            color: #ffffff !important;
            font-family: 'Segoe UI', Arial, sans-serif !important;
            font-size: 14px;
            line-height: 1.6;
            margin: 0;
            white-space: pre-wrap;
            background: transparent;
        }
    </style>
    """, unsafe_allow_html=True)

def configure_page():
    """إعداد صفحة التطبيق"""
    st.set_page_config(
        page_title="🛡️ Spam Detector",
        page_icon="🛡️",
        layout="wide",
        initial_sidebar_state="expanded"
    )
