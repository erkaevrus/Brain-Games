

def logic_games(name, question, correct_answer, i):
    print(f'Question: {question}')
    ans = input('Your answer: ')
    if ans == correct_answer:
        print('Correct!')
    else:
        print(f"'{ans}' is wrong answer ;(. Correct answer was '{correct_answer}'.\n"
        f"Let's try again, {name}!"
        )
        return False
    if i == 3:
        print(f'Congratulations, {str(name)}!')


if __name__ == '__main__':
    logic_games()
