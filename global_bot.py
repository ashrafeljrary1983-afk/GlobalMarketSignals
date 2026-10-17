import os
from flask import Flask

# إعداد خادم الويب الخفيف لإرضاء منصة Render وابقائها خضراء
app = Flask('')

@app.route('/')
def home():
    return "Bot is alive and running!"

# --- كود البوت ---
TOKEN = os.environ.get("TELEGRAM_TOKEN")

print("Starting Global Binary Market Signals Bot...")

if __name__ == "__main__":
    # تشغيل سيرفر الويب مباشرة على المنفذ المطلوب لضمان عدم إغلاق التطبيق مبكراً
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
