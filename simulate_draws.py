from itertools import chain, repeat
from random import shuffle
from typing import List, Union


Card = Union[int, 'miss', 'crit']


class Game:

    def __init__(self, deck: List[Card]):
        self.original_deck = deck

        self.deck = self.original_deck.copy()
        self.damage = 0

    def attack(self, base: int, advantage=False):
        modifier = self.deck.pop()

        if advantage:
            modifier = max(self.deck.pop(), modifier)
        
        if modifier == 'crit':
            self.damage += 2 * base
            self.shuffle()
        elif modifier == 'miss':
            self.shuffle()
        else:
            self.damage += max(base + modifier, 0)

    def shuffle(self):
        self.deck = self.original_deck.copy()
        shuffle(self.deck)


def create_deck(deck_distribution):
    """
    >>> assert create_deck({ 0: 1, 3: 2 }) == [0, 3, 3]
    """
    return list(chain.from_iterable(
        repeat(card, amount)
        for card, amount
        in deck_distribution.items()
    ))


def simulate_cycle(deck):
    shuffle(deck)


def deck_to_pair_distribution(deck_distribution):
    deck = create_deck(deck_distribution)
    simulate_cycle(deck.copy())


