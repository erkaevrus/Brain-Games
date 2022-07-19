import random
from brain_games.logics.logics import logic_games


def finder_gcd(num1, num2):
    max_num = max(num1, num2)
    min_num = min(num1, num2)
    divisor = 0
    for i in range(min_num, 0, -1):
        if min_num % i == 0 and max_num % i == 0:
            divisor = i
            break
    return divisor


def gcd(name):
    print('Find the greatest common divisor of given numbers.')
    i = 1
    while i < 4:
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        question = f'{str(num1)} {str(num2)}'
        correct_answer = str(finder_gcd(num1, num2))
        flag = logic_games(name, question, correct_answer, i)
        if flag is False:
            break
        i += 1


if __name__ == '__main__':
    gcd()
