#!/usr/bin/python

"""Runs the flask server"""

from dashboard import setup

APP = setup()

if __name__ in '__main__':
    APP.run()
