#!/usr/bin/env/ python3
from brain_games.logics.check_even import check_even
from brain_games.logics.hello import welcome_user
import prompt


def main():
    welcome_user()
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    check_even(name)


if __name__ == '__main__':
    main()
