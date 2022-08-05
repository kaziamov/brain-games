#!/usr/bin/env python

import prompt

from brain_games.cli import welcome_user
from brain_games.games.brain_even import get_question_and_answer
from brain_games.games.brain_progression import get_question_and_answer
from brain_games.games.brain_calc import get_question_and_answer
from brain_games.games.brain_gcd import get_question_and_answer
from brain_games.games.brain_prime import get_question_and_answer


def the_game(name_of_game, rules):
    """General game script"""
    name = welcome_user()
    print(rules)

    game_is_on = True
    game = dict_of_games[name_of_game]

    for i in range(NUMBER_OF_QUESTIONS):
        if game_is_on:
            correct_answer = game()
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
        user_answer = input('Your answer: ')
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


NUMBER_OF_QUESTIONS = 3

dict_of_games = {
    'brain_even': get_question_and_answer,
    'brain_calc': get_question_and_answer,
    'brain_gcd': get_question_and_answer,
    'brain_progression': get_question_and_answer,
    'brain_prime': get_question_and_answer,
}
