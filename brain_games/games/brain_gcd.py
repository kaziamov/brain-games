#!/usr/bin/env python

from brain_games.engine import the_game

RULES = 'Find the greatest common divisor of given numbers.'


def main():
    """Main function"""
    the_game('brain_gcd', RULES)


if __name__ == '__main__':
    main()
