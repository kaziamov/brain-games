#!/usr/bin/env python

import prompt



NUMBER_OF_QUESTIONS = 3

def greet():
    """Ask user name and say hi"""
    name = prompt.string('May I have your name? ')
    print(f'Nice to meet you {name}')
    return name


def ask_user(type_of_answer):
    """Ask user and return True for Yes and False for No. For int return int"""
    if type_of_answer == 'string':
        print('Answer "yes" if the number is even, otherwise answer "no".')
        user_answer = prompt.string('Question: ')
        user_answer_is_yes = user_answer[0].lower() == 'y'
        return user_answer_is_yes
    else:
        user_answer = prompt.integer('Question: ')
        return user_answer


def check_answer(correct_answer, user_answer):
    """Return True if correct answer and user answer same"""
    will_it_be_continue = correct_answer == user_answer
    # print(f'Debug: user answer {user_answer}, correct answer {correct_answer}')
    if will_it_be_continue:
        print('You right!')
    else:
        print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
    return will_it_be_continue
