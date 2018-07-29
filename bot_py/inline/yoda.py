from bot_py import update, dispatcher
from suds.client import Client
import re

def yoda_inline(bot,update):
    query = update.inline_query.query

    replace_dict = {
    "aren't" : "are not",
    "can't" : "cannot",
    "couldn't" : "could not",
    "didn't" : "did not",
    "doesn't" : "does not",
    "don't" : "do not",
    "hadn't" : "had not",
    "hasn't" : "has not",
    "haven't" : "have not",
    "he'll" : "he will",
    "he's" : "he is",
    "I'd" : "I had",
    "I'll" : "I will",
    "I'm" : "I am",
    "I've" : "I have",
    "isn't" : "is not",
    "let's" : "let us",
    "mightn't" : "might not",
    "mustn't" : "must not",
    "shan't" : "shall not",
    "she'd" : "she would",
    "she'll" : "she will",
    "she's" : "she is",
    "shouldn't" : "should not",
    "that's" : "that is",
    "there's" : "'there is",
    "they'd" : "they had",
    "they'll" : "they will",
    "they're" : "they are",
    "they've" : "they have",
    "we'd" : "we would",
    "we're" : "we are",
    "we've" : "we have",
    "weren't" : "were not",
    "what'll" : "what will",
    "what're" : "what are",
    "what's" : "what is",
    "what've" : "what have",
    "where's" : "where is",
    "who's" : "who would",
    "who'll" : "who will",
    "who're" : "who are",
    "who's" : "who is",
    "who've" : "who have",
    "won't" : "will not",
    "wouldn't" : "would not",
    "you'd" :  "you would",
    "you'll" : "you will",
    "you're" : "you are",
    "you've" : "you have", 
}


    pattern = re.compile(r'\b(' + '|'.join(replace_dict.keys()) + r')\b')
    result = pattern.sub(lambda x: replace_dict[x.group()], query)
    yoda_url = 'http://www.yodaspeak.co.uk/webservice/yodatalk.php?wsdl'
    client  = Client(yoda_url)
    yodish = client.service.yodaTalk(result)
    return(yodish)