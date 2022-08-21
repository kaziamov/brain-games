#!/usr/bin/env python

from brain_games.games import brain_progression
from brain_games.engine import run_game


def main():
    """Main function"""
    run_game(brain_progression)


if __name__ == '__main__':
    main()
