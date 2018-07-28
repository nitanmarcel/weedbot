from telegram.ext import Updater, CommandHandler
from bot_py import dispatcher, update
from tinytext import tinytext
from zalgo_text import zalgo


def reverse_reply(bot, update):
    message = update.effective_message
    rep_message = message.reply_to_message
    revese_text = rep_message.text[::-1]
    if not rep_message:
        update.effective_message.reply_text("Reply to a message to make this work")
    else:
        update.message.reply_text(revese_text)

def tiny_reply(bot, update):
    message = update.effective_message
    rep_message = message.reply_to_message
    tiny_text = tinytext(rep_message.text)
    if not rep_message:
        update.effective_message.reply_text("Reply to a message to make this work")
    else:
        update.message.reply_text(tiny_text)
def zalgo_text(bot, update):
    message = update.effective_message
    rep_message = message.reply_to_message
    z = zalgo.zalgo()
    if not rep_message:
        update.effective_message.reply_text("Reply to a message to make this work")
    else:
        update.message.reply_text(z.zalgofy(rep_message.text))

dispatcher.add_handler(CommandHandler("reverse", reverse_reply))
dispatcher.add_handler(CommandHandler("tiny", tiny_reply))
dispatcher.add_handler(CommandHandler("zalgofy", zalgo_text))