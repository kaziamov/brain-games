import random

from brain_games.engine import check_answer, ask_user


def main():
    is_missing_number()


def is_missing_number():
    """Generate missing in the progression"""
    first_num = random.randint(3, 9)
    num_list = [str(num + first_num) for num in range(7)]
    correct_answer = random.choice(num_list)
    num_index = num_list.index(correct_answer)
    num_list[num_index] = '. .'
    secret_list = ' '.join(num_list)
    print(f'What number is missing in the progression?\n{secret_list}')
    checked_answer = check_answer(correct_answer, str(ask_user('integer')))
    print('Correct answer -', correct_answer)
    return checked_answer
