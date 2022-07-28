#!/usr/bin/env python

import random

RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even_number_question():
    """Generate new question about even number.
    Ask user answer and return True if answer correct or False"""
    random_number = random.randint(1, 50)
    correct_answer = random_number % 2 == 0
    print("Question: {}".format(random_number))
    return 'yes' if correct_answer else 'no'


if __name__ == '__main__':
    pass
