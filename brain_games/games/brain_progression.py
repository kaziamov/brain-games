import random

DESCRIPTION = 'What number is missing in the progression?'


def get_question_and_answer():
    """Generate missing in the progression"""
    start_number = random.randint(3, 9)
    length = 7
    numbers_in_progression = [str(num + start_number) for num in range(length)]
    correct_answer = (random.choice(numbers_in_progression))
    num_index = numbers_in_progression.index(correct_answer)
    numbers_in_progression[num_index] = '..'
    secret_list = ' '.join(numbers_in_progression)
    math_message = f'{secret_list}'
    correct_answer_int = int(correct_answer)

    return correct_answer_int, math_message
