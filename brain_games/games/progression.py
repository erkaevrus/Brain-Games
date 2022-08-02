import random

DESCRIPTION = 'What number is missing in the progression?'


def create_progression(num1, num2):
    start = num1
    step = num2
    progression = [start]
    for i in range(10):
        progression.append(progression[i] + step)
    return progression


def hidden_step_progression(num3, progression):
    hidden_step = num3
    progression[hidden_step] = '..'
    progression_for_game = ' '.join(map(str, progression))
    return (progression_for_game)


def question():
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 10)
    num3 = random.randint(1, 10)
    progression = create_progression(num1, num2)
    hidden_value = progression[num3]
    question = hidden_step_progression(num3, progression)
    answer = str(hidden_value)
    return (question, answer)


if __name__ == '__main__':
    question()
