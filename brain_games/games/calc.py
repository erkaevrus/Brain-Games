import random

DESCRIPTION = 'What is the result of the expression?'
OPERATIONS = ('-', '+', '*')


def generate_operation():
    return random.choice(OPERATIONS)


def question():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operation = generate_operation()
    question = f'Question: {num1} {operation} {num2}'
    answer = correct_answer(num1, num2, operation)
    return (question, answer)


def correct_answer(num1, num2, operation):
    expressions = [num1 - num2, num1 + num2, num1 * num2]
    correct_answer = str(expressions[OPERATIONS.index(operation)])
    return correct_answer


if __name__ == '__main__':
    question()
