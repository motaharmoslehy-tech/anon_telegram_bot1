import os
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, CommandHandler, filters

# توکن رباتی که از BotFather گرفتی اینجا بذار
TOKEN = "8366650825:AAFU7gRQRKXyeGw8qvwU1l0bOd_HiaETJJU"

# آیدی عددی صاحب ربات (خودت)
OWNER_ID = 6547160508

# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "سلام 👋\n"
        "اینجا می‌تونی ناشناس پیام بدی، فقط کافیه پیام یا عکس یا ویس بفرستی ✅"
    )

# دریافت پیام‌ها از بقیه
async def relay(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    text = update.message.text or ""
    caption = update.message.caption or ""

    # متن
    if text:
        msg = f"📩 پیام ناشناس جدید:\n\n{text}"
        await context.bot.send_message(OWNER_ID, msg)

    # عکس
    elif update.message.photo:
        await context.bot.send_photo(
            OWNER_ID,
            update.message.photo[-1].file_id,
            caption=f"📩 پیام ناشناس:\n{caption}"
        )

    # ویس
    elif update.message.voice:
        await context.bot.send_voice(
            OWNER_ID,
            update.message.voice.file_id,
            caption="📩 ویس ناشناس"
        )

    # استیکر
    elif update.message.sticker:
        await context.bot.send_sticker(
            OWNER_ID,
            update.message.sticker.file_id
        )

    # به فرستنده تأیید بده
    await update.message.reply_text("✅ پیامت ناشناس فرستاده شد.")

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.ALL & ~filters.COMMAND, relay))

    print("Bot is running...")
    app.run_polling()

if name == "main":
    main()
