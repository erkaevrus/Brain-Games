import random
from brain_games.logics.logics import logic_games


def create_progression(num1, num2):
    start = num1
    step = num2
    progression = [start]
    for i in range(10):
        progression.append(progression[i]+step)
    return progression


def hidden_step_progression(num3, progression):
    hidden_step = num3
    progression[hidden_step] = '..'
    progression_for_game = ' '.join(map(str, progression))
    return progression_for_game


def progression(name):
    print('What number is missing in the progression?')
    i = 1
    while i < 4:
        num1 = random.randint(1, 50)
        num2 = random.randint(1, 10)
        num3 = random.randint(1, 10)
        question = hidden_step_progression(num3, create_progression(num1, num2))
        correct_answer = str(create_progression(num1, num2)[num3])
        flag = logic_games(name, question, correct_answer, i)
        if flag == False:
            break
        i += 1
