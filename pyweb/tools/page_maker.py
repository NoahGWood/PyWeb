import os
import re

ILLEGAL_CHARS = ['~','!','@','#','$','%','^','&','*','(',')','+','=','{','}','|',':','"','<','>','?','/',';',"'",'[',']','\\','`']

class PageMaker:
    def __init__(self, app, name, route=None, blueprint=True):
        self.app = app
        self.name = self.fname_sanitizer(name)
        self.route = route
        self.blueprint = blueprint
        print(self.name)

    def run(self):
        if self.folder_generator():
            if self.file_generator():
                if self.page_updater():
                    pass
                else:
                    page_update_failed
            else:
                file generator failed
        else:
            folder generator failed
        
    def fname_sanitizer(self, name):
        return re.sub(r'[^\w]', '', name).lower().replace(' ', '_')

    def folder_generator(self):
        if !osdir(app):
            mkdir(app)
        mkdir(app/name)
        mkdir(app/name/templates)
        mkdir(app/name/static)
        return True
        pass

    def file_generator(self):
        chdir app
        touch routes.py
        with open('routes.py','w') as f:
            if self.blueprint:
                f.writelines(routes_bp_prototype)
            else:
                f.writelines(routes_prototype)
        return True

    def page_updater(self):
        pass

if __name__ in '__main__':
    pm = PageMaker("""`~test ~!@#$%^&*()_+-0987654321`1{}|}{[]\];;'/.,./[]\]+}|}{)(*&^%$#@!`1234567890-='""")
    
"""
what we need:
    1. Name of the page
    2. page route (default to page name)
    3. Is blueprint (default yes)

To create a new page:

create folders:
        basic/
                pages/
                        'new page'/
                                'static'/
                                'templates'/

create blank html file in templates dir

create routes.py
        if blueprint
                from flask import Blueprint, render_template
                from flask import current_app as app
                new_page_bp = Blueprint('new_page_bp', __name__,
                                        template_folder='templates,
                                        static_folder='static
                                        )
                @new_page_bp.route('new page')
                def new_page():
                        return render_template('new page.html')

        if not blueprint
                from flask import render_template
                from basic import app

                @app.route('new page')
                def new_page():
                        return render_template('new page.html')


append basic/pages/pages.ini:
['new page']
loc=ROOT/pages/'new page'
routes=routes.py
blueprint=True???
bp=new_page_bp"""
