import random

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def question():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    question = f'Question: {str(num1)} {str(num2)}'
    answer = correct_answer(num1, num2)
    return (question, answer)


def correct_answer(num1, num2):
    max_num = max(num1, num2)
    min_num = min(num1, num2)
    divisor = 0
    for i in range(min_num, 0, -1):
        if min_num % i == 0 and max_num % i == 0:
            divisor = i
            break
    return str(divisor)


if __name__ == '__main__':
    question()
