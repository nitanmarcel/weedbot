from telethon import events
from telethon.tl.functions.messages import SetInlineBotResultsRequest
from telethon.tl.types import InputBotInlineMessageText, InputBotInlineResult

from bot_py import bot
from bot_py.apis import gangsta, misc, owo, yoda


@bot.on(events.NewMessage(incoming=True, pattern=r"^\/start"))
async def start(event):
    await event.reply("Hi! I'm the Weed Bot \nI can translate any text in a gangsta text\n Find about my commands with /help")


@bot.on(events.NewMessage(incoming=True, pattern=r"^\/help"))
async def help(event):
    await event.reply(HELP_STRING)


HELP_STRING = """
My commands will work inline too:
/420 -Reply to a message to translate it in gangsta slang
/yodish - Reply to a message to translate it in yoda slang
/owo - Reply to a message to translate it in owo slang
/reverse - Reply to a meesage to reverse it
/tiny - Reply to a meesage to make it tiny
/zalgofy - Reply to a message to zalgofy it
/fancy light - Reply with a fancy text
"""


commands = r"^\/(owo|gangsta|yoda|tiny|reverse|fancy)"


async def get_results(text, as_dict=False):
    func_dict = {"gangsta": await gangsta.gangstafy(text),
                 "owo": owo.owoify(text),
                 "yoda": yoda.yodify(text),
                 "reverse": misc.reverse_text(text),
                 "tiny": misc.tiny_text(text),
                 "fancy": misc.fancy_text(text)}

    if as_dict is True:
        return func_dict
    return func_dict.get(text)


@bot.on(events.NewMessage(incoming=True, pattern=commands))
async def handler(event):
    if event.is_reply:
        text = (await event.get_reply_message()).text
    else:
        if len(event.text.split()) > 1:
            text = event.text.split(None, 1)[1]
        else:
            await event.reply("You have to reply to a message for this to work")
            return

    await event.reply(await get_results(text))


@bot.on(events.InlineQuery)
async def query_handler(event):
    builder = event.builder
    query = event.text
    results = []

    if query:
        for k, v in (await get_results(query, as_dict=True)).items():
            results.append(
                builder.article(
                    str(k),
                    description=str(v),
                    text=str(v)))

        await event.answer(results=results)
    else:
        await event.answer(switch_pm="Text can't be empty", switch_pm_param='_')


if __name__ == "__main__":
    bot.run_until_disconnected()
