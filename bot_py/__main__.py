from bot_py import update, dispatcher, TOKEN, URL, PORT
from telegram.ext import Updater, InlineQueryHandler, CommandHandler
from bot_py.reply import *
import logging
import sys

from bot_py.inline.base import inline_query

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
level=logging.INFO)

def start(bot, update):
    update.message.reply_text("Hi! I'm the Weed Bot \nI can translate any text in a gangsta text\n Find about my commands with /help")


def help(bot, update):

    HELP_STRING = """

    My commands works inline too:
    /420 - Use this to translate sentences in gangsta slang
    /yodish - Use this to translate sentences in yoda slang
    """
    update.message.reply_text(HELP_STRING)

def main():

    start_handler = CommandHandler("start", start)
    help_handler = CommandHandler("help", help)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(help_handler)

    update.start_webhook(listen="0.0.0.0",
                              port=PORT,
                              url_path=TOKEN)

    update.bot.set_webhook(url=URL + TOKEN)


if __name__ == '__main__':
    main()