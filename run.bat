@echo off
echo 🚀 تشغيل تطبيق كاشف الرسائل المزعجة...
echo Starting Spam Detector App...
echo.

REM التحقق من وجود Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python غير مثبت. يرجى تثبيت Python أولاً.
    echo ❌ Python is not installed. Please install Python first.
    pause
    exit /b 1
)

echo ✅ Python متوفر
echo ✅ Python is available
echo.

REM تشغيل التطبيق
echo 🔄 تشغيل التطبيق...
echo 🔄 Starting application...
streamlit run app.py

pause
