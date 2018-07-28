from bot_py import update, dispatcher
from suds.client import Client

def yoda_inline(bot,update):
    query = update.inline_query.query

    yoda_url = 'http://www.yodaspeak.co.uk/webservice/yodatalk.php?wsdl'
    client  = Client(yoda_url)
    yodish = client.service.yodaTalk(query)
    return(yodish)