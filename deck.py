from itertools import chain, repeat


def create_deck(deck_distribution):
    """
    >>> assert create_deck({ 0: 1, 3: 2 }) == [0, 3, 3]
    """
    return list(chain.from_iterable(
        repeat(card, amount)
        for card, amount
        in deck_distribution.items()
    ))