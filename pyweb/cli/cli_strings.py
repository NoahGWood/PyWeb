import emoji
import colored
from colored import stylize, fg, bg, attr

B = fg(14)
G = fg(119)
GR = fg('light_gray')
D = fg('white')

BOLD=attr('bold')
R=attr('reset')

BGP = bg('purple_4b')
BGB = bg(0)
ESCAPE = '\x1b[0m'
label = emoji.emojize("""
  {}    ____       _       __     __   {}
  {}   / __ \__  _| |     / /__  / /   {}
  {}  / /_/ / / / / | /| / / _ \/ __ \ {}
  {} / ____/ /_/ /| |/ |/ /  __/ /_/ / {}
  {}/_/    \__, / |__/|__/\___/_.___/  {}
  {}      /____/  CLI 0.0.1  :factory:        {}""".format(BGP,ESCAPE,BGP,ESCAPE,BGP,ESCAPE,BGP,ESCAPE,BGP,ESCAPE,BGP,ESCAPE,))

usage = """
{}  Usage:{}

    {} $ pyweb <command> [<args>] [--help] [options] {}

{}  Global Commands:{}

    {}config <subcommand>{} .............{} Manage CLI and project config values
                                      (subcommands: get, set, unset)
    {}docs{} ............................{} Open the PyWeb documentation website

    {}start{} ...........................{} Create a new project

{}  Project Commands:{}
    {}serve{} ...........................{} Start a local dev server for app
                                      dev/testing (alias: s)
    {}generate{} ........................{} Automatically create framework features
                                      (alias: g)

""".format(BOLD,R,B,D,BOLD,R,B,GR,D,B,GR,D,B,GR,D,BOLD,R,B,GR,D,B,GR,D)


CONFIG_HELP = """
{}{}  pyweb config{} - Manage CLI and project config values{}

    These commands are used to programmatically read, write, and delete CLI and
    project config values.
    
    By default, these commands use your project's {}./ionic.config.json{} file.
    
    To use these commands for the global CLI config file ({}~/.ionic/config.json{}),
    use the {}--global flag.{}

{}  Usage:{}

    $ {}pyweb config <command> [<args>] [--help] [--confirm] [options]{}

{}  Global Commands:{}

    {}get{} .............................{} Print config values
    {}set{} .............................{} Set config values
    {}unset{} ...........................{} Delete config values
""".format(BOLD,B,D,R,BOLD,R,BOLD,R,B,D,BOLD,
    R,B,D,BOLD,R,B,GR,D,B,GR,D,B,GR,D)

INFO_HELP = """
{}  PyWeb{}

    PyWeb CLI                     :{} 0.0.1 (/usr/local/lib/node_modules/ionic){}
""".format(BOLD,R,GR,D)

START_HELP = """

    {}{}pyweb start{} - Create a new project{}

    This command creates a working Flask app in a new virtualenv and installs
    dependencies for you.

    Running {}pyweb start{} without any arguments will prompt you for
    information about your new project.

    The first argument is your app's {}name{}. Don't worry, you can always
    change this later.

    The second argument is the {}template{} used to generate your app. You can
    list all templates with the {}--list{} option.

    {}Usage:{}
        {}${} pyweb start <name> <template> [options]{}

    {}Inputs:{}
        {}name{} ............................{} The name of your new project (e.g {}myApp{},
                                          {}"My App"{})
        {}template{} ........................{} The starter template to use (e.g. {}blank{}, {}
                                          tabs{}; use {}--list{} to see all)
    {}Options:{}
        {}--list{}, {}-l{} .........................{} List available starter templates

    {}Examples:{}
        {}${} pyweb start
        {}${} pyweb start --list
        {}${} pyweb start myApp
        {}${} pyweb start myApp blank{}
""".format(BOLD,B,D,R,B,D,B,D,B,D,B,D,BOLD,R,GR,B,D,BOLD,R,
           B,GR,D,B,D,B,D,B,GR,D,B,D,B,D,B,D,BOLD,R,B,D,B,GR,
           D,BOLD,R,GR,B,GR,B,GR,B,GR,B,GR,B,D)

def err_not_proj(*args):
    print("Sorry {}{}{}{}{} needs to be run in a project directory.".format(
        BOLD, B, args[0], B, R))

def cmd_not_found(cmd=None,*args):
    if cmd:
        print(" {}{}ERROR: Unable to find command: {}{}{} {}\n".format(
            BOLD,fg('red'),B,cmd,D,R))
    print(label)
    print(usage)

def help_switch(cmd):
    switcher = {
        'config':None,
        'docs': None,
        'start': START_HELP,
        'serve': None,
        'generate': None,
        'g': None
        }
    x = switcher.get(cmd)
    if x:
        print(x)
    else:
        cmd_not_found(cmd)
