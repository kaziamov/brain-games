import random

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question_and_answer():
    """Generate new question about even number.
    Ask user answer and return True if answer correct or False"""
    random_number = random.randint(1, 50)
    correct_answer = 'yes' if random_number % 2 == 0 else 'no'

    return correct_answer, random_number
