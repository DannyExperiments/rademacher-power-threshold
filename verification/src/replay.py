"""Exact finite checks for the balanced-sign variance identity and exponent algebra."""
from fractions import Fraction as F
from itertools import combinations
from math import comb

def check_balance(weights):
    size = len(weights)
    outcomes = [
        2 * sum(weights[index] for index in positive) - sum(weights)
        for positive in combinations(range(size), size // 2)
    ]
    assert len(outcomes) == comb(size, size // 2)
    assert sum(outcomes) == 0
    variance = sum(value**2 for value in outcomes) / len(outcomes)
    average = sum(weights) / size
    assert variance == F(size, size - 1) * sum((value - average)**2 for value in weights)

cases = 0
for size in range(2, 15, 2):
    for slope in range(-3, 4):
        check_balance([F(index * index + slope * index, 2 * index + 1) for index in range(size)])
        cases += 1
for exponent in [F(i, 80) for i in range(1, 41)]:
    expected_visits = F(1, 2) - exponent
    expected_cluster = (1 - exponent) / 3
    assert expected_visits - expected_cluster == (1 - 4 * exponent) / 6
    assert (expected_visits >= expected_cluster) == (exponent <= F(1, 4))
assert F(1, 2) - F(1, 4) == (1 - F(1, 4)) / 3 == F(1, 4)
print(f"PASS: {cases} exact balanced-sign variance fixtures, 40 rational exponent fixtures, and the critical equality.")
