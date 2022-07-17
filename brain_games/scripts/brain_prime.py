#!/usr/bin/env/ python3
from brain_games.games.prime import prime
from brain_games.logics.hello import welcome_user


def main():
    name = welcome_user()
    prime(name)


if __name__ == '__main__':
    main()
