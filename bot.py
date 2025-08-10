import os
import logging
from datetime import datetime
import pytz
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import requests

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

TOKEN = os.environ.get("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hello 🌟
"
        "I am the Gold Market Advisor bot.
"
        "Use /price to see the current gold price."
    )

async def price(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        response = requests.get("https://api.metals.live/v1/spot")
        data = response.json()
        gold_price = data[0]["gold"]  # USD per ounce

        # Simple signal logic
        if gold_price > 2000:
            signal = "📈 Buy"
        else:
            signal = "📉 Sell"

        now_tehran = datetime.now(pytz.timezone("Asia/Tehran")).strftime("%Y-%m-%d %H:%M")

        await update.message.reply_text(
            f"Current Gold Price: {gold_price} USD
"
            f"Signal: {signal}
"
            f"Time (Tehran): {now_tehran}"
        )

    except Exception as e:
        logging.error(e)
        await update.message.reply_text("❌ Error fetching gold price.")

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("price", price))

    print("✅ Bot is running...")
    app.run_polling()

if name == "main":
    main()
