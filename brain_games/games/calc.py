import random
from brain_games.logics.logics import logic_games


def calc(name):
    print('What is the result of the expression?')
    i = 1
    while i < 4:
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operation = ('-', '+', '*')
        sign = random.choice(operation)
        expressions = [num1 - num2, num1 + num2, num1 * num2]
        question = f'{str(num1)} {sign} {str(num2)}'
        correct_answer = str(expressions[operation.index(sign)])
        flag = logic_games(name, question, correct_answer, i)
        if flag is False:
            break
        i += 1


if __name__ == '__main__':
    calc()
