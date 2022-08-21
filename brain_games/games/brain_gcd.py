import random

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def get_question_and_answer():
    """Generate two number for Find
    the greatest common divisor of given numbers."""
    first_num = random.randint(3, 50)
    second_num = random.randint(2, 50)

    math_question = '{} {}'.format(first_num, second_num)

    list_of_numbers = [second_num, first_num]
    sorted(list_of_numbers)

    highest_number = list_of_numbers[-1]
    lowest_number = list_of_numbers[0]

    correct_answer = find_gcd(lowest_number, highest_number)

    return correct_answer, math_question


def find_gcd(low_num, high_num):
    """Function find GCD for two numbers and return GSD"""
    highest_number_gcd = [num for num in range(1, high_num + 1)
                          if high_num % num == 0]
    lowest_number_gcd = [num for num in highest_number_gcd
                         if low_num % num == 0]
    gcd = max(lowest_number_gcd)

    return gcd
