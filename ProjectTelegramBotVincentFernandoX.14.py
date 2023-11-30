from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, filters, MessageHandler


TOKEN = '6597400300:AAEn9x6lJjNx_EDi32QOeI70hGv2JFSktBs'
USER_BOT = '@Melonsss_bot'

async def  start_command(update: Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Jika Tidak tahu, jangan cari tahu. Tapi klik /help aja")
    
async def  help_command(update: Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Terima kasih telah chat bot by vincent. Gunakan perintah dengan huruf kecil saja\n berikut daftar perintah yang bisa anda gunakan.\n halo\n tentang kamu\n kamu siapa?\n rumah kamu dimana\n sekolah dimana\n minta ignya dong\n wow nama yang bagus\n kamu agama apa?\n jenis kelamin\n tanggal lahir\n siapa yang menciptakanmu?\n Sabbe Satta Bhavantu Sukhitatta\n")

async def  text_massage(update: Update, context:ContextTypes.DEFAULT_TYPE):
    text_diterima : str = update.message.text
    print(f"Pesan diterima : {text_diterima}")

    if 'halo' in text_diterima:
        await update.message.reply_text("halo juga")
    elif 'tentang kamu' in text_diterima:
        await update.message.reply_text("Haii Namaku Bot dibuat oleh vincent. Aku dibuat untuk menemani kalian dan mengenal aku.")
    elif 'kamu siapa?' in text_diterima:
        await update.message.reply_text("aku bot by vincent")
    elif 'rumah kamu dimana?' in text_diterima:
        await update.message.reply_text("hmm sepertinya ini rahasia")
    elif 'sekolah dimana?' in text_diterima:
        await update.message.reply_text("Ignatius Global School")
    elif 'minta ignya dong' in text_diterima:
        await update.message.reply_text("vincent_fernando")
    elif 'wow nama yang bagus' in text_diterima:
        await update.message.reply_text("terima kasih")
    elif 'kamu agama apa?' in text_diterima:
        await update.message.reply_text("Buddha")
    elif 'jenis kelamin' in text_diterima:
        await update.message.reply_text("Laki laki")
    elif 'tanggal lahir' in text_diterima:
        await update.message.reply_text("11 maret 2008")
    elif 'siapa yang menciptakanmu?' in text_diterima:
        await update.message.reply_text("Yang menciptakan saya vincent")
    elif 'diajaran buddha mengatakan' in text_diterima:
        await update.message.reply_text("Sabbe Satta Bhavantu Sukhitatta / Semoga Semua Makhluk Berbahagia")
    else:
        await update.message.reply_text("Maaf, Kami tidak mengerti perintah anda.")

async def photo_message(update: Update, context:ContextTypes.DEFAULT_TYPE):
    return await update.message.reply_text("Gambarnya Indah sekali.")
        
async def  error(update: Update, context:ContextTypes.DEFAULT_TYPE):
    print(f"error... : {context.error}")

if __name__ == '__main__':
    print("Mulai")
    app = Application.builder().token(TOKEN).build()

    #COMMAND :
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))

    #MASSAGE:
    app.add_handler(MessageHandler(filters.TEXT, text_massage))
    app.add_handler(MessageHandler(filters.PHOTO, photo_message))

    #error :
    app.add_error_handler(error)

    #polling :
    app.run_polling(poll_interval=1)