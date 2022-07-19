import random

from brain_games.engine import check_answer, ask_user, greet, NUMBER_OF_QUESTIONS


def main():
    """Main function"""
    name = greet()
    answer = True
    score = 0
    for i in range(NUMBER_OF_QUESTIONS):
        if answer:
            answer = is_greatest_divisor()
            if answer:
                score += 1

    print('Game over {}. Your score is {}'.format(name, score))


def is_greatest_divisor():
    """Generate two number for Find the greatest common divisor of given numbers."""
    first_num = random.randint(1, 50)
    second_num = random.randint(1, 50)
    print(f'Find the greatest common divisor of numbers {first_num} and {second_num}: ')
    first_num_gsd = [num for num in range(1, first_num) if first_num % num == 0]
    second_num_gsd = [num for num in range(1, second_num) if second_num % num == 0]
    compare_gsd = [num for num in first_num_gsd if num in second_num_gsd]
    correct_answer = max(compare_gsd)
    checked_answer = check_answer(correct_answer, ask_user('integer'))
    print('Correct answer -', correct_answer)
    return checked_answer


if __name__ == '__main__':
    main()
