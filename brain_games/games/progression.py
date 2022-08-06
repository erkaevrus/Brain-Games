import random

DESCRIPTION = 'What number is missing in the progression?'


def create_progression(num1, num2):
    start = num1
    step = num2
    progression = [start]
    length_of_progression = 10
    for _ in range(length_of_progression):
        progression.append(progression[_] + step)
    return progression


def hidden_step_progression(num3, progression):
    hidden_step = num3
    progression[hidden_step] = '..'
    progression_for_game = ' '.join(map(str, progression))
    return (progression_for_game)


def generate_question_answer():
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 10)
    num3 = random.randint(1, 10)
    progression = create_progression(num1, num2)
    hidden_value = progression[num3]
    question = f'Question: {hidden_step_progression(num3, progression)}'
    answer = str(hidden_value)
    return (question, answer)
