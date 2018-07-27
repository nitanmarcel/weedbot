from bot_py import dispatcher, update


def reverse_inline(bot, update):
    query = update.inline_query.query
    return query[::-1]


