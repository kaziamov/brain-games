import random

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime_number():
    num = random.randint(2, 50)
    correct_answer = True
    print("Question: {}".format(num))
    for i in range(2, num):
        if (num % i) == 0:
            correct_answer = False
            break
    return 'yes' if correct_answer else 'no'
