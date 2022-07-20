# cli.py
"""Module for green user in start program"""

import prompt


def welcome_user():
    """Ask user name and greet"""
    print('May I have your name? ', end='')
    name = prompt.string()
    print(f'Hello, {name}')
