import prompt
import random

# Functions

def main():
    pass


def is_even_number_question():
    """Generate new question about even number. Ask user answer and return True if answer correct or False"""

    random_number = random.randint(1, 50)

    user_answer = prompt.string(f'{random_number} is even number?')
    user_answer_is_yes = user_answer[0].lower() == 'y'

    correct_answer = random_number % 2 == 0
    will_it_be_continue = user_answer_is_yes == correct_answer

    # print(user_answer_is_yes, correct_answer)

    if will_it_be_continue:
        print('Correct answer!')

    else:
        print('Uncorrect answer.')

    return will_it_be_continue

# Variables

points_count = 0
number_of_questions = 3

# Main Code

user_name = prompt.string('May I have your name? ')
print(f'Nice to meet you {user_name}')

game_is_on = True

while game_is_on and number_of_questions > 0:
    game_is_on = is_even_number_question()
    if game_is_on:
        points_count += 1
        number_of_questions -= 1
    else:
        print('Game Over. Try again.')
        break
