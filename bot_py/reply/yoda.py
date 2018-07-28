from telegram.ext import Updater, CommandHandler
from bot_py import dispatcher, update
from suds.client import Client

def yoda_reply(bot, update):
    message = update.effective_message
    rep_message = message.reply_to_message
    if not rep_message:
                update.effective_message.reply_text("For this to work reply a message you have.")
    else:
        yoda_url = 'http://www.yodaspeak.co.uk/webservice/yodatalk.php?wsdl'
        client  = Client(yoda_url)
        yodish = client.service.yodaTalk(rep_message.text)
        update.message.reply_text(yodish)

dispatcher.add_handler(CommandHandler("yodish", yoda_reply))