#!/usr/bin/env python

from brain_games.engine import the_game

RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def main():
    """Main function"""
    the_game('brain_even', RULES)


if __name__ == '__main__':
    main()
