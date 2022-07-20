#!/usr/bin/env python

from brain_games.engine import the_game

RULES = 'What is the result of the expression?'


def main():
    """Main function"""
    the_game('brain_calc', RULES)


if __name__ == '__main__':
    main()
