import random
from brain_games.logics.logics import logic_games


def is_it_prime(num):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    if count == 2:
        return 'yes'
    else:
        return 'no'


def prime(name):
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    i = 1
    while i < 4:
        num = random.randint(1, 100)
        question = str(num)
        correct_answer = is_it_prime(num)
        flag = logic_games(name, question, correct_answer, i)
        if flag is False:
            break
        i += 1


if __name__ == '__main__':
    prime()
