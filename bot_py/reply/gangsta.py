import re
import bs4
import random
import requests

from telegram.ext import Updater, CommandHandler
from bot_py import dispatcher, update


def gizoogle(bot, update):

        emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"
                           u"\U0001F300-\U0001F5FF"
                           u"\U0001F680-\U0001F6FF"
                           u"\U0001F1E0-\U0001F1FF"
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           "]+", flags=re.UNICODE)
        message = update.effective_message
        rep_message = message.reply_to_message
        is_url = ("http", "www.", "https")

        if not rep_message:
                update.effective_message.reply_text("Yo gotta reply ta a message/link fo' me to work")
        else:

                if rep_message.text.startswith(is_url):
                        params = {"search": emoji_pattern.sub(r'', rep_message.text)}
                        update.message.reply_text("http://www.gizoogle.net/tranzizzle.php?{}".format(parse.urlencode(params)))
                else:
        	        params = {"translatetext": emoji_pattern.sub(r'', rep_message.text)}
        	        target_url = "http://www.gizoogle.net/textilizer.php"
        	        resp = requests.post(target_url, data=params)
                         # the html returned is in poor form normally.
        	        soup_input = re.sub("/name=translatetext[^>]*>/", 'name="translatetext" >', resp.text)
        	        soup = bs4.BeautifulSoup(soup_input, "lxml")
        	        giz = soup.find_all(text=True)
        	        giz_text = giz[39].strip("\r\n") # Hacky, but consistent.
        	        update.message.reply_text(giz_text)

dispatcher.add_handler(CommandHandler("420", gizoogle))