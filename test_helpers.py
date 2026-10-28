"""Shared helper functions for the stones.py test suite."""
import math

import stones


def run_main(monkeypatch, capsys, lower_limit, upper_limit):
    """Runs stones.main() with the given limits and returns
    (return value, full console output)."""
    inputs = iter([str(lower_limit), str(upper_limit)])
    monkeypatch.setattr("builtins.input", lambda *_args: next(inputs))
    result = stones.main()
    output = capsys.readouterr().out
    return result, output


def expected_numbers(upper_limit):
    """Reference sequence of all "Nummer=" values printed by a correct solution."""
    numbers = []
    for day in range(1, upper_limit + 1):
        number = day
        while number < upper_limit:
            numbers.append(number)
            number += day
    return numbers


def expected_stones(upper_limit):
    """Reference stones list.

    stones[index] is toggled once per divisor of `index`, so it ends up
    "blue" iff index is a perfect square. Index 0 is never reached by the
    loops (day and number both start at 1), so it always stays "green".
    """
    stone_list = []
    for index in range(upper_limit):
        if index == 0:
            stone_list.append("green")
            continue
        root = math.isqrt(index)
        stone_list.append("blue" if root * root == index else "green")
    return stone_list


def square_count_up_to(limit):
    """Number of perfect squares in the range 1..limit."""
    if limit < 1:
        return 0
    return math.isqrt(limit)
