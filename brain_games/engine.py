#!/usr/bin/env python

import prompt

NUMBER_OF_QUESTIONS = 3


def run_game(game):
    """General game script"""

    print("Welcome to the Brain Games!")
    print('May I have your name? ', end='')
    name = prompt.string()
    print('Hello, {}'.format(name))

    game_is_on = True
    print(game.DESCRIPTION)

    for i in range(NUMBER_OF_QUESTIONS):
        if game_is_on:
            correct_answer = game.get_question_and_answer()

            if correct_answer == 'yes' or correct_answer == 'no':
                user_answer = prompt.string('Your answer: ')
            else:
                user_answer = prompt.integer('Your answer: ')

            message = "'{}' is wrong answer ;(. Correct answer was '{}'"
            if correct_answer == user_answer:
                print('Correct!')
                user_answer = True
            else:
                print(message.format(user_answer, correct_answer))
                user_answer = False

            game_is_on = user_answer

    if game_is_on:
        print('Congratulations, {}!'.format(name))
    else:
        print("""Let's try again, {}!""".format(name))
