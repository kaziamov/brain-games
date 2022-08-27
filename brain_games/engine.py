#!/usr/bin/env python

QUESTIONS_COUNT = 3


def run_game(game):
    """General game script"""

    print("Welcome to the Brain Games!")
    print('May I have your name? ', end='')

    name = input()

    print(f'Hello, {name}')
    print(game.DESCRIPTION)

    for i in range(QUESTIONS_COUNT):
        correct_answer, question_message = game.get_question_and_answer()

        print(f'Question: {question_message}')

        user_answer = input('Your answer: ')

        if correct_answer != user_answer:
            print(f"""'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'
Let's try again, {name}!""")
            return

        print('Correct!')

    print(f'Congratulations, {name}!')
