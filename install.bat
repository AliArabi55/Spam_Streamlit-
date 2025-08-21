@echo off
echo 🚀 Installing required packages for Spam Classifier...
echo تثبيت المكتبات المطلوبة لمكتشف الرسائل المزعجة...

REM تحديث pip
echo 📦 Updating pip...
python -m pip install --upgrade pip

REM تثبيت المكتبات
echo 📦 Installing packages from requirements.txt...
python -m pip install -r requirements.txt

REM التحقق من التثبيت
echo ✅ Checking installation...
python -c "import streamlit, joblib, sklearn; print('All packages installed successfully!')"

echo.
echo 🎉 Installation completed!
echo يمكنك الآن تشغيل التطبيق باستخدام:
echo streamlit run app.py
echo.
pause
