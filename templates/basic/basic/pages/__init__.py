"""
Automated page handling
"""
import configparser
import os
import importlib

class PageLoader:
    """PageLoader reads pages.ini and automagically loads
the pages and blueprints into the app"""
    def __init__(self, app, root='basic', ignore_bad=False):
        self.app = app
        self.root = root
        self.ignore = ignore_bad

        conf = configparser.ConfigParser()
        conf.read(self.root+'/pages/pages.ini')
        self.pages = conf
        self.cwd = os.getcwd()
        self.loadable = []
        self.blueprints = []
        self.load_pages()

    def load_pages(self):
        """Master function to load all pages"""
        self.test_pages()
        # variable to check if we need to register blueprints
        bp = 0
        for page in self.loadable:
            # Check if blueprint or normal page
            # if blueprint call load_blueprint else import page
            if self.pages[page]['blueprint']:
                self._load_blueprint(page)
                bp += 1
            else:
                # import routes.py
                self._load_page(page)
        if bp > 0:
            self.register_blueprints()


    def test_pages(self):
        """Removes non-functioning pages from the loading que to reduce error messages"""
        for page in self.pages.sections():
            if self.verify_page(page):
                self.loadable.append(page)

    def verify_page(self, page):
        """Verifies that page exists and is accessible"""
        # Get the location of the file
        path = self.cwd + self._get_path(page)
        if os.path.isfile(path):
            print("{} exists.".format(page))
        else:
            if self.ignore is False:
                raise Exception("{} Does not exist. Expected to be found: {}".format(page, path))
        return True

    def _get_path(self, page, loading=False):
        """Helper function returns the path of a page"""
        location = self.pages[page]['loc'].replace('ROOT', self.root) + '/' + self.pages[page]['routes']
        if loading:
            return location.replace('/', '.').strip('.py')
        else:
            return location

    def _load_page(self, page):
        """Imports the page"""
        importlib.import_module(self._get_path(page, loading=True))

    def _load_blueprint(self, page):
        """Imports the blueprint"""
        module = importlib.import_module(self._get_path(page, loading=True))
        # Only need the blueprint class
        bp_class = getattr(module, self.pages[page]['bp'])
        # Add the blueprint to blueprint dictionary
        self.blueprints.append(bp_class)
        del module

    def register_blueprints(self):
        """Adds available blueprints to the app"""
        for blueprint in self.blueprints:
            self.app.register_blueprint(blueprint)
