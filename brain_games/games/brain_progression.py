#!/usr/bin/env python

from brain_games.engine import the_game

RULES = 'What number is missing in the progression?'


def main():
    """Main function"""
    the_game('brain_progression', RULES)


if __name__ == '__main__':
    main()
