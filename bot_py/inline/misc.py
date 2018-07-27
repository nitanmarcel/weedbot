from bot_py import dispatcher, update
from tinytext import tinytext

def reverse_inline(bot, update):
    query = update.inline_query.query
    return query[::-1]


def tiny_inline(bot, update):
    query = update.inline_query.query
    return tinytext(query)


