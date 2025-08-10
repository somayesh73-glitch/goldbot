from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hello,I am the Gold Market Advisor bot.Use /price to see the current gold price.")
async def price(update: Update, context: ContextTypes.DEFAULT_TYPE):
    gold_price = 1923.45  # Example price
    signal = "Buy"  # Example signal
    now_tehran = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    await update.message.reply_text
    (f"Current Gold Price: {gold_price} USD Signal: {signal}Time (Tehran): {now_tehran}")
if name == "main":
    app = ApplicationBuilder().token("YOUR_BOT_TOKEN_HERE").build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("price", price))
    print("✅ Bot is running...")
    app.run_polling()
