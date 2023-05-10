from config.config import app, chatbot
from revChatGPT.typings import APIConnectionError
from pyrogram import filters
import pyrogram.enums.parse_mode as parse_mode


@app.on_message(filters.me)
async def bogomol_reply_private(_, message):
    answer = ''

    try:
        for data in chatbot.ask_stream(message.text):
            answer += data
        await app.send_message(chat_id=message.chat.id, text=answer)
    except APIConnectionError:
        await app.send_message(chat_id=message.chat.id, text='❎ <b><i>Запрос не выполнен<i><b>\n\nПока что мой <u>светлый</u> разум рассчитан на поток пользователей, поэтому из-за </i><b>неправильной организации</b></i> очереди запросов - 3 запроса доступны за 1 минуту пользования ботом.\n\nПросто <u>подождите немного</u> и <b>попробуйте заново</b> ✅', parse_mode=parse_mode.ParseMode.HTML)
