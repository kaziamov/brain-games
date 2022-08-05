import random

DESCRIPTION = 'What number is missing in the progression?'


def get_question_and_answer():
    """Generate missing in the progression"""
    first_num = random.randint(3, 9)
    num_list = [str(num + first_num) for num in range(7)]
    correct_answer = (random.choice(num_list))
    num_index = num_list.index(correct_answer)
    num_list[num_index] = '..'
    secret_list = ' '.join(num_list)
    print(f'Question: {secret_list}')
    # print(correct_answer, type(correct_answer))
    correct_answer_int = int(correct_answer)
    return correct_answer_int
