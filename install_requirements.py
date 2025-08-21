#!/usr/bin/env python3
"""
ملف تثبيت المكتبات المطلوبة للمشروع
Install required libraries for the project
"""

import os
import subprocess
import sys

def install_package(package):
    """تثبيت مكتبة واحدة"""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package], 
                              stdout=subprocess.DEVNULL, 
                              stderr=subprocess.DEVNULL)
        return True
    except subprocess.CalledProcessError:
        return False

def install_from_requirements():
    """تثبيت المكتبات من ملف requirements.txt"""
    if os.path.exists("requirements.txt"):
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"],
                                 stdout=subprocess.DEVNULL, 
                                 stderr=subprocess.DEVNULL)
            return True
        except subprocess.CalledProcessError:
            return False
    else:
        return False

def main():
    """الدالة الرئيسية"""
    print("🚀 بدء تثبيت المكتبات المطلوبة...")
    
    # تحديث pip
    print("📦 تحديث pip...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
    
    # تثبيت المكتبات
    if install_from_requirements():
        print("\n🎉 تم الانتهاء من تثبيت جميع المكتبات!")
        print("🚀 يمكنك الآن تشغيل التطبيق باستخدام: streamlit run app.py")
    else:
        print("\n⚠️ يرجى التحقق من الأخطاء وإعادة المحاولة")

if __name__ == "__main__":
    main()
if __name__ == "__main__":
    main()
