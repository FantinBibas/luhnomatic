#!/usr/bin/env python3

from credit_card import CreditCard
import sys


def main(av):
    if len(av) != 2:
        print("USAGE: " + av[0] + " card_number")
    else:
        card = CreditCard(av[1])
        for possibility in card.get_all_possibilities():
            print(possibility)


if __name__ == '__main__':
    exit(main(sys.argv))
