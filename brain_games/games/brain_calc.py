import random

DESCRIPTION = 'What is the result of the expression?'


def get_question_and_answer():
    """Create randon +, _ or * with 2 numbers and check answer"""
    actions = ['+', '-', '*']
    first_num = random.randint(1, 14)
    second_num = random.randint(1, 14)
    random_action = random.choice(actions)
    math_question = f'{first_num} {random_action} {second_num}'
    print('Question: {}'.format(math_question))
    correct_answer = eval(math_question)
    return correct_answer
