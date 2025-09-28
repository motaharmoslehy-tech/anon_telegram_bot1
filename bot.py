import os
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, CommandHandler, filters

TOKEN = "8366650825:AAFU7gRQRKXyeGw8qvwU1l0bOd_HiaETJJU"
OWNER_ID = 6547160508

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "سلام 👋\n"
        "اینجا می‌تونی ناشناس پیام بدی، فقط کافیه پیام یا عکس یا ویس بفرستی ✅"
    )

async def relay(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text or ""
    caption = update.message.caption or ""

    if text:
        await context.bot.send_message(OWNER_ID, f"📩 پیام ناشناس:\n\n{text}")

    elif update.message.photo:
        await context.bot.send_photo(
            OWNER_ID,
            update.message.photo[-1].file_id,
            caption=f"📩 پیام ناشناس:\n{caption}"
        )

    elif update.message.voice:
        await context.bot.send_voice(OWNER_ID, update.message.voice.file_id, caption="📩 ویس ناشناس")

    elif update.message.sticker:
        await context.bot.send_sticker(OWNER_ID, update.message.sticker.file_id)

    await update.message.reply_text("✅ پیامت ناشناس فرستاده شد.")

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.ALL & ~filters.COMMAND, relay))
    print("Bot is running...")
    app.run_polling()

if name == "main":
    main()
