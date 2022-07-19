import prompt
import random

# Functions


def main():
    """Empty function"""
    pass


def the_game():
    """Script of game"""
    score = 0
    number_of_questions = 3
    list_of_challenges = [is_even_number_question, is_calc_correct, is_greatest_divisor, is_missing_number, is_prime_number]
    user_name = greet()

    game_is_on = True

    for new_game in list_of_challenges:
        for new_question in range(number_of_questions):
            if game_is_on:
                game_is_on = new_game()
                if game_is_on:
                    score += 1
                    print(f"{user_name}'s score is {score}")

    print(f'Game Over. Your final score is {score}. Try again.')


def greet():
    """Ask user name and say hi"""
    name = prompt.string('May I have your name? ')
    print(f'Nice to meet you {name}')
    return name


def is_even_number_question():
    """Generate new question about even number. Ask user answer and return True if answer correct or False"""
    random_number = random.randint(1, 50)
    correct_answer = random_number % 2 == 0
    print(f'{random_number} is even number? (Yes or No)')
    checked_answer = check_answer(correct_answer, ask_user('string'))
    print('Correct answer - ', correct_answer)
    return checked_answer


def is_calc_correct():
    """Create randon +, _ or * with 2 numbers and check answer"""
    actions = ['+', '-', '*']
    first_num = random.randint(1, 14)
    second_num = random.randint(1, 14)
    random_action = random.choice(actions)
    math_question = f'{first_num} {random_action} {second_num}'
    print(f'What is {math_question}?')
    correct_answer = eval(math_question)
    checked_answer = check_answer(correct_answer, ask_user('integer'))
    print('Correct answer - ', correct_answer)
    return checked_answer


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
    print('Correct answer - ', correct_answer)
    return checked_answer

def is_missing_number():
    """Generate missing in the progression"""
    first_num = random.randint(3, 9)
    num_list = [str(num + first_num) for num in range(7)]
    correct_answer = random.choice(num_list)
    num_index = num_list.index(correct_answer)
    num_list[num_index] = '. .'
    secret_list = ' '.join(num_list)
    print(f'What number is missing in the progression?\n{secret_list}')
    checked_answer = check_answer(correct_answer, str(ask_user('integer')))
    print('Correct answer - ', correct_answer)
    return checked_answer


def is_prime_number():
    number = random.randint(1, 100)
    check_list = [number % 2 != 0, number % 3 != 0, number % 5 != 0, number % 7 != 0]
    correct_answer = all(check_list)
    print(f'{number} is it a prime number? (Yes or No)')
    checked_answer = check_answer(correct_answer, ask_user('string'))
    print('Correct answer - ', correct_answer)
    return checked_answer


def ask_user(type_of_answer):
    """Ask user and return True for Yes and False for No. For int return int"""
    if type_of_answer == 'string':
        user_answer = prompt.string('Input your answer: ')
        user_answer_is_yes = user_answer[0].lower() == 'y'
        return user_answer_is_yes
    else:
        user_answer = prompt.integer('Input your answer: ')
        return user_answer


def check_answer(correct_answer, user_answer):
    """Return True if correct answer and user answer same"""
    will_it_be_continue = correct_answer == user_answer
    # print(f'Debug: user answer {user_answer}, correct answer {correct_answer}')
    if will_it_be_continue:
        print('You right!')

    else:
        print('You are wrong.')
    return will_it_be_continue


# General Code

the_game()