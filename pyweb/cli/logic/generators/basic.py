"""The basic template generator"""
import configparser
import os
from cli.logic.generators.gen_tools import get_template, unzip, replace, mvdir, rm, change_app, gen_settings

config = configparser.ConfigParser()
CWD = os.getcwd() + '/'


def BasicTemplate(settings):
    # Download file and unzip
    name = settings['main']['app_name']
    member = 'PyWeb-Basic-master'
    zipped = get_template(
        'https://github.com/NoahGWood/PyWeb-Basic/archive/master.zip',
        name+'.zip')
    unzip(zipped)
    # Change file name to APP_NAME
    mvdir(member, name)
    change_app(name, 'basic', name)
    # Cleanup temp folders
    rm(zipped)
    # Step 2 update config with cmd line
    gen_settings(name, settings)
    # Step 4 replace 'basic' in every .py file with APP_NAME
    replace(name, 'basic', name, "*.py")

if __name__ in '__main__':
    BasicTemplate({'main': {
        'app_name': 'test'}
                   })
