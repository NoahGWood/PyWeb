#!/usr/bin/python3

from PyInquirer import prompt

questions = [
    {
        'type': 'input',
        'name': 'appName',
        'message': "Project Name:",
    },
    {
        'type': 'list',
        'name': 'template',
        'choices': [
            'Blank        | A blank starter project',
            'Sidemenu     | A starting project with a side menu',
            'Dashboard    | A starting project with a dashboard panel',
            'Blog         | A starting project for a blog site',
            'Kitchen      | A kitchen-sink application that shows off all pyweb has to offer'
        ],
        'message': 'Starter Template:'
    }
]


answers = prompt(questions, answers=['bob','Blank        | A blank starter project'])
print(answers)
