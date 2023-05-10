from pyrogram import Client
from revChatGPT.V3 import Chatbot

TELEGRAM_API_ID = '25384280'
TELEGRAM_API_HASH = '5a879a2dac030fb406f58810174ebcf2'

app = Client(api_hash=TELEGRAM_API_HASH, api_id=TELEGRAM_API_ID, name='my_account')

OPENAI_TOKEN = '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'
chatbot = Chatbot(api_key=OPENAI_TOKEN)
