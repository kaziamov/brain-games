#!/usr/bin/env python

# Import third-party modules
import prompt

QUESTIONS_COUNT = 3


def run_game(game):
    """General game script"""

    print("Welcome to the Brain Games!")
    print('May I have your name? ', end='')

    name = prompt.string()

    print('Hello, {}'.format(name))
    print(game.DESCRIPTION)

    for i in range(QUESTIONS_COUNT):
        correct_answer, question_message = game.get_question_and_answer()

        print('Question: {}'.format(question_message))

        if type(correct_answer) is str:
            user_answer = prompt.string('Your answer: ')
        else:
            user_answer = prompt.integer('Your answer: ')

        if correct_answer == user_answer:
            print('Correct!')
        else:
            print("""'{}' is wrong answer ;(. Correct answer was '{}'
Let's try again, {}!""".format(user_answer, correct_answer, name))
            return

    print('Congratulations, {}!'.format(name))
