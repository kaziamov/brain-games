import random

from brain_games.engine import check_answer, ask_user


def main():
    """Main function"""
    is_even_number_question()


def is_even_number_question():
    """Generate new question about even number. Ask user answer and return True if answer correct or False"""
    random_number = random.randint(1, 50)
    correct_answer = random_number % 2 == 0
    print(f'{random_number} is even number? (Yes or No)')
    checked_answer = check_answer(correct_answer, ask_user('string'))
    print('Correct answer -', correct_answer)
    return checked_answer
