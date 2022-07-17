import random

from brain_games.engine import check_answer, ask_user, greet, NUMBER_OF_QUESTIONS


def main():
    """Main function"""
    name = greet()
    answer = True
    count_questions = 0
    while answer and count_questions < NUMBER_OF_QUESTIONS + 1:
        count_questions = + 1
        answer = is_even_number_question()
    else:
        if answer:
            print('Congratulation {name}!')
        elif count_questions <= 3:
            print('Game over')
        else:
            print('You broke my heart and this game')


def is_even_number_question():
    """Generate new question about even number. Ask user answer and return True if answer correct or False"""
    random_number = random.randint(1, 50)
    correct_answer = random_number % 2 == 0
    print(f'{random_number} is even number? (Yes or No)')
    checked_answer = check_answer(correct_answer, ask_user('string'))
    print('Correct answer -', correct_answer)
    return checked_answer

if __name__ == '__main__':
    main()
