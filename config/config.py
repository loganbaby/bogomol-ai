from pyrogram import Client
from revChatGPT.V1 import Chatbot

TELEGRAM_API_ID = '25384280'
TELEGRAM_API_HASH = '5a879a2dac030fb406f58810174ebcf2'

app = Client(api_hash=TELEGRAM_API_HASH, api_id=TELEGRAM_API_ID, name='my_account')

ACCESS_TOKEN = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1UaEVOVUpHTkVNMVFURTRNMEZCTWpkQ05UZzVNRFUxUlRVd1FVSkRNRU13UmtGRVFrRXpSZyJ9.eyJodHRwczovL2FwaS5vcGVuYWkuY29tL3Byb2ZpbGUiOnsiZW1haWwiOiJkbWl0cnlrb3Rvdjg5QHlhbmRleC5ydSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlfSwiaHR0cHM6Ly9hcGkub3BlbmFpLmNvbS9hdXRoIjp7InVzZXJfaWQiOiJ1c2VyLTlRcG9JcUNPNHNGd1NkRHNTMU43TGpRZCJ9LCJpc3MiOiJodHRwczovL2F1dGgwLm9wZW5haS5jb20vIiwic3ViIjoiYXV0aDB8NjQ1NTVjZmU1NTIwZjk3YjAwZjNjNTllIiwiYXVkIjpbImh0dHBzOi8vYXBpLm9wZW5haS5jb20vdjEiLCJodHRwczovL29wZW5haS5vcGVuYWkuYXV0aDBhcHAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTY4MzMxNjgxNywiZXhwIjoxNjg0NTI2NDE3LCJhenAiOiJUZEpJY2JlMTZXb1RIdE45NW55eXdoNUU0eU9vNkl0RyIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwgbW9kZWwucmVhZCBtb2RlbC5yZXF1ZXN0IG9yZ2FuaXphdGlvbi5yZWFkIG9mZmxpbmVfYWNjZXNzIn0.i7xmw2ArEZ46UqNQcGyPGzl-FjnaNCHnWwueZX3TDcmBy8lk7TnHM3cVgLQKtbzFSg4GYOjI7Ia6_h7zvHSL1hlEha7ihsoWNk2iW57g7N8cwfZQp6wBF7jX-mtMUBSWsgrMbS4oDioTwXmShiYTl7APTocoOFk9KAl3ju_YNfwl-mO_L8EvdnuPPkYoJjtQTVruUzY5U76bddZdt4_Te836vr--UvxzbbQ7N3nBqCoSSycTfADeoV1b0pRwpT_27FML7u2Qe3Kvyr8leVD3-qFVhlh8hyWbTFxhz49k40N2I0Dx3oOOB-9s9PHzRn9CmHhXNLBxULpdlXUow685Ig'
chatbot = Chatbot(config={
    "access_token": ACCESS_TOKEN,
    "model": "gpt-4"
})
