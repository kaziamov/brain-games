#!/usr/bin/env python

import random

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime_number():
    num = random.randint(1, 50)
    print("Question: {}".format(num))
    for i in range(2, num):
        if (num % i) == 0:
            correct_answer = False
        else:
            correct_answer = True
        return 'yes' if correct_answer else 'no'


if __name__ == '__main__':
    pass
