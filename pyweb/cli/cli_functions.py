from PyInquirer import prompt

class CLIFunction:
    def __init__(self, help_message=None, args={}, options={}, questions=[], answers=[]):
        self.help_message = help_message
        self.args = args
        self.options = options
        self.questions = []
        self.answers = []

    def _call_option(self, option, cmd=None):
        if 'help' in option:
            self.help(cmd)
        self.options.get(self.args[option], self.help(cmd, option))()
        pass

    def _call_arg(self, arg):
        self.options.get(self.args[arg], print('whoops'))()
        pass

    def prompt(self, pid):
        self.answers.append(prompt(self.questions[pid]))
        pass
    
    def cmd(self, *args):
        for each in args:
            # separate args and options
            if each.startswith('-'):
                self._call_option(each, args[0])
            else:
                self._call_arg(each)
        pass

class Start:
    def __init__(self):
        super()
        self.args = {'name':,'

if __name__ in '__main__':
    x = CLIFunction(args={'start':print})
    print(x.cmd('-start'))
