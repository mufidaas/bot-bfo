from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
TOKEN = "8918494180:AAGrpmidPz4GgN9R9d6_IyTcm_UupFIBxEs"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome = "Selamat datang di administrasi BF Organizer\nSilakan pilih jenis event Anda, jika bot tidak merespon segera hubungi: @iHrgoN"
    await update.message.reply_text(welcome)
    rules = """𝐁𝐀𝐄𝐊'𝐒 𝐅𝐀𝐌𝐈𝐋𝐘 𝐎𝐑𝐆𝐀𝐍𝐈𝐙𝐄𝐑
ㅤㅤㅤㅤㅤ── ❲ 𝐁𝐅𝐎 ❳ ── ㅤ              
ㅤ
╭─────────────────────╮ 
ㅤㅤ𝐀𝐓𝐓𝐄𝐍𝐓𝐈𝐎𝐍 • 𝐏𝐋𝐄𝐀𝐒𝐄 𝐑𝐄𝐀𝐃 ╰─────────────────────╯

With love and dedication,
𝐁𝐚𝐞𝐤'𝐬 𝐅𝐚𝐦𝐢𝐥𝐲 𝐎𝐫𝐠𝐚𝐧𝐢𝐳𝐞𝐫 is ready to accompany your precious and unforgettable moments. ✨
Before making a reservation, please read and comply with all regulations below.

──────────── ༺𓆩⚝𓆪༻ ────────────

⌕ 𝐁𝐅𝐎 𝐑𝐔𝐋𝐄𝐒

1. Sebelum registrasi, calon client wajib subscribe channel BFO dan dilarang unsubscribe meskipun acara sudah selesai.

2. Sambutan (speech) maksimal 5 orang. (kalau ingin lebih harus konfirmasi pada staff dan beri alasan)

3. Dilarang meminta tema yang tidak sesuai dengan konsep wedding atau terlalu berlebihan. (selayaknya manusia aja)

4. Registrasi wajib dilakukan minimal 2 minggu sebelum hari pelaksanaan event. (untuk birthday party bisa di lakukan 1 minggu sebelum)

5 .Setelah registrasi, wajib share bukti registrasi ke channel atau group yang telah ditentukan.

6. Client wajib memberikan detail konsep acara dengan jelas agar proses persiapan berjalan lancar.

7. Perubahan konsep atau susunan acara hanya dapat dilakukan maksimal H-7 sebelum event berlangsung.

8. Dilarang membatalkan acara secara sepihak tanpa konfirmasi kepada pihak BFO.

9. Seluruh peserta dan tamu undangan wajib menjaga kenyamanan serta ketertiban selama acara berlangsung.


──────────── ༺𓆩⚝𓆪༻ ────────────

❕ Dengan melakukan registrasi, client dianggap telah membaca, memahami, dan menyetujui seluruh rules yang berlaku di BFO.

Thank you for your trust and cooperation.
────────────༺𓆩⚝𓆪༻ ────────────

𝐌𝐀𝐊𝐄 𝐘𝐎𝐔𝐑 𝐃𝐑𝐄𝐀𝐌 𝐖𝐄𝐃𝐃𝐈𝐍𝐆 𝐂𝐎𝐌𝐄 𝐓𝐑𝐔𝐄

🤍 @BAEKSFAMILYORGANIZER
🤍 @BFOCHANNEL 
🤍 @BFOEVENT"""
    await update.message.reply_text(rules, parse_mode='HTML')
    keyboard = [
        [KeyboardButton("Wedding"), KeyboardButton("Birthday Party")],
        [KeyboardButton("Anniversary"), KeyboardButton("Engagement")]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=False)
    await update.message.reply_text(
    "Silakan pilih jenis event Anda:",
    reply_markup=reply_markup) 
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    
    if text == "Wedding":
        form = """༺𓆩⚝𓆪༻𝐖𝐄𝐃𝐈𝐍𝐆 𝐑𝐄𝐆𝐈𝐒𝐓𝐑𝐀𝐓𝐈𝐎𝐍༺𓆩⚝𓆪༻

▌CLIENT DATA
⟡ Groom 
• Username :
• Chara/Muse :

⟡ Bride 
• Username :
 • Chara/Muse :

━━━━━━━━━━━━━━━━━━━━

▌GUARDIAN
⟡ Groom's Guardian 
• Username :
⟡ Bride's Guardian 
• Username :

━━━━━━━━━━━━━━━━━━━━

▌EVENT DETAILS
• Date : 
• Time : 
• Theme : 
• Dresscode : 
• Officiant : 

━━━━━━━━━━━━━━━━━━━━
▌GREETING LIST

Groom Side : 
1. 
2. 
3. 
4. 
5.

Bride Side : 
1. 
2. 
3. 
4. 
5.

━━━━━━━━━━━━━━━━━━━━
▌DOWRY
• Giver :

━━━━━━━━━━━━━━━━━━━━
▌DOWRY HANDOVER
• Receiver :

━━━━━━━━━━━━━━━━━━━━
▌ADDITIONAL REQUEST :

━━━━━━━━━━━━━━━━━━━━
༺ 𝐁𝐀𝐄𝐊'𝐒 𝐅𝐀𝐌𝐈𝐋𝐘 𝐎𝐑𝐆𝐀𝐍𝐈𝐙𝐄𝐑 ༻

"An elegant beginning for a timeless story."
"""
        await update.message.reply_text(form)
    
    elif text == "Birthday Party":
        form = """༺𓆩⚝𓆪༻𝐁𝐈𝐑𝐓𝐇𝐃𝐀𝐘 𝐑𝐄𝐆𝐈𝐒𝐓𝐑𝐀𝐓𝐈𝐎𝐍༺𓆩⚝𓆪༻

▌CLIENT DATA

• Username :
• Chara/Muse :


━━━━━━━━━━━━━━━━━━━━ 

▌EVENT DETAILS
• Date : 
• Time : 
• Theme : 
• Dresscode : 
• Officiant : 

━━━━━━━━━━━━━━━━━━━━
▌GREETING LIST

Birthday Party : 
1. 
2. 
3. 
4. 
5.

━━━━━━━━━━━━━━━━━━━━

▌ADDITIONAL REQUEST :

━━━━━━━━━━━━━━━━━━━━
༺ 𝐁𝐀𝐄𝐊'𝐒 𝐅𝐀𝐌𝐈𝐋𝐘 𝐎𝐑𝐆𝐀𝐍𝐈𝐙𝐄𝐑 ༻

"Hope your birthday is as amazing as you are."
"""
        await update.message.reply_text(form)
    
    elif text == "Anniversary":
        form = """༺𝐀𝐍𝐈𝐕𝐄𝐑𝐒𝐀𝐑𝐘 𝐑𝐄𝐆𝐈𝐒𝐓𝐑𝐀𝐓𝐈𝐎𝐍༻

▌CLIENT DATA

⟡ Man
• Username : 
• Chara/Muse :

⟡ Woman
• Username : 
• Chara/Muse :

━━━━━━━━━━━━━━━━━━━━
▌EVENT DETAILS

• Date : 
• Time : 
• Theme : 
• Dresscode : 
• Year/Month :

━━━━━━━━━━━━━━━━━━━━
▌GREETING LIST

Man Side : 
1. 
2. 
3. 
4. 
5.

Woman Side : 
1.
2. 
3. 
4. 
5.

━━━━━━━━━━━━━━━━━━━━
▌ADDITIONAL REQUEST :


━━━━━━━━━━━━━━━━━━━━
༺ 𝐁𝐀𝐄𝐊'𝐒 𝐅𝐀𝐌𝐈𝐋𝐘 𝐎𝐑𝐆𝐀𝐍𝐈𝐙𝐄𝐑 ༻

"Here's to love, laughter, and forever."
"""
        await update.message.reply_text(form)
    
    elif text == "Engagement":
        form = """╔═════════╗
༺𝐄𝐍𝐆𝐀𝐆𝐄𝐌𝐄𝐍𝐓 𝐑𝐄𝐆𝐈𝐒𝐓𝐑𝐀𝐓𝐈𝐎𝐍༻
╚═════════╝

▌CLIENT DATA

⟡ Future Groom 
• Username : 
• Chara/Muse :

⟡ Future Bride 
• Username : 
• Chara/Muse :

━━━━━━━━━━━━━━━━━━━━
▌GUARDIAN

⟡ Groom's Guardian 
• Username :

⟡ Bride's Guardian 
• Username :

━━━━━━━━━━━━━━━━━━━━
▌EVENT DETAILS

• Date : 
• Time : 
• Theme : 
• Dresscode : 
• Host/MC :

━━━━━━━━━━━━━━━━━━━━
▌GREETING LIST

Groom Side : 
1. 
2. 
3. 
4. 
5.

Bride Side : 
1.
2. 
3. 
4. 
5.

━━━━━━━━━━━━━━━━━━━━
▌ENGAGEMENT TOKEN

• Giver :

━━━━━━━━━━━━━━━━━━━━
▌TOKEN HANDOVER

• Receiver :

━━━━━━━━━━━━━━━━━━━━
▌ADDITIONAL REQUEST :

━━━━━━━━━━━━━━━━━━━━
▌EVENT ARRANGEMENT

1. Opening by MC
2. Welcome Spee
3. Family Introduction
4. Expression of Intent & Blessing
5. Engagement Token / Ring Exchange
6. Future Couple Speech
7. Documentation Session
8. Closing

━━━━━━━━━━━━━━━━━━━━
༺ 𝐁𝐀𝐄𝐊'𝐒 𝐅𝐀𝐌𝐈𝐋𝐘 𝐎𝐑𝐆𝐀𝐍𝐈𝐙𝐄𝐑 ༻

"Two hearts, one promise, and a beautiful future ahead."
"""
        await update.message.reply_text(form)
    
    else:
       GROUP_ID = -1003967512814 
    
       user = update.effective_user.username or update.effective_user.first_name
       teks_ke_grup = f"📩 FORM BARU MASUK!\nDari: @{user}\nID: {update.effective_user.id}\n\n{update.message.text}"
       await context.bot.send_message(chat_id=GROUP_ID, text=teks_ke_grup)
       await update.message.reply_text("✅ Succes! data anda kami terima dan akan segera kami proses, kabar selengkapnya hubungi bagian administrasi kami saja > @Nauvioletta")

def main():
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start, filters=filters.ChatType.PRIVATE))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND & filters.ChatType.PRIVATE, handle_message))
    
    print("Bot sedang berjalan...")
    application.run_polling()

if __name__ == '__main__':
    main()