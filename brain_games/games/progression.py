import random

DESCRIPTION = 'What number is missing in the progression?'


def create_progression(start, step):
    progression = [start]
    length_of_progression = 10
    for element in range(length_of_progression):
        progression.append(progression[element] + step)
    return progression


def hidden_step_progression(hidden_step, progression):
    progression[hidden_step] = '..'
    progression_for_game = ' '.join(map(str, progression))
    return (progression_for_game)


def generate_question_answer():
    start = random.randint(1, 50)
    step = random.randint(1, 10)
    hidden_step = random.randint(1, 10)
    progression = create_progression(start, step)
    hidden_value = progression[hidden_step]
    question = f'Question: {hidden_step_progression(hidden_step, progression)}'
    answer = str(hidden_value)
    return (question, answer)
