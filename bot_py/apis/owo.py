

import random
import re


def owoify(text):

    faces = [
        '(・`ω´・)',
        ';;w;;',
        'owo',
        'UwU',
        '>w<',
        '^w^',
        r'\(^o\) (/o^)/',
        '( ^ _ ^)∠☆',
        '(ô_ô)',
        '~:o',
        ';____;',
        '(*^*)',
        '(>_',
        '(♥_♥)',
        '*(^O^)*',
        '((+_+))']
    reply_text = re.sub(r'r|l', "w", text)
    reply_text = re.sub(r'R|L', 'W', reply_text)
    reply_text = re.sub(r'[ＲＬ]', 'Ｗ', reply_text)
    reply_text = re.sub(r'n([aeiouａｅｉｏｕ])', r'ny\1', reply_text)
    reply_text = re.sub(r'ｎ([ａｅｉｏｕ])', r'ｎｙ\1', reply_text)
    reply_text = re.sub(r'N([aeiouAEIOU])', r'Ny\1', reply_text)
    reply_text = re.sub(r'Ｎ([ａｅｉｏｕＡＥＩＯＵ])', r'Ｎｙ\1', reply_text)
    reply_text = re.sub(r'\!+', ' ' + random.choice(faces), reply_text)
    reply_text = re.sub(r'！+', ' ' + random.choice(faces), reply_text)
    reply_text = reply_text.replace("ove", "uv")
    reply_text = reply_text.replace("ｏｖｅ", "ｕｖ")
    reply_text += ' ' + random.choice(faces)
    return reply_text
