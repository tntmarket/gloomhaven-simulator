from collections import defaultdict
from typing import Any, Dict

Distribution = Dict[Any, int]


def add_distributions(d1: Distribution, d2: Distribution) -> Distribution:
    result = defaultdict(int)

    for option1, probability1 in d1.items():
        for option2, probability2 in d2.items():
            result[option1 + option2] += probability1 * probability2

    return result


def max_distributions(d1: Distribution, d2: Distribution) -> Distribution:
    result = defaultdict(int)

    for option1, probability1 in d1.items():
        for option2, probability2 in d2.items():
            result[max(option1, option2)] += probability1 * probability2

    return result
