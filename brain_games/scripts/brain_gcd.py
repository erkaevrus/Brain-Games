#!/usr/bin/env/ python3
from brain_games.games.gcd import gcd
from brain_games.logics.hello import welcome_user


def main():
    name = welcome_user()
    gcd(name)


if __name__ == '__main__':
    main()
