#!/usr/bin/python3

from PyInquirer import prompt

questions = [
    {
        'type': 'input',
        'name': 'first_name',
        'message': 'What\'s your first name?',
    },
    {
        'type': 'list',
        'name': 'l_answer',
        'choices': [
            'Jumbo',
            'Large',
            'Standard',
            'Medium',
            'Small',
            'Micro'
        ],
        'message': 'What size do you need?'
    }
]
answers = prompt(questions)
print(answers)
