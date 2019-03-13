from random import shuffle
from typing import Union, List

Card = Union[int, 'miss', 'crit']


class Game:

    def __init__(self, deck: List[Card]):
        self.original_deck = deck.copy()

        self.should_reshuffle = False
        self.deck = self.original_deck.copy()
        self.num_attacks = 0
        self.total_base_damage = 0
        self.damage = 0

    def attack(self, base: int, advantage=False, targets=1):
        for target in range(targets):
            modifier = self.draw_card(base)

            if advantage:
                modifier = max(self.draw_card(base), modifier)

            self.damage += max(base + modifier, 0)
            self.total_base_damage += base
            self.num_attacks += 1

        if self.should_reshuffle:
            self.shuffle()

    def average_bonus(self):
        return (self.damage - self.total_base_damage)/self.num_attacks

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

        if card == 'bless':
            self.original_deck.remove('bless')
            return base

        if card == 'miss':
            self.should_reshuffle = True
            return -base

        return card

