import random

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_question_answer():
    num = random.randint(1, 100)
    question = f'Question: {num}'
    if is_even(num):
        answer = 'yes'
    else:
        answer = 'no'
    return (question, answer)


def is_even(num):
    return num % 2 == 0
