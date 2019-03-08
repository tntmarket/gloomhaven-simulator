from deck import create_deck
from game import Game


def simulate_no_advantage_game(distribution):
    game = Game(create_deck(distribution))

    game.attack(3)
    game.attack(3, targets=2)
    game.attack(2)
    game.attack(2)

    game.attack(3)
    game.attack(3)
    game.attack(2)

    game.attack(4, targets=2)
    game.attack(3)

    game.attack(3)

    game.attack(3)
    game.attack(3)
    game.attack(2)

    return game.damage


def simulate_less_advantaged_game(distribution):
    game = Game(create_deck(distribution))

    game.attack(3)
    game.attack(3, advantage=True, targets=2)
    game.attack(2)
    game.attack(2)

    game.attack(3)
    game.attack(3, advantage=True)
    game.attack(2)

    game.attack(4, advantage=True, targets=2)
    game.attack(3)

    game.attack(3, advantage=True)

    game.attack(3, advantage=True)
    game.attack(3)
    game.attack(2)

    return game.damage


def simulate_typical_game(distribution):
    game = Game(create_deck(distribution))

    game.attack(3)
    game.attack(3, advantage=True, targets=3)
    game.attack(2)
    game.attack(2)

    game.attack(3)
    game.attack(3, advantage=True)
    game.attack(2)

    game.attack(4, advantage=True, targets=3)
    game.attack(3)

    game.attack(3, advantage=True)

    game.attack(3, advantage=True, targets=3)
    game.attack(3)
    game.attack(2)

    return game.damage


def simulate_very_advantaged_game(distribution):
    game = Game(create_deck(distribution))

    game.attack(3)
    game.attack(3, advantage=True, targets=3)
    game.attack(2)

    game.attack(3)
    game.attack(3, advantage=True)
    game.attack(2)

    game.attack(4, advantage=True, targets=3)
    game.attack(3)

    game.attack(3, advantage=True)

    game.attack(3, advantage=True, targets=3)
    game.attack(3)

    game.attack(3, advantage=True, targets=3)
    game.attack(2)

    return game.damage


def simulate_games(deck, simulate_game, samples=1000):
    damage_samples = []

    for _ in range(samples):
        damage_samples.append(simulate_game(deck))

    return damage_samples
