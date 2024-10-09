"""Summing the elements of a list using different loops"""

__author__: str = "730402097"


def w_sum(vals: list[float]) -> float:
    # Adds all values in a list together using a while loop.
    idx: int = 0
    flt: float = 0.0
    while idx < len(vals):
        flt += vals[idx]
        idx += 1
    return flt


def f_sum(vals: list[float]) -> float:
    # Adds all values in a list together using a for.. in.. loop.
    flt_two: float = 0.0
    for val in vals:
        flt_two += val
    return flt_two


def f_range_sum(vals: list[float]) -> float:
    # Adds all values in a list together using a for... in range(...) loop.
    flt_three: float = 0.0
    for val in range(0, len(vals)):
        flt_three += vals[val]
    return flt_three
