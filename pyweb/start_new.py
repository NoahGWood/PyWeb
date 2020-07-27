

class StartNewProject:
    def __init__(self, *args):
        """Starts a new project"""
        self.available = self.get_available()
        self.project_type = None
        self.project_name = None
        self._sort_init(*args)
        
    def _sort_init(self, *args):
        print(args)
        if len(args) > 2:
            raise NotImplementedError("Not sure what you're doing here")
        if args[0]:
            if args[0][1]:
                self.project_name = args[0][1]
            if args[0][0] == "blank":
                print("Creating Blank Starter Project")
                self.project_type='blank'
            elif args[0][0] == "kitchen":
                print("Creating Kitchen Starter Project")
                self.project_type='kitchen'
        self._create_new()
        

    def get_available(self):
        """returns a list of the available starters"""
        stringy = [x for x in self.__dir__() if 'create' in x and "_create" not in x]
        return_me = {}
        for each in stringy:
            return_me[each] = self.__getattribute__(each).__doc__
        return return_me

    def _create_new(self):
        """creates a new project"""
        # 1 verify project type
        # 2 verify project name
        # 3 call the project builder for type with name
        try:
            self.project_typifier()
            self.project_namifier()
            if not self.project_confirmator():
                raise Exception("Derpy")
            print("success")
            print(self.project_name, self.project_type)
        except Exception as e:
            if e == "Derpy":
                print("Please try again")
        
        pass

    def project_typifier(self):
        if self.project_type == None:
            self.type_helper()
        else:
            print(self.project_type)
            return True

    def help(self, help_type=None):
        if help_type == 'template':
            print()
            print("=======================================================================")
            for key in self.available.keys():
                print(" {}  ".format(key.strip('create_')), self.available[key])
                print("=======================================================================")
            return input(">")
        elif help_type == 'name':
            print("What would you like to call your new project?")
            return input(">")
        else:
            return None

    def type_helper(self):
        if self.project_name:
            print("What kind of project is {} going to be?".format(self.project_name))
            x = self.help('template')
            self._sort_init(x, self.project_name)
        else:
            print("What kind of project would you like to start?")
            x = self.help('template')
            self._sort_init(x)


    def project_namifier(self):
        pass

    def project_name_helper(self):
        pass
    
    def project_confirmator(self):
        pass
    
    def create_blank(self):
        """Creates a blank starter project"""
        pass

    def create_kitchen(self):
        """Creates 'everything and the kitchen sink'"""
        pass

    def create_blog(self):
        """Creates a starter blog website"""
        pass

    def _create_dirs(self):
        pass


if __name__ in '__main__':
    sn = StartNewProject('')
    sn.get_available()
