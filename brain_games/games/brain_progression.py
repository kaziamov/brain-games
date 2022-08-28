import random

DESCRIPTION = 'What number is missing in the progression?'


def get_question_and_answer():
    """Generate missing in the progression"""
    start_number = random.randint(3, 9)
    step = random.randint(3, 9)
    length = 7

    numbers = list(range(start_number, (start_number + length * step), step))
    progression = ' '.join(map(str, numbers))

    hidden_index = random.randrange(0, length)
    correct_answer, progression[hidden_index] = progression[hidden_index], '..'

    math_message = f'{progression}'

    return str(correct_answer), math_message
