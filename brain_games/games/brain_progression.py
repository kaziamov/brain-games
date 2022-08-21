import random

DESCRIPTION = 'What number is missing in the progression?'


def get_question_and_answer():
    """Generate missing in the progression"""
    start = random.randint(3, 9)
    step = random.randint(3, 9)
    length = 7

    numbers = [num for num in range(start, (start + length * step), step)]
    correct_answer = (random.choice(numbers))

    progression = ' '.join([str(n) if n != correct_answer else '..' for n in numbers])
    math_message = f'{progression}'

    return correct_answer, math_message
