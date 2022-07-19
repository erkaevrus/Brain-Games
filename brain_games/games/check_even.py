from brain_games.logics.logics import logic_games
import random


def check_even(name):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 1
    while i < 4:
        num = random.randint(1, 10)
        question = str(num)
        if num % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        flag = logic_games(name, question, correct_answer, i)
        if flag is False:
            break
        i += 1


if __name__ == '__main__':
    check_even()
