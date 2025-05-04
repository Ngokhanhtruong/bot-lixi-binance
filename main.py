import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = os.getenv("ADMIN_ID")

if ADMIN_ID:
    ADMIN_ID = int(ADMIN_ID)

ma_da_thu_thap = set()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Chào bạn! Gửi mã lì xì Binance cho mình nhé!")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()
    if "binance.com/vi/red-packet" in text:
        if text in ma_da_thu_thap:
            await update.message.reply_text("Mã này đã được thu thập trước đó rồi.")
        else:
            ma_da_thu_thap.add(text)
            await update.message.reply_text("Đã ghi nhận mã lì xì!")
            if ADMIN_ID:
                await context.bot.send_message(chat_id=ADMIN_ID, text=f"Nhận được mã: {text}")
    else:
        await update.message.reply_text("Bạn vừa gửi không phải là mã lì xì Binance.")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
