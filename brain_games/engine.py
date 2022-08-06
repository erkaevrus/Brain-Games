import prompt

NUMBER_OF_ROUNDS = 3


def engine(game):
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print(game.DESCRIPTION)
    count = 0
    while count < NUMBER_OF_ROUNDS:
        question, correct_answer = game.generate_question_answer()
        print(question)
        user_answer = prompt.string('Your answer: ')
        if correct_answer == user_answer:
            print('Correct!')
        else:
            print(
                f"'{user_answer}' is wrong answer ;(."
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {user_name}!")
            return
        count += 1
    print(f'Congratulations, {user_name}!')
