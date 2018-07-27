
# imports needed for the inline bot to work
from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import Updater, InlineQueryHandler

from bot_py import update, dispatcher
from bot_py.inline.gangsta import gangsta_inline # Import the gangsta inline command
from bot_py.inline.yoda import yoda_inline # Import the yoda inline command
from bot_py.inline.owo import owo_inline
from uuid import uuid4

def inline_query(bot, update):
    
    gangsta = gangsta_inline(bot, update) # calling the gangsta inline command
    yoda = yoda_inline(bot, update) ## calling the yoda inline command
    owo = owo_inline(bot, update)

# Repeat "InlineQueryResultArticle( ))"" for every inline command, add a dot after "))" if the pharanteses are before the ending bracket
    results = [
        InlineQueryResultArticle(
            id=uuid4(),
            title="Gangsta",
            description=gangsta,
            input_message_content=InputTextMessageContent(
                gangsta)),
        InlineQueryResultArticle(
            id=uuid4(),
            title="Yoda",
            description=yoda,
            input_message_content=InputTextMessageContent(
                yoda)),
        InlineQueryResultArticle(
            id=uuid4(),
            title="OwO",
            description=owo,
            input_message_content=InputTextMessageContent(
                owo))]
                
    update.inline_query.answer(results)


dispatcher.add_handler(InlineQueryHandler(inline_query))
