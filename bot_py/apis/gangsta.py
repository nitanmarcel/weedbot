import re
from urllib import parse
import bs4
import aiohttp


async def gangstafy(text):
    if text.startswith(url_start):
        params = {"search": emoji_pattern.sub(r'', text)}
        return f"http://www.gizoogle.net/tranzizzle.php?{parse.urlencode(params)}"

    async with aiohttp.ClientSession() as session:
        async with session.post("http://www.gizoogle.net/textilizer.php", data={"translatetext": emoji_pattern.sub(r'', text)}) as resp:
            re_resp = re.sub("/name=translatetext[^>]*>/", 'name="translatetext" >', await resp.text())
            soup = bs4.BeautifulSoup(re_resp, "lxml")
            giz = soup.find_all(text=True)
            return giz[39].strip("\r\n")


url_start = ("http", "www.", "https")
emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"
                           u"\U0001F300-\U0001F5FF"
                           u"\U0001F680-\U0001F6FF"
                           u"\U0001F1E0-\U0001F1FF"
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251""]+", flags=re.UNICODE)
