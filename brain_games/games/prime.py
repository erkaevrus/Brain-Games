import random

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def question():
    num = random.randint(1, 100)
    question = f'Question: {str(num)}'
    answer = correct_answer(num)
    return (question, answer)


def correct_answer(num):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    if count == 2:
        return 'yes'
    else:
        return 'no'


if __name__ == '__main__':
    question()
