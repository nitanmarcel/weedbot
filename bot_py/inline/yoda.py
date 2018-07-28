from bot_py import update, dispatcher

import requests

def yoda_inline(bot,update):
    query = update.inline_query.query

    yoda_params = {"text": query}
    yoda_url = 'http://yoda-api.appspot.com/api/v1/yodish'
    try:
        yoda_re = requests.get(yoda_url, params=yoda_params)
        yoda_text = yoda_re.json()
        yodish = yoda_text.get("yodish", None)
    except ValueError:
        yodish = 'Text too long to be translated'
    return yodish