from . import dispatcher
from config.config import bot, chatbot


@dispatcher.message_handler(lambda call: True)
async def bogomol_reply_private(message):
    if message.text[:6] != '/start':
        response = ''
        for data in chatbot.ask(message.text):
            response = data['message']
        await bot.send_message(chat_id=message.chat.id, text=response)
    else:
        await bot.send_message(chat_id=message.chat.id, text='Я ChatGPT. Вернее богомол. Задай вопрос')
