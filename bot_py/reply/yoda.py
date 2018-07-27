from telegram.ext import Updater, CommandHandler
from bot_py import dispatcher, update

import requests

def yoda_reply(bot, update):
    message = update.effective_message
    rep_message = message.reply_to_message
    if not rep_message:
                update.effective_message.reply_text("For this to work reply a message you have.")
    else:
        yoda_params = {"text": rep_message.text}
        yoda_url = 'http://yoda-api.appspot.com/api/v1/yodish'
        yoda_re = requests.get(yoda_url, params=yoda_params)
        yoda_text = yoda_re.json()
        yodish = yoda_text.get("yodish", None)
        update.message.reply_text(yodish)

dispatcher.add_handler(CommandHandler("yodish", yoda_reply))