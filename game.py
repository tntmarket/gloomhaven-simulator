from random import shuffle
from typing import Union, List

Card = Union[int, 'miss', 'crit']


class Game:

    def __init__(self, deck: List[Card]):
        self.original_deck = deck

        self.should_reshuffle = False
        self.deck = self.original_deck.copy()
        self.damage = 0

    def attack(self, base: int, advantage=False, targets=1):
        for target in range(targets):
            modifier = self.draw_card(base)

            if advantage:
                modifier = max(self.draw_card(base), modifier)

            self.damage += max(base + modifier, 0)

        if self.should_reshuffle:
            self.shuffle()

    def shuffle(self):
        self.deck = self.original_deck.copy()
        shuffle(self.deck)
        self.should_reshuffle = False

    def draw_card(self, base):
        if not self.deck:
            self.shuffle()

        card = self.deck.pop()

        if card == 'crit':
            self.should_reshuffle = True
            return base

        if card == 'miss':
            self.should_reshuffle = True
            return -base

        return card
        