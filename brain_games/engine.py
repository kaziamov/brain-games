#!/usr/bin/env python

import prompt

from brain_games.cli import welcome_user
from brain_games.games.brain_even import is_even_number_question
from brain_games.games.brain_progression import is_missing_number
from brain_games.games.brain_calc import is_calc_correct
from brain_games.games.brain_gcd import is_greatest_divisor
from brain_games.games.brain_prime import is_prime_number


def the_game(name_of_game, rules):
    """General game script"""
    name = welcome_user()
    print(rules)

    game_is_on = True
    game = dict_of_games[name_of_game]
    score = 0

    for i in range(NUMBER_OF_QUESTIONS):
        if game_is_on:
            correct_answer = game()
            if correct_answer == 'yes' or correct_answer == 'no':
                user_answer = input('Your answer: ')
            else:
                user_answer = prompt.integer('Your answer: ')

            if correct_answer == user_answer:
                print('Correct!')
                score += 1
            else:
                print(''''{}' is wrong answer ;(. Correct answer was '{}'.
Let's try again, {}!'''.format(user_answer, correct_answer, name))
                game_is_on = False

    if game_is_on:
        print('Congratulations, {}!'.format(name))


NUMBER_OF_QUESTIONS = 3

dict_of_games = {
    'brain_even': is_even_number_question,
    'brain_calc': is_calc_correct,
    'brain_gcd': is_greatest_divisor,
    'brain_progression': is_missing_number,
    'brain_prime': is_prime_number,
}
