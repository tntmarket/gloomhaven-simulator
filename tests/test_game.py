from unittest import mock

import pytest

from game import Game


def test_attack():
    game = Game([0])
    game.attack(1)

    assert game.damage == 1


def test_attack_with_bonus():
    game = Game([1])
    game.attack(1)

    assert game.damage == 2


def test_attack_with_minus():
    game = Game([-1])
    game.attack(1)

    assert game.damage == 0


def test_attack_with_negative_damage():
    game = Game([-2])
    game.attack(1)

    assert game.damage == 0


def test_attack_twice():
    game = Game([0, 0])
    game.attack(1)
    game.attack(1)

    assert game.damage == 2


def test_attack_with_crit():
    game = Game(['crit'])
    game.attack(5)

    assert game.damage == 10


def test_attack_with_miss():
    game = Game(['miss'])
    game.attack(3)

    assert game.damage == 0


def test_reshuffle_after_miss(mock_shuffle):
    game = Game(['miss'])
    game.attack(3)

    assert mock_shuffle.called


def test_reshuffle_after_crit(mock_shuffle):
    game = Game(['crit'])
    game.attack(3)

    assert mock_shuffle.called


def test_attack_depletes_deck():
    game = Game([0, 1, 2])
    game.attack(1)

    assert len(game.deck) == 2


def test_reshuffle_restores_drawn_cards():
    game = Game([0, 1, 2])
    game.attack(1)
    game.attack(1)

    game.shuffle()

    assert len(game.deck) == 3


def test_advantage_prefers_higher_card():
    game = Game([5, 0])
    game.attack(1, advantage=True)

    assert game.damage == 6


def test_advantage_prefers_crit():
    game = Game(['crit', 0])
    game.attack(2, advantage=True)

    assert game.damage == 4


def test_advantaged_crit_reshuffles(mock_shuffle):
    game = Game(['crit', 0])
    game.attack(2, advantage=True)

    assert mock_shuffle.called


def test_advantaged_miss_reshuffles(mock_shuffle):
    game = Game([0, 'miss'])
    game.attack(2, advantage=True)

    assert mock_shuffle.called


def test_advantage_applies_to_whole_attack_action():
    game = Game([1, 0, 0, 1])
    game.attack(2, advantage=True, targets=2)

    assert game.damage == 6


def test_do_not_shuffle_until_end_of_action():
    game = Game([1, 1, 'miss'])
    game.attack(2, targets=3)

    assert game.damage == 6


def test_do_not_shuffle_until_end_of_advantaged_action():
    game = Game([1, 1, 0, 'miss'])
    game.attack(2, advantage=True, targets=2)

    assert game.damage == 5


def test_reshuffle_if_out_of_cards():
    game = Game([1])
    game.attack(2, targets=2)

    assert game.damage == 6


def test_average_bonus_damage():
    game = Game([1, 2, 3])
    game.attack(1)
    game.attack(4)
    game.attack(7)

    assert game.average_bonus() == 2


def test_average_bonus_damage_with_crit_and_miss():
    game = Game(['crit', 0])
    game.attack(5)
    game.attack(5)

    game.deck = ['miss', 0]
    game.attack(5)
    game.attack(5)

    assert game.average_bonus() == 0


def test_average_bonus_damage_with_multiple_targets():
    game = Game([1])
    game.attack(1, targets=3)

    assert game.average_bonus() == 1


@pytest.fixture
def mock_shuffle():
    with mock.patch.object(Game, 'shuffle') as shuffle:
        yield shuffle


