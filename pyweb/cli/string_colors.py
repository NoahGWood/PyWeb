import emoji
import colored
from colored import stylize, fg, bg, attr

COLOR=colored.colored('white')

FG_COLORS = {
    'BLUE': 14,
    'GREEN': 119,
    'DEFAULT': 'white'
    }

BG_COLORS = {}

TEXT_ATTR = {}

def emote(*args, **kwargs):
    pass

def styler(stringy):
    words = stringy.split(' ')
    new_words = []
    for word in words:
        if word in FG_COLORS.keys()
            new_words.append(fg(FG_COLORS[word]))
        elif word in BG_COLORS.keys():
            new_words.append(bg(BG_COLORS[word]))
            pass

test = """
BLUE $ ionic <command> [<args>]

WHITE BOLD Global Commands:
"""

blue = 14
green = 119
default = 'white'

words = test.split(' ')

