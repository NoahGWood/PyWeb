import configparser
from cli_strings import cmd_not_found, err_not_proj, CONFIG_HELP
import webbrowser

def helper(func):
    def help_wrapper(*args):
        if '--help' in args or '-h' in args:
            cmd_not_found()
            exit()
        func(*args)
    return help_wrapper
    

class CLI:
    def __init__(self):
        self.conf_file = 'pyweb.conf'
        self.docs_url = 'http://localhost'
        self.conf = configparser.ConfigParser()

    def switch_cmd(self, cmd, *args):
        switcher = {
            'config':self.config,
            'docs':self.docs,
            'start':self.start,
            'serve':self.serve,
            'generate':self.generate,
            'g':self.generate
            }
        return switcher.get(cmd, cmd_not_found)(*args)

    def config(self, *args):
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

    def config_set(self, *args):
        self.conf.set(*args)
        with open(self.conf_file, 'w') as f:
            self.conf.write(f)

    def config_get(self):
        try:
            self.conf.read(self.conf_file)
            for section in self.conf.sections():
                print(section, ":")
                for each in self.conf[section]:
                    print(each + "=" + self.conf[section][each])
        except Exception as e:
            err_not_proj('config')
            
    @helper
    def docs(self, *args):
        webbrowser.open_new_tab(self.docs_url)
        pass

    @helper
    def start(self, *args):
        """Starts a new project"""
        
        pass

    @helper
    def serve(self, *args):
        pass

    @helper
    def generate(self, *args):
        pass

    def __call__(self):
        # Add code before function call
        print('lol1')

#        self.function()

        print('lol3')
        # Add code after function call
        

if __name__ in '__main__':
    cmd = 'config'
    args = 'get'
    x = CLI()
    x.switch_cmd(cmd, *args)
