import random

from brain_games.engine import check_answer, ask_user, greet, NUMBER_OF_QUESTIONS


def main():
    """Main function"""
    name = greet()
    answer = True
    score = 0
    for i in range(NUMBER_OF_QUESTIONS):
        if answer:
            answer = is_even_number_question()
            if answer:
                score += 1

    print('Game over {}. Your score is {}'.format(name, score))


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
