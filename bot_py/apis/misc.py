import random
from typing import List

from fancy_text import \
    fancy  # available at https://github.com/nitanmarcel/fancy_text
from tinytext import tinytext
from zalgo_text import zalgo


def reverse_text(text):
    return text[::-1]


def tiny_text(text):
    return tinytext(text)


def zalgo_text(text):
    return zalgo.Zalgo().zalgofy(text)


def fancy_text(text):
    return random.choice([fancy.bold(text), fancy.light(text)])
