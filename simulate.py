from deck import create_deck
from game import Game


def simulate_games(deck, attack_sequence, samples=1000):
    damage_samples = []

    for _ in range(samples):
        game = Game(create_deck(deck))

        for attack in attack_sequence:
            game.attack(**attack)

        damage_samples.append(game.average_bonus())

    return damage_samples
