import os
import random
from telegram import Bot
import time
from datetime import datetime

# بيانات البوت والقناة الخاصة بك
TOKEN = "8977461364:AAE3AVwDBmnR1tLDZl0g75oq09NSLMIUNWY"
CHANNEL_ID = "@GlobalMarketSignls"

bot = Bot(token=TOKEN)

# أزواج العملات الحقيقية للسوق العالمي
PAIRS = ["EUR/USD", "GBP/USD", "USD/JPY", "AUD/USD", "EUR/GBP", "USD/CAD"]
DIRECTIONS = ["🟢 صعود (CALL)", "🔴 هبوط (PUT)"]
TIMEFRAMES = ["1 دقيقة", "5 دقائق"]

def generate_signal():
    pair = random.choice(PAIRS)
    direction = random.choice(DIRECTIONS)
    timeframe = random.choice(TIMEFRAMES)
    win_rate = random.randint(88, 98)
    
    message = (
        f"🌍 **إشارة صفقات السوق العالمي (Global Market)** 📈\n\n"
        f"💱 الزوج: `{pair}`\n"
        f"⏱ الإطار الزمني: `{timeframe}`\n"
        f"اتجاه الصفقة: {direction}\n"
        f"🎯 نسبة الدقة المتوقعة: `{win_rate}%`\n\n"
        f"💵 *تمنياتنا لكم بالتوفيق وأرباح ممتازة اليوم!*"
    )
    return message

def send_signal_to_channel():
    # التحقق من أن اليوم ليس سبت أو أحد (عطلة السوق العالمي)
    now = datetime.now()
    if now.weekday() >= 5: # 5 هو السبت، 6 هو الأحد
        print("السوق العالمي مغلق اليوم (عطلة نهاية الأسبوع).")
        return

    try:
        msg = generate_signal()
        bot.send_message(chat_id=CHANNEL_ID, text=msg, parse_mode="Markdown")
        print("تم إرسال إشارة السوق العالمي بنجاح إلى القناة!")
    except Exception as e:
        print(f"حدث خطأ أثناء إرسال الإشارة: {e}")

if __name__ == "__main__":
    print("البوت يعمل الآن وجاهز لإرسال إشارات السوق العالمي...")
    while True:
        send_signal_to_channel()
        # يرسل إشارة كل ساعة (يمكنك تعديل الوقت بالثواني حسب رغبتك)
        time.sleep(3600)
