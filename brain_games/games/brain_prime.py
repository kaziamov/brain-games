#!/usr/bin/env python

from brain_games.engine import the_game

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def main():
    """Main function"""
    the_game('brain_prime', RULES)


if __name__ == '__main__':
    main()
