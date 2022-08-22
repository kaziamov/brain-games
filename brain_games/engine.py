#!/usr/bin/env python

# Import third-party modules
import prompt

NUMBER_OF_QUESTIONS = 3


def run_game(game):
    """General game script"""

    print("Welcome to the Brain Games!")
    print('May I have your name? ', end='')

    name = prompt.string()

    print('Hello, {}'.format(name))
    print(game.DESCRIPTION)

    msg_question = 'Question: {}'
    msg_answer = 'Your answer: '
    msg_correct = 'Correct!'
    msg_win = 'Congratulations, {}!'
    msg_wrong = """'{}' is wrong answer ;(. Correct answer was '{}'
Let's try again, {}!"""

    for i in range(NUMBER_OF_QUESTIONS):
        correct_answer, question_message = game.get_question_and_answer()

        print(msg_question.format(question_message))

        if type(correct_answer) is str:
            user_answer = prompt.string(msg_answer)
        else:
            user_answer = prompt.integer(msg_answer)

        if correct_answer == user_answer:
            print(msg_correct)
        else:
            print(msg_wrong.format(user_answer, correct_answer, name))
            return

    print(msg_win.format(name))
