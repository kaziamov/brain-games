#!/usr/bin/env python

from brain_games.games import brain_prime
from brain_games.engine import run_game


def main():
    """Main function"""
    run_game(brain_prime)


if __name__ == '__main__':
    main()
