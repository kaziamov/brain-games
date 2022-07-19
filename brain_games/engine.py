#!/usr/bin/env python

import prompt

NUMBER_OF_QUESTIONS = 3

def greet():
    """Ask user name and say hi"""
    print("Welcome to the Brain Games!\n")
    name = prompt.string('May I have your name? ')
    print(f'Nice to meet you {name}')
    return name


def ask_user(type_of_answer):
    """Ask user and return True for Yes and False for No. For int return int"""
    if type_of_answer == 'string':
        user_answer = prompt.string('Input your answer: ')
        user_answer_is_yes = user_answer[0].lower() == 'y'
        return user_answer_is_yes
    else:
        user_answer = prompt.integer('Input your answer: ')
        return user_answer


def check_answer(correct_answer, user_answer):
    """Return True if correct answer and user answer same"""
    will_it_be_continue = correct_answer == user_answer
    # print(f'Debug: user answer {user_answer}, correct answer {correct_answer}')
    if will_it_be_continue:
        print('You right!')
    else:
        print('You are wrong.')
    return will_it_be_continue
