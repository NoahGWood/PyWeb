#!/usr/bin/python3
import sys
from cli.cli_strings import label, usage, cmd_not_found
from cli.cli import CLI


if len(sys.argv) == 1:
    cmd_not_found()
else:
    args = sys.argv[1:]
    cmd = args[0]
    x = CLI()
    x.switch_cmd(cmd,*args[1:])
    
