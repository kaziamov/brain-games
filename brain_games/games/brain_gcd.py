import random

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def get_question_and_answer():
    """Generate two number for Find
    the greatest common divisor of given numbers."""
    first_num = random.randint(3, 50)
    second_num = random.randint(2, 50)
    # first_num = 17
    # second_num = 34

    print('Question: {} {}'.format(first_num, second_num))

    list_of_numbers = [second_num, first_num]
    sorted(list_of_numbers)

    highest_number = list_of_numbers[-1]
    lowest_number = list_of_numbers[0]
    # print(highest_number, lowest_number)

    highest_number_gsd = [num for num in range(1, highest_number + 1)
                          if highest_number % num == 0]
    lowest_number_gsd = [num for num in highest_number_gsd
                         if lowest_number % num == 0]
    # print(highest_number_gsd, lowest_number_gsd)

    correct_answer = max(lowest_number_gsd)

    return correct_answer
