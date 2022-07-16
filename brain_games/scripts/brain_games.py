#!/usr/bin/env python

"""Module for start The Game"""

# from brain_games import cli


from brain_games.games.brain_even import is_even_number_question
from brain_games.games.brain_calc import is_calc_correct
from brain_games.games.brain_gcd import is_greatest_divisor
from brain_games.games.brain_prime import is_prime_number
from brain_games.games.brain_progression import is_missing_number
from brain_games.engine import greet


def the_game():
    """Script of game"""
    score = 0
    number_of_questions = 3
    list_of_challenges = [is_even_number_question, is_calc_correct,
                          is_greatest_divisor, is_missing_number, is_prime_number]
    user_name = greet()

    game_is_on = True

    for new_game in list_of_challenges:
        for new_question in range(number_of_questions):
            if game_is_on:
                game_is_on = new_game()
                if game_is_on:
                    score += 1
                    print(f"{user_name}'s score is {score}")

    print(f'Game Over. Your final score is {score}. Try again.')


def main():
    """User greet function"""
    print("Welcome to the Brain Games!\n")


if __name__ == '__main__':
    main()

# END
