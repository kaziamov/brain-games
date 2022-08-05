#!/usr/bin/env python

import prompt

NUMBER_OF_QUESTIONS = 3


def welcome_user():
    """Ask user name and greet"""
    print("Welcome to the Brain Games!")
    print('May I have your name? ', end='')
    name = prompt.string()
    print('Hello, {}'.format(name))
    return name


def the_game(game):
    """General game script"""

    name = welcome_user()

    game_is_on = True
    print(game.DESCRIPTION)

    for i in range(NUMBER_OF_QUESTIONS):
        if game_is_on:
            correct_answer = game.get_question_and_answer()
            user_answer = input_user_answer(correct_answer)
            game_is_on = user_answer

    if game_is_on:
        player_win(name)
    else:
        player_lose(name)


def player_lose(name):
    """Function print message."""
    print("""Let's try again, {}!""".format(name))


def player_win(name):
    """Function print message."""
    print('Congratulations, {}!'.format(name))


def input_user_answer(correct_answer):
    """Function check and return True if user answer correct."""
    if correct_answer == 'yes' or correct_answer == 'no':
        user_answer = prompt.string('Your answer: ')
    else:
        user_answer = prompt.integer('Your answer: ')

    return check_answer(correct_answer, user_answer)


def check_answer(correct_answer, user_answer):
    """Function check user answer and return True or False"""
    message = "'{}' is wrong answer ;(. Correct answer was '{}'"
    if correct_answer == user_answer:
        print('Correct!')
        return True
    else:
        print(message.format(user_answer, correct_answer))
        return False
