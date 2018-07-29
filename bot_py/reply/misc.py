from telegram.ext import Updater, CommandHandler
from bot_py import dispatcher, update
from typing import List
import random
from tinytext import tinytext
from zalgo_text import zalgo
from fancy_text import fancy # available at https://github.com/nitanmarcel/fancy_text


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

def fancy_reply(bot, update, args: List[str]):
    message = update.effective_message
    rep_message = message.reply_to_message
    fancy_bold = fancy.bold(rep_message.text)
    fancy_light = fancy.light(rep_message.text)
    if not rep_message:
        update.effective_message.reply_text("Reply to a message to make this work")
    elif 'light' in args:
        update.message.reply_text(fancy_light)
    elif 'bold' in args:
        update.message.reply_text(fancy_bold)
    else:
        update.message.reply_text(random.choice([fancy_light, fancy_bold]))



dispatcher.add_handler(CommandHandler("reverse", reverse_reply))
dispatcher.add_handler(CommandHandler("tiny", tiny_reply))
dispatcher.add_handler(CommandHandler("zalgofy", zalgo_text))
dispatcher.add_handler(CommandHandler('fancy', fancy_reply, pass_args=True))