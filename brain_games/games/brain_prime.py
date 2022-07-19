import random

from brain_games.engine import check_answer, ask_user, greet, NUMBER_OF_QUESTIONS


def main():
    """Main function"""
    name = greet()
    answer = True
    score = 0
    for i in range(NUMBER_OF_QUESTIONS):
        if answer:
            answer = is_prime_number()
            if answer:
                score += 1

    print('Game over {}. Your score is {}'.format(name, score))


def is_prime_number():
    number = random.randint(1, 100)
    check_list = [number % 2 != 0, number % 3 != 0, number % 5 != 0, number % 7 != 0]
    correct_answer = all(check_list)
    print(f'{number} is it a prime number? (Yes or No)')
    checked_answer = check_answer(correct_answer, ask_user('string'))
    print('Correct answer -', correct_answer)
    return checked_answer


if __name__ == '__main__':
    main()
