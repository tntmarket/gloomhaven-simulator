from deck import create_deck


def test_create_mono_deck():
    assert create_deck({0: 2}) == [0, 0]


def test_create_deck():
    assert create_deck({0: 1, 3: 2}) == [0, 3, 3]
