#!/usr/bin/env/ python3
from brain_games.games.progression import progression
from brain_games.logics.hello import welcome_user


def main():
    name = welcome_user()
    progression(name)


if __name__ == '__main__':
    main()
