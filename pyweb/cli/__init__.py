#!/usr/bin/python3

import os
import sys
from PyInquirer import style_from_dict, Token, prompt, Separator
from cli_strings import *
if __name__ in '__main__':
    if len(sys.argv) <= 1:
        print(label)
        print(CONFIG_HELP)
        print(INFO_HELP)
        print(START_HELP)

    else:
        # cli
        pass
