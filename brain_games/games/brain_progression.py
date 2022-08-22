import random

DESCRIPTION = 'What number is missing in the progression?'


def get_question_and_answer():
    """Generate missing in the progression"""
    start_number = random.randint(3, 9)
    step = random.randint(3, 9)
    length = 7

    numbers = [num for num in range(start_number, (start_number + length * step), step)]
    correct_answer = (random.choice(numbers))

    progression = ' '.join([str(number) if number != correct_answer
                            else '..' for number in numbers])
    math_message = f'{progression}'

    return correct_answer, math_message
