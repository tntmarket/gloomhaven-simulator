START = {
    'miss': 1,
    -2: 1,
    -1: 5,
    0: 6,
    1: 5,
    2: 1,
    'crit': 1,
}


def apply_perk(deck, perk):
    deck = deck.copy()

    for card, amount in perk.items():
        deck[card] += amount

    return deck


def compare_various_perks(deck):
    return {
        'Start': deck,
        'Remove 0 0 0 0': apply_perk(deck, {0: -4}),
        'Add +2': apply_perk(deck, {2: 1}),
        'Replace -1 => +1': apply_perk(deck, {-1: -1, 1: 1}),
    }
