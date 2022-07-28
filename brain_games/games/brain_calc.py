#!/usr/bin/env python

import random

RULES = 'What is the result of the expression?'

def is_calc_correct():
    """Create randon +, _ or * with 2 numbers and check answer"""
    actions = ['+', '-', '*']
    first_num = random.randint(1, 14)
    second_num = random.randint(1, 14)
    random_action = random.choice(actions)
    math_question = f'{first_num} {random_action} {second_num}'
    print('Question: {}'.format(math_question))
    correct_answer = eval(math_question)
    return correct_answer

if __name__ == '__main__':
    pass
