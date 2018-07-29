import re
from bot_py import update, dispatcher
from telegram.ext import Updater, CommandHandler
from bot_py import dispatcher, update

def fancy_reply(bot, update):
    fancy_dict= { 'a' : '\uD835\uDD86'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                  'b' : '\uD835\uDD87'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                  'c' : '\uD835\uDD88'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                  'd' : '\uD835\uDD89'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                  'e' : '\uD835\uDD8A'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                  'f' : '\uD835\uDD8B'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                  'g' : '\uD835\uDD8C'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                  'h' : '\uD835\uDD8D'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                  'i' : '\uD835\uDD8E'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                  'j' : '\uD835\uDD8F'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                  'k' : '\uD835\uDD90'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                  'l' : '\uD835\uDD91'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                  'm' : '\uD835\uDD92'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                  'n' : '\uD835\uDD93'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                  'o' : '\uD835\uDD94'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                  'p' : '\uD835\uDD95'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                  'q' : '\uD835\uDD96'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                  'r' : '\uD835\uDD97'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                  's' : '\uD835\uDD98'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                  't' : '\uD835\uDD99'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                  'u' : '\uD835\uDD9A'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                  'v' : '\uD835\uDD9B'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                  'w' : '\uD835\uDD9C'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                  'x' : '\uD835\uDD9D'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                  'y' : '\uD835\uDD9E'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                  'z' : '\uD835\uDD9F'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                  'A' : '\uD835\uDD6C'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                  'B' : '\uD835\uDD6D'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                  'C' : '\uD835\uDD6E'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                  'D' : '\uD835\uDD6F'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                  'E' : '\uD835\uDD70'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                  'F' : '\uD835\uDD71'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                  'G' : '\uD835\uDD72'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                  'H' : '\uD835\uDD73'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                  'I' : '\uD835\uDD74'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                  'J' : '\uD835\uDD75'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                  'K' : '\uD835\uDD76'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                  'L' : '\uD835\uDD77'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                  'M' : '\uD835\uDD78'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                  'N' : '\uD835\uDD79'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                  'O' : '\uD835\uDD7A'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                  'P' : '\uD835\uDD7B'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                  'Q' : '\uD835\uDD7C'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                  'R' : '\uD835\uDD7D'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                  'S' : '\uD835\uDD7E'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                  'T' : '\uD835\uDD7F'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                  'U' : '\uD835\uDD80'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                  'V' : '\uD835\uDD81'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                  'W' : '\uD835\uDD82'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                  'X' : '\uD835\uDD83'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                  'Y' : '\uD835\uDD84'.encode('utf-16', 'surrogatepass').decode('utf-16'),
                  'Z' : '\uD835\uDD85'.encode('utf-16', 'surrogatepass').decode('utf-16')
                  }
    message = update.effective_message
    rep_message = message.reply_to_message
    if not rep_message:
                update.effective_message.reply_text("You have to reply to a message for this to work")
    else:
        pattern = re.compile(r'(' + '|'.join(fancy_dict.keys()) + r')')
        result = pattern.sub(lambda x: fancy_dict[x.group()], rep_message.text)
        update.effective_message.reply_text(result)

dispatcher.add_handler(CommandHandler("fancy", fancy_reply))