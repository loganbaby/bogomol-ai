from config.config import app, chatbot
from revChatGPT.typings import Error as ChatGPTError
from contextlib import suppress
from pyrogram import filters, types
from pyrogram.errors.exceptions import MessageIdInvalid
import pyrogram.enums.parse_mode as parse_mode
import asyncio


async def delete_message(message: types.Message, sleep_time: int = 0):
    await asyncio.sleep(sleep_time)
    with suppress(MessageIdInvalid):
        await message.delete()


@app.on_message(filters.text & filters.outgoing)
async def bogomol_reply_private(_, message):
    try:
        response = ''
        for data in chatbot.ask(message.text):
            response = data['message']
        await app.send_message(chat_id=message.chat.id, text=response)
    except ChatGPTError:
        msg = await app.send_message(chat_id=message.chat.id, text='❎ <b><i>Запрос не выполнен</i></b>\n\nПока что мой <u>светлый</u> разум рассчитан на поток пользователей, поэтому из-за <i><b>неправильной организации</b></i> очереди запросов - 5 запросов доступны за 10 секунд пользования ботом.\n\nПросто <u>подождите немного</u> и <b>попробуйте заново</b> ✅', parse_mode=parse_mode.ParseMode.HTML)
        asyncio.create_task(delete_message(msg, 10))
