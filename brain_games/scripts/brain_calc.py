#!/usr/bin/env python

from brain_games.games.brain_calc import RULES
from brain_games.engine import the_game


def main():
    """Main function"""
    the_game('brain_calc', RULES)


if __name__ == '__main__':
    main()
