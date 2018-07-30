from bot_py import update, dispatcher # import updater and dispatcher

import re
#small port of https://chrome.google.com/webstore/detail/gizoogle-20/fmlbfmomaljkgpojlalmifholhflgfmp?hl=en
def gangsta_inline(bot, update):
    query = update.inline_query.query 
    replacements = {
                        "about": "'bout",
                        "am": "be",
                        "and": "n",
                        "are": "is",
                        "awesome": "off tha hook",
                        "because": "coz",
                        "being": "bein",
                        "boy": "boi",
                        "car": "ride",
                        "cars": "ridez",
                        "church": "chuch",
                        "cities": "hoodz",
                        "comrades": "posse",
                        "cute": "skanky",
                        "dog": "dogg",
                        "driving": "rollin'",
                        "eed": "ee'",
                        "for": "fo`",
                        "friend": "nigga",
                        "friends": "niggaz",
                        "ged": "ge'",
                        "get": "git",
                        "got": "gots",
                        "great": "bootylicious",
                        "gun": "gat",
                        "guns": "gats",
                        "guy": "homey",
                        "happy": "stoked",
                        "head": "heezee",
                        "house": "hizouse",
                        "ied": "y",
                        "in": "'n",
                        "information": "411",
                        "is": "be",
                        "killed": "iced",
                        "killing": "cappin'",
                        "lil": "shawty",
                        "lil'": "shawty",
                        "little": "shawty",
                        "mad": "buggin'",
                        "man": "dawg",
                        "my": "mah",
                        "nice": "funky ass",
                        "nothing": "nuttin",
                        "ool": "oo'",
                        "peculiar": "perculiar",
                        "people": "thugz",
                        "players": "playas",
                        "please": "pleaze",
                        "police": "po-po",
                        "says": "sez",
                        "se": "ze",
                        "sed": "zed",
                        "ses": "zes",
                        "something": "sum-m sum-m",
                        "super": "snoopa",
                        "take": "takes",
                        "talk": "rap",
                        "television": "televizzle",
                        "the": "tha",
                        "their": "they",
                        "this": "dis",
                        "to": "ta",
                        "town": "ghetto",
                        "with": "wit",
                        "women": "bitchez",
                        "your": "yo'",
                        "yourself": "yoself",
                        "you're": "yoe",
                        "you've": "you",
                        "zed": "ze'",
                    }

    replacements2 = {
                        "'s": "",
                        "ers": "a",
                        "er": "a",
                        "ings": "in'",
                        "ing": "in'",
                        }
    longreplacements = {
                        "do you": "d-ya",
                        "or anything": "or nothin' trippin'",
                        "with a": "witta",
                        "you all": "y-aw",
                        "you're all": "y-aw",
                    }

    pattern = re.compile(r'\b(' + '|'.join(replacements.keys()) + r')\b')
    result = pattern.sub(lambda x: replacements[x.group()], query)
    pattern2 = re.compile(r'(' + '|'.join(replacements2.keys()) + r')\b')
    result2 = pattern2.sub(lambda x: replacements2[x.group()], result)
    pattern3 = re.compile(r'\b(' + '|'.join(longreplacements.keys()) + r')\b')
    result3 = pattern3.sub(lambda x: longreplacements[x.group()], result2)
    return result3