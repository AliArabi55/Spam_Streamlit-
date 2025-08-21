# 🛡️ Spam Message Detector

A powerful AI-powered spam detection application built with Streamlit that analyzes text messages and classifies them as spam or ham (normal messages).

## 📊 Model Performance

- **Accuracy: 97%**
- **Spam Classification:**
  - Precision: 1.00
  - Recall: 0.75
  - F1-score: 0.86
- **Ham Classification:**
  - Precision: 0.96
  - Recall: 1.00
  - F1-score: 0.98

## 🗂️ Project Structure

```
├── app.py                 # Main application file (with auto-install)
├── styles.py              # UI styles and design components
├── languages.py           # Multilingual support (English/German)
├── spam_classifier.pkl    # Trained machine learning model
├── vectorizer.pkl         # Text vectorizer for preprocessing
├── requirements.txt       # Required Python packages
├── run.bat               # Quick launcher for Windows
└── README.md             # This file
```

## 🛠️ Installation & Setup

### Quick Start (Windows)

For Windows users, simply double-click `run.bat` or run:
```bash
run.bat
```

### Automatic Installation (All Systems)

The app automatically checks for and installs all required packages when you run it:

```bash
streamlit run app.py
```

The application will:
1. ✅ Check if all required packages are installed
2. 📦 Automatically install missing packages from `requirements.txt`
3. 🔍 Display installation status in the console
4. 🎉 Start the spam detection interface

### Manual Installation

If you prefer to install packages manually:

```bash
# Clone the repository
git clone https://github.com/AliArabi55/Spam_Streamlit-.git
cd Spam_Streamlit-

# Install required packages
pip install -r requirements.txt

# Run the application
streamlit run app.py
```

## 📦 Required Packages

The following packages are automatically installed from `requirements.txt`:

- `streamlit>=1.28.0` - Web app framework
- `joblib>=1.3.0` - Model serialization
- `scikit-learn>=1.3.0` - Machine learning library
- `pandas>=1.5.0` - Data manipulation
- `numpy>=1.24.0` - Numerical computing

## 🚀 Features

- **Real-time Analysis**: Instant spam detection for any text message
- **High Accuracy**: 97% accuracy with robust performance metrics
- **Multilingual Support**: Available in English and German
- **Interactive Examples**: Pre-loaded examples for testing
- **Clean Interface**: Modern, user-friendly design
- **Detailed Results**: Confidence levels and message statistics

## 💡 Example Messages

### ✅ Ham Examples (Normal Messages)
1. "Are we still meeting for lunch tomorrow?"
2. "Please call me when you arrive."
3. "Happy birthday! Wishing you all the best."
4. "Don't forget to bring your notebook for class."
5. "Can you send me the report before 5 pm?"

### 🚨 Spam Examples (Spam Messages)
1. "Congratulations! You have won a free lottery ticket. Claim now!"
2. "URGENT! Your account will be suspended unless you verify immediately."
3. "You've been selected for a $1000 Walmart gift card."
4. "Win a brand new iPhone by clicking this link."
5. "Get cheap loans instantly, no credit check required."

## 🛠️ Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone https://github.com/AliArabi55/Spam_Streamlit-.git
   cd Spam_Streamlit-
   ```

2. **Install dependencies:**
   ```bash
   pip install streamlit joblib scikit-learn
   ```

3. **Run the application:**
   ```bash
   streamlit run app.py
   ```

4. **Open your browser** and navigate to `http://localhost:8501`

## 🔧 Technical Details

- **Framework**: Streamlit for web interface
- **Machine Learning**: Scikit-learn for model training
- **Language Processing**: TF-IDF vectorization
- **Model**: Support Vector Machine (SVM) classifier
- **Languages**: Python 3.7+

## 🌐 Language Support

The application supports:
- 🇺🇸 English
- 🇩🇪 Deutsch (German)

## 📈 How It Works

1. **Text Input**: User enters a message to analyze
2. **Preprocessing**: Text is cleaned and vectorized using TF-IDF
3. **Classification**: Pre-trained SVM model predicts spam/ham
4. **Results**: Display prediction with confidence level and statistics

## 🔒 Security Tips

- Never click on suspicious links in messages
- Don't share personal information through unverified messages
- Delete spam messages immediately
- Report suspicious messages to relevant authorities

## 🤝 Contributing

Feel free to fork this project and submit pull requests for improvements!

## 📄 License

This project is open source and available under the [MIT License](LICENSE).