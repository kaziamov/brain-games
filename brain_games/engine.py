#!/usr/bin/env python

import prompt
import random

from brain_games.cli import welcome_user


def the_game(name_of_game, rules):
    """General game script"""
    name = welcome_user()
    print(rules)

    game_is_on = True
    game = dict_of_games[name_of_game]
    score = 0

    for i in range(NUMBER_OF_QUESTIONS):
        if game_is_on:
            correct_answer = game()
            if correct_answer == 'yes' or correct_answer == 'no':
                user_answer = input('Your answer: ')
            else:
                user_answer = prompt.integer('Your answer: ')

            if correct_answer == user_answer:
                print('Correct!')
                score += 1
            else:
                print(''''{}' is wrong answer ;(. Correct answer was '{}'.
Let's try again, {}!'''.format(user_answer, correct_answer, name))
                game_is_on = False

    if game_is_on:
        print('Congratulations, {}!'.format(name))


def is_even_number_question():
    """Generate new question about even number.
    Ask user answer and return True if answer correct or False"""
    random_number = random.randint(1, 50)
    correct_answer = random_number % 2 == 0
    print("Question: {}".format(random_number))
    return 'yes' if correct_answer else 'no'


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


def is_greatest_divisor():
    """Generate two number for Find
    the greatest common divisor of given numbers."""
    first_num = random.randint(3, 50)
    second_num = random.randint(2, 50)
    # first_num = 17
    # second_num = 34

    print('Question: {} {}'.format(first_num, second_num))

    list_of_numbers = [second_num, first_num]
    sorted(list_of_numbers)

    highest_number = list_of_numbers[-1]
    lowest_number = list_of_numbers[0]
    # print(highest_number, lowest_number)

    highest_number_gsd = [num for num in range(1, highest_number + 1) \
                          if highest_number % num == 0]
    lowest_number_gsd = [num for num in highest_number_gsd \
                         if lowest_number % num == 0]
    # print(highest_number_gsd, lowest_number_gsd)

    correct_answer = max(lowest_number_gsd)

    return correct_answer


def is_missing_number():
    """Generate missing in the progression"""
    first_num = random.randint(3, 9)
    num_list = [str(num + first_num) for num in range(7)]
    correct_answer = (random.choice(num_list))
    num_index = num_list.index(correct_answer)
    num_list[num_index] = '..'
    secret_list = ' '.join(num_list)
    print(f'Question: {secret_list}')
    # print(correct_answer, type(correct_answer))
    correct_answer_int = int(correct_answer)
    return correct_answer_int


def is_prime_number():
    list_of_primes = [2, 3, 5, 7]
    random_number = random.randint(1, 50)
    list_of_checkup = [random_number % 2 == 0,  random_number % 5 == 0,
                       random_number % 7 == 0, random_number % 3 == 0]
    print("Question: {}".format(random_number))
    if random_number in list_of_primes:
        return True
    else:
        correct_answer = not(any(list_of_checkup))
        return 'yes' if correct_answer else 'no'


NUMBER_OF_QUESTIONS = 3

dict_of_games = {
    'brain_even': is_even_number_question,
    'brain_calc': is_calc_correct,
    'brain_gcd': is_greatest_divisor,
    'brain_progression': is_missing_number,
    'brain_prime': is_prime_number,
}
