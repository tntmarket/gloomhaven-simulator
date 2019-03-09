import numpy as np
from simulate import simulate_games


def test_starter_deck_has_no_bonus():
    damage_samples = np.array(simulate_games(
        {
            'miss': 1,
            -2: 1,
            -1: 5,
            0: 6,
            1: 5,
            2: 1,
            'crit': 1,
        },
        [
            dict(base=2),
            dict(base=3),
            dict(base=4),
        ],
        samples=1000,
    ))

    assert -0.1 < damage_samples.mean() < 0.1
