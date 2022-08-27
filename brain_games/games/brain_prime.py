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
    primes = [2, 3, 5, 7]
    check_list = [number > 1,
                  number % 2 != 0,
                  number % 3 != 0,
                  number % 5 != 0,
                  number % 7 != 0]
    return all(check_list) or number in primes
