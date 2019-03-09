from deck import create_deck
from game import Game


def simulate_games(deck, attack_sequence, samples=1000):
    damage_samples = []
    deck = create_deck(deck)

    for _ in range(samples):
        game = Game(deck)
        game.shuffle()
        for attack in attack_sequence:
            game.attack(**attack)

        damage_samples.append(game.average_bonus())

    return damage_samples
