from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
TOKEN = "8887762650:AAHOvAiD2oyv3rSc4ylQcsNInKXyLdULasA"
ALLOWED_USERS = [8224767845, 8561340161, 8331554328, 7328251123, 5460556297, 8179557515]
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Halo! Bot udah jalan 🔥")
async def forward_media(update: Update, context: ContextTypes.DEFAULT_TYPE):
    group_id = -1002811100898
    user_id = update.effective_user.id
    if user_id not in ALLOWED_USERS:
        return
    if update.message.photo:
        photo = update.message.photo[-1].file_id
        caption = update.message.caption or "Foto dari owner BFbot 📸"
        await context.bot.send_photo(chat_id=group_id, photo=photo, caption=caption)
    
    elif update.message.video:
        video = update.message.video.file_id
        caption = update.message.caption or "Video dari owner BFbot 🎬"
        await context.bot.send_video(chat_id=group_id, video=video, caption=caption)
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.PHOTO | filters.VIDEO, forward_media))
async def error_handler(update, context):
    print(f"Error: {context.error}")

app.add_error_handler(error_handler)
print("Bot udah jalan di Acode...")
app.run_polling(allowed_updates=Update.ALL_TYPES, drop_pending_updates=True, poll_interval=2)