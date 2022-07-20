from brain_games.logics.logics import logic_games
import random


def is_it_even(num):
    if num % 2 == 0:
        return 'yes'
    else:
        return 'no'


def check_even(name):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 1
    while i < 4:
        num = random.randint(1, 10)
        question = str(num)
        correct_answer = is_it_even(num)
        flag = logic_games(name, question, correct_answer, i)
        if flag is False:
            break
        i += 1


if __name__ == '__main__':
    check_even()
