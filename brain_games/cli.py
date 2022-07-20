# cli.py
"""Module for green user in start program"""

import prompt


def welcome_user():
    """Ask user name and greet"""
    print("Welcome to the Brain Games!")
    print('May I have your name? ', end='')
    name = prompt.string()
    print('Hello, {}'.format(name))
    return name
