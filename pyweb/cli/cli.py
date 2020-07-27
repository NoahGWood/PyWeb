import configparser
import webbrowser
import os
from cli_strings import cmd_not_found, err_not_proj, CONFIG_HELP, help_switch


def helper(func):
    def help_wrapper(cmd, *args):
        if '--help' in args or '-h' in args:
            if '--help' in str(args[0]) or '-h' in str(args[0]):
                help_switch(args[1])
            else:
                help_switch(args[0])
            exit()
        func(cmd, *args)
    return help_wrapper
    

def project_check(func):
    """Check if we are in project directory"""
    def check_wrapper(cmd, *args):
        sfile = 'settings.conf'
        found = False
        i=0
        while i <= 4:
            if os.path.exists(sfile):
                found = True
                i = 5
            else:
                sfile = '../' + sfile
                i += 1
        if found == True:
            with open(sfile) as f:
                if '#PyWeb' in f.readline():
                    func(*args)
                else:
                    err_not_proj(*args)
        else:
            err_not_proj(*args)
    return check_wrapper

class CLI:
    def __init__(self):
        self.conf_file = 'pyweb.conf'
        self.docs_url = 'http://localhost'
        self.conf = configparser.ConfigParser()

    @helper
    def switch_cmd(self, cmd, *args):
        switcher = {
            'config':self.config,
            'docs':self.docs,
            'start':self.start,
            'serve':self.serve,
            'generate':self.generate,
            'g':self.generate
            }
        return switcher.get(cmd, cmd_not_found)(cmd, *args)
    
    @project_check
    def config(self, cmd, *args):
        try:
            self.conf.read(self.conf_file)
            if args[0] == 'get':
                self.config_get()
            elif args[0] == 'set':
                if len(args) == 4:
                    self.config_set(*args[1:])
                    self.config_get()
                else:
                    print("Sorry, I can't do that yet. Please edit manually")
            else:
                print(CONFIG_HELP)
        except Exception as e:
            print(CONFIG_HELP)

    @project_check
    def config_set(self, cmd, *args):
        self.conf.set(*args)
        with open(self.conf_file, 'w') as f:
            self.conf.write(f)

    @project_check
    def config_get(self, cmd):
        try:
            self.conf.read(self.conf_file)
            for section in self.conf.sections():
                print(section, ":")
                for each in self.conf[section]:
                    print(each + "=" + self.conf[section][each])
        except Exception as e:
            err_not_proj('config')
            
    def docs(self, cmd, *args):
        webbrowser.open_new_tab(self.docs_url)
        pass

    def start(self, cmd, *args):
        """Starts a new project"""
        from logic.start import START
        START()
        pass

    @project_check
    def serve(self, cmd, *args):
        print("Serving!")
        pass

    @project_check
    def generate(self, cmd, *args):
        print("Generating!")
        pass

if __name__ in '__main__':
    cmd = 'config'
    args = 'get'
    x = CLI()
    x.switch_cmd(cmd, *args)
