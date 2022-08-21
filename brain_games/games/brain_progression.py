import random

DESCRIPTION = 'What number is missing in the progression?'


def get_question_and_answer():
    """Generate missing in the progression"""
    start_number = random.randint(3, 9)
    length = 7
    numbers_in_progression = [str(num + start_number) for num in range(7)]
    correct_answer = (random.choice(num_list))
    num_index = num_list.index(correct_answer)
    num_list[num_index] = '..'
    secret_list = ' '.join(num_list)
    print(f'Question: {secret_list}')
    # print(correct_answer, type(correct_answer))
    correct_answer_int = int(correct_answer)
    return correct_answer_int
