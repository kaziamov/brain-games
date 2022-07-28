#!/usr/bin/env python

from brain_games.games.brain_even import RULES
from brain_games.engine import the_game


def main():
    """Main function"""
    the_game('brain_even', RULES)


if __name__ == '__main__':
    main()
