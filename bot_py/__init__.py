import os
from telethon import TelegramClient
import logging

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO)


try:
    API_ID = os.environ["APP_ID"]
    API_HASH = os.environ["APP_HASH"]
    TOKEN = os.environ["TOKEN"]
except KeyError as e:
    quit(e.args[0] + ' missing from environment variables')

bot = TelegramClient("weedbot", API_ID, API_HASH)

bot.start(bot_token=TOKEN)
