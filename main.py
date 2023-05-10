from pyrogram.handlers import MessageHandler
from handlers.gptai import bogomol_reply_private
from config.config import app

if __name__ == '__main__':
    app.add_handler(MessageHandler(bogomol_reply_private))       # private message reply by bogomol AI
    app.run(print('Bot started...'))
