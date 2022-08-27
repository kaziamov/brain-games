import random

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def get_question_and_answer():
    """Generate two number for Find
    the greatest common divisor of given numbers."""
    first_num = random.randint(3, 50)
    second_num = random.randint(2, 50)

    math_question = '{} {}'.format(first_num, second_num)

    correct_answer = find_gcd(first_num, second_num)

    return correct_answer, math_question


def find_gcd(num1, num2):
    """Function find GCD for two numbers and return GSD"""
    if not num2:
        return num1
    return find_gcd(num2, num1 % num2)
