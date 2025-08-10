import os
import requests
from datetime import datetime
from telegram import Update, Bot
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import pytz

TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=TOKEN)
tehran_tz = pytz.timezone("Asia/Tehran")

def get_gold_price():
    try:
        url = "https://api.metals.live/v1/spot"
        data = requests.get(url, timeout=10).json()
        for metal in data:
            if "gold" in metal:
                return metal["gold"]
    except Exception:
        return None

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "سلام 🌟
من ربات مشاور طلای سومیه‌جان هستم.
"
        "برای دریافت قیمت، دستور /price رو بزن."
    )

async def price(update: Update, context: ContextTypes.DEFAULT_TYPE):
    price = get_gold_price()
    if price is None:
        await update.message.reply_text("❌ خطا در دریافت قیمت")
        return
    signal = "📈 خرید" if price < 2350 else "📉 فروش" if price > 2400 else "⏳ صبر"
    now_tehran = datetime.now(tehran_tz).strftime("%Y-%m-%d %H:%M:%S")
    await update.message.reply_text(
        f"💰 قیمت لحظه‌ای طلا: {price} دلار
"
        f"📊 سیگنال: {signal}
"
        f"🕒 زمان: {now_tehran}"
    )

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("price", price))
    print("✅ Bot is running...")
    app.run_polling()

if name == "main":
    main()
