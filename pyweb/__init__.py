#!/usr/bin/python3
"""
PyWeb

Ionic like CLI for python projects

Usage:

    $ ionic <command> [<args>] [--help] [--verbose] [--quiet] [--no-interactive] [--no-color] [--confirm] [options]

  Global Commands:

    completion ...................... (experimental) Enables tab-completion for
                                      Ionic CLI commands.
    config <subcommand> ............. Manage CLI and project config values
                                      (subcommands: get, set, unset)
    docs ............................ Open the Ionic documentation website
    info ............................ Print project, system, and environment
                                      information
    init ............................ (beta) Initialize existing projects with
                                      Ionic
    login ........................... Log in to Ionic
    logout .......................... Log out of Ionic
    signup .......................... Create an Ionic account
    ssh <subcommand> ................ Commands for configuring SSH keys
                                      (subcommands: add, delete, generate, list,
                                      setup, use)
    start ........................... Create a new project

"""
from pycli import CLI
from start_new import StartNewProject

def docs():
    "Opens the PyWeb Documentation Site"
    print("Opening documentation site")

def start(new_type=None, proj_name=None):
    print("Starting")
    print(new_type, proj_name)
    project = StartNewProject(new_type, proj_name)

if __name__ in '__main__':
    cli=CLI()
    cli.add_function('start', start)
    cli.add_function('docs', docs)
    cli.loop()
