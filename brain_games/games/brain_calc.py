# Import build-in modules
import random
import operator


DESCRIPTION = 'What is the result of the expression?'


def get_question_and_answer():
    """Create randon +, _ or * with 2 numbers and check answer"""
    actions = {'+': operator.add, '*': operator.mul, '-': operator.sub}
    first_num = random.randint(1, 14)
    second_num = random.randint(1, 14)
    random_action = random.choice(list(actions))
    math_question = f'{first_num} {random_action} {second_num}'
    correct_answer = actions[random_action](first_num, second_num)

    return str(correct_answer), math_question
