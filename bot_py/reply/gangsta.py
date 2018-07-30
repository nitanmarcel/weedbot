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
                        replacements = {
                        "about": "'bout",
                        "am": "be",
                        "and": "n",
                        "are": "is",
                        "awesome": "off tha hook",
                        "because": "coz",
                        "being": "bein",
                        "boy": "boi",
                        "car": "ride",
                        "cars": "ridez",
                        "church": "chuch",
                        "cities": "hoodz",
                        "comrades": "posse",
                        "cute": "skanky",
                        "dog": "dogg",
                        "driving": "rollin'",
                        "eed": "ee'",
                        "for": "fo`",
                        "friend": "nigga",
                        "friends": "niggaz",
                        "ged": "ge'",
                        "get": "git",
                        "got": "gots",
                        "great": "bootylicious",
                        "gun": "gat",
                        "guns": "gats",
                        "guy": "homey",
                        "happy": "stoked",
                        "head": "heezee",
                        "house": "hizouse",
                        "ied": "y",
                        "in": "'n",
                        "information": "411",
                        "is": "be",
                        "killed": "iced",
                        "killing": "cappin'",
                        "lil": "shawty",
                        "lil'": "shawty",
                        "little": "shawty",
                        "mad": "buggin'",
                        "man": "dawg",
                        "my": "mah",
                        "nice": "funky ass",
                        "nothing": "nuttin",
                        "ool": "oo'",
                        "peculiar": "perculiar",
                        "people": "thugz",
                        "players": "playas",
                        "please": "pleaze",
                        "police": "po-po",
                        "says": "sez",
                        "se": "ze",
                        "sed": "zed",
                        "ses": "zes",
                        "something": "sum-m sum-m",
                        "super": "snoopa",
                        "take": "takes",
                        "talk": "rap",
                        "television": "televizzle",
                        "the": "tha",
                        "their": "they",
                        "this": "dis",
                        "to": "ta",
                        "town": "ghetto",
                        "with": "wit",
                        "women": "bitchez",
                        "your": "yo'",
                        "yourself": "yoself",
                        "you're": "yoe",
                        "you've": "you",
                        "zed": "ze'",
                    }
                        replacements2 = {
                        "'s": "",
                        "ers": "a",
                        "er": "a",
                        "ings": "in'",
                        "ing": "in'",
                        }
                        longreplacements = {
                        "do you": "d-ya",
                        "or anything": "or nothin' trippin'",
                        "with a": "witta",
                        "you all": "y-aw",
                        "you're all": "y-aw",
                        }


                        text = "You are a motherfucker"
                        pattern = re.compile(r'\b(' + '|'.join(replacements.keys()) + r')\b')
                        result = pattern.sub(lambda x: replacements[x.group()], rep_message.text)
                        pattern2 = re.compile(r'(' + '|'.join(replacements2.keys()) + r')\b')
                        result2 = pattern2.sub(lambda x: replacements2[x.group()], result)
                        pattern3 = re.compile(r'\b(' + '|'.join(longreplacements.keys()) + r')\b')
                        result3 = pattern3.sub(lambda x: longreplacements[x.group()], result2)
                        update.message.reply_text(result3)

dispatcher.add_handler(CommandHandler("420", gizoogle))