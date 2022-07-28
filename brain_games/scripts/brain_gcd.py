#!/usr/bin/env python

from brain_games.games.brain_gcd import RULES
from brain_games.engine import the_game


def main():
    """Main function"""
    the_game('brain_gcd', RULES)


if __name__ == '__main__':
    main()