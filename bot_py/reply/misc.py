from telegram.ext import Updater, CommandHandler
from bot_py import dispatcher, update
from tinytext import tinytext

def reverse_reply(bot, update):
    message = update.effective_message
    rep_message = message.reply_to_message
    revese_text = rep_message.text[::-1]
    if not rep_message:
        update.effective_message.reply_text("Reply to a message to make this work")
    else:
        update.message.reply_text(revese_text)

dispatcher.add_handler(CommandHandler("reverse", reverse_reply))