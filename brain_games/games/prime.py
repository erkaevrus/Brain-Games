import random

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_question_answer():
    num = random.randint(1, 100)
    question = f'Question: {str(num)}'
    if is_prime(num):
        answer = 'yes'
    else:
        answer = 'no'
    return (question, answer)


def is_prime(num):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    return count == 2
