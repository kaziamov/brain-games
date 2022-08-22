import random

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_question_and_answer():
    """Create random number and check is prime or not.
    Return True or False"""
    num = random.randint(2, 50)
    correct_answer = is_prime(num)
    math_message = ("{}".format(num))

    return 'yes' if correct_answer else 'no', math_message


def is_prime(number):
    """Function check is prime number or not. And return True or False"""
    for i in range(2, number):
        if (number % i) == 0:
            return False
    return True
