import os, fnmatch
import configparser
from zipfile import ZipFile
import wget

config = configparser.ConfigParser()

def replace(directory, find, replace, pattern):
    """This function was shamelessly stolen from David Sulpy's answer:
    https://stackoverflow.com/questions/4205854/python-way-to-recursively-find-and-replace-string-in-text-files

    because I'm lazy and it works.
    """
    for path, dirs, files in os.walk(os.path.abspath(directory)):
        for filename in fnmatch.filter(files, pattern):
            fp = os.path.join(path, filename)
            with open(fp) as f:
                s = f.read()
            s = s.replace(find, replace)
            with open(fp, 'w') as f:
                f.write(s)

def unzip(file):
    with ZipFile(file, 'r') as zipped:
        zipped.extractall()
    
def mvdir(src, dst):
    os.rename(src, dst)

def rm(file):
    os.remove(file)

def get_template(template_url, app_name):
    CWD = os.getcwd()
    file = os.path.join(CWD, app_name)
    wget.download(template_url, file)
    return file


def change_app(member, folder_name, app_name):
    """Changes all folders in 'member' of 'folder_name' to app_name"""
    for root, dirs, files in os.walk(member):
        print(root, dirs, files)
        for each in dirs:
            if folder_name in each:
                mvdir(os.path.join(member, each), os.path.join(member, app_name))

def load_config(root):
    """Loads the settings in the root app directory"""
    config.read_file(open(os.path.join(root, 'settings.conf')))

def gen_settings(root, settings):
    # Step 1: Load configuration
    load_config(root)
    # Step 2 edit configuration
    config['APP'] = {
        'title': settings['main']['app_name'],
        'ignore_bad_pages':settings['main']['ignore_bad']
        }
    config['META'] = {
        'description':settings['meta']['description'],
        'content':settings['meta']['content'],
        'keywords':settings['meta']['keywords'],
        'author':settings['meta']['author'],
        'viewport':'width=device-width,initial-scale=1.0'
        }
    config['NAVBAR'] = {
        'enabled': settings['main']['navbar'],
        'searchbar': settings['navbar']['searchbar']
    }
    config['NAVITEMS'] = {
        'home': '/'
        }
    config['BRAND'] = {
        'enabled': settings['main']['branded'],
        'href': settings['branding']['href'],
        'brand_name': settings['branding']['name'],
        'brand_image': settings['branding']['image']
        }
    config['AUTH'] = {
        'admin_enabled': settings['main']['admin'],
        'user_enabled': settings['main']['user']
    }
    with open(os.path.join(root, 'settings.conf'), 'w') as f:
        config.write(f)

