import prompt

NUMBER_OF_ROUNDS = 3


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def get_user_answer():
    return prompt.string('Your answer: ')


def check_answer(user_answer, correct_answer):
    if user_answer == correct_answer:
        text = 'Correct!'
        return (True, text)
    else:
        text = (
            f"'{user_answer}' is wrong answer ;(."
            f"Correct answer was '{correct_answer}'."
        )
        return (False, text)


def engine(game):
    user_name = welcome_user()
    print(game.DESCRIPTION)
    count = 0
    while count < NUMBER_OF_ROUNDS:
        question, correct_answer = game.question()
        print(question)
        result, message = check_answer(get_user_answer(), correct_answer)
        print(message)
        if not result:
            print(f"Let's try again, {user_name}!")
            return
        count += 1
    print(f'Congratulations, {user_name}!')
