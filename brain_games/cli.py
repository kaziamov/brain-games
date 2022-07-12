# cli.py
"""Module for green user in start program"""

import prompt


def welcome_user():
    """Ask user name and greet"""
    name = prompt.string('May I have your name? ')
    print(f'Nice to meet you {name}')
