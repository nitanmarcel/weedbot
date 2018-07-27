from telegram.ext import Updater
import os

from os.path import dirname, basename, isfile
import glob


TOKEN = os.environ.get('TOKEN', None)
update = Updater(TOKEN)
dispatcher = update.dispatcher

URL = os.environ.get('URL', "")
PORT = int(os.environ.get('PORT', 5000))


