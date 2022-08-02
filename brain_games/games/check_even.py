import random

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def question():
    num = random.randint(1, 100)
    question = f'Question: {num}'
    answer = correct_answer(num)
    return (question, answer)


def correct_answer(num):
    if num % 2 == 0:
        return 'yes'
    else:
        return 'no'


if __name__ == '__main__':
    question()
