from config.config import dispatcher
from handlers.gptai import bogomol_reply_private
from aiogram import executor
from background import keep_alive


keep_alive()
if __name__ == '__main__':
    dispatcher.register_message_handler(bogomol_reply_private)
    executor.start_polling(dispatcher=dispatcher, skip_updates=True)
