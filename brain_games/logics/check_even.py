import random


def check_even(name):
    i = 1
    while i < 4:
        num = random.randint(1, 100)
        print('Question: ' + str(num))
        ans = input('Your answer: ')
        if num % 2 != 0 and ans != 'no':
            print("'yes' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, " + str(name) + '!')
            break
        elif num % 2 == 0 and ans != 'yes':
            print("'no' is wrong answer ;(. Correct answer was 'yes'.\nLet's try again, " + str(name) + '!')
            break
        else:
            print('Correct!')
            i += 1
    if i == 4:
        print('Congratulations, ' + str(name) + '!')


if __name__ == '__main__':
    check_even(name)
