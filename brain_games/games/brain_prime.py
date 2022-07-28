#!/usr/bin/env python

import random

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime_number():
    list_of_primes = [2, 3, 5, 7]
    rm = random.randint(1, 50)
    print("Question: {}".format(rm))
    if rm in list_of_primes:
        return True
    else:
        cor = rm % 2 == 0 or rm % 5 == 0 or rm % 7 == 0 or rm % 3 == 0
        correct_answer = not(cor)
        return 'yes' if correct_answer else 'no'


if __name__ == '__main__':
    pass
