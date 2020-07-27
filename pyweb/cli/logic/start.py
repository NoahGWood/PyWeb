#!/usr/bin/python3

from PyInquirer import prompt

questions = [
    {
        'type': 'input',
        'name': 'app_name',
        'message': 'What Should We Call Your New App?',
    },
    {
        'type': 'list',
        'name': 'l_answer',
        'choices': [
            'Basic',
            'Dashboard'
        ],
        'message': 'What Template Do You Need?'
    }
]
answers = prompt(questions)
print(answers)


def START():
    print("Starting with arguments: {}".format(answers))
