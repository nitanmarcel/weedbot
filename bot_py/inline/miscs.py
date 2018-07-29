from bot_py import dispatcher, update
from tinytext import tinytext
from zalgo_text import zalgo
from fancy_text import fancy

def reverse_inline(bot, update):
    query = update.inline_query.query
    return query[::-1]


def tiny_inline(bot, update):
    query = update.inline_query.query
    return tinytext(query)

def zalgo_inline(bot, update):
    query = update.inline_query.query
    z = zalgo.zalgo()
    return z.zalgofy(query)

def fancy_bold_inline(bot, update):
    query = update.inline_query.query
    return fancy.bold(query)

def fancy_light_inline(bot, update):
    query = update.inline_query.query
    return fancy.light(query)


