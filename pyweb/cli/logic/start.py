#!/usr/bin/python3
from PyInquirer import prompt
 
def START():   
    title = [
        {
            'type': 'input',
            'name': 'app_name',
            'message': 'What Should We Call Your New App?',
        },
        {
            'type': 'list',
            'name': 'template',
            'choices': [
                'Basic',
                'Dashboard'
            ],
            'message': 'What Template Do You Need?'
        },
        {
            'type':'confirm',
            'name':'ignore_bad',
            'choices': [
                True,
                False,
            ],
            'message': "Ignore (don't serve) bad pages?"
        },
        {
            'type': 'confirm',
            'name': 'navbar',
            'choices': [
                True,
                False,
            ],
            'message': "Enable NavBar?"
        },
        {
            'type': 'confirm',
            'name': 'branded',
            'choices': [
                True,
                False
            ],
            'message': 'Enable branding?'
        },
        {
            'type':'confirm',
            'name': 'add_meta',
            'choices': [
                True,
                False,
            ],
            'message': "Add custom meta?"
        },
        {
            'type': 'confirm',
            'name': 'admin',
            'choices': [
                False,
                True
            ],
            'message': "Enable admin login?"
        },
        {
            'type': 'confirm',
            'name': 'user',
            'choices': [
                False,
                True
            ],
            'message': "Enable user accounts?"
        }
    ]
    
    title_answers = prompt(title)
    name = title_answers['app_name']
    
    meta = [
        {
            'type':'input',
            'name':'description',
            'message': 'Enter a description for "{}" (optional)'.format(name)
        },
        {
            'type':'input',
            'name':'content',
            'message': 'Enter content meta for "{}" (optional)'.format(name)
        },
        {
            'type': 'input',
            'name': 'keywords',
            'message': 'Add some keywords for "{}" (comma separated)'.format(name)
        },
        {
            'type': 'input',
            'name': 'author',
            'message': 'Add your name as the project author :)'
        }
    ]
    
    navbar = [
            {
                'type': 'confirm',
                'name': 'searchbar',
                'choices': [
                    True,
                    False
                ],
                'message': "Enable searchbar?"
            }
            ]
    
    branding = [
        {
            'type': 'input',
            'name': 'href',
            "message": "URL for brand link (default: '/' )"
        },
        {
            'type': 'input',
            'name': 'name',
            'message': "Name of brand (default {})".format(name)
        },
        {
            'type': 'input',
            'name': 'image',
            'message': "URL to brand image (default {}/static/brand.png)".format(name)
        }
    ]
    
    
    meta_answers={
        'description':'',
        'content':'',
        'keywords':'',
        'author':''
        }
    navbar_answers={'searchbar':False}
    branding_answers={
        'enabled':False,
        'href':'/',
        'name':'',
        'image':'./static/brand.png'
        }
    
    if title_answers['add_meta']:
        meta_answers = prompt(meta)
    
    if title_answers['navbar']:
        navbar_answers = prompt(navbar)
    
    if title_answers['branded']:
        branding_answers = prompt(branding)
    
    answers = {
        'main': title_answers,
        'meta': meta_answers,
        'navbar': navbar_answers,
        'branding': branding_answers
        }
    
    if title_answers['template'] == 'Basic':
        from cli.logic.generators.basic import BasicTemplate
        BasicTemplate(answers)
    
