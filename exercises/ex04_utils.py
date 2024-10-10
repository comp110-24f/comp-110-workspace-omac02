"""Practice using computational functions."""

__author__: str = "730402097"


def all(list_a: list[int], match: int) -> bool:
    idx: int = 0
    if len(list_a) == 0:
        return False
    while idx < len(list_a):
        if list_a[idx] == match:
            idx += 1
        else:
            return False
    return True


def max(input: list[int]) -> int:
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    while len(input) > 1:  # While loop until only one variable (the max) remains
        if input[0] > input[1]:
            input.pop(1)
        else:
            input.pop(0)
    return input[0]  # returns an int value


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    instance: int = 1
    if len(list_1) != len(list_2):
        return False
    while instance < len(
        list_1
    ):  # using "and" will ensure instance remains smaller than both lists, making sure the length of the lists can vary.
        if list_1[instance] != list_2[instance]:
            return False  # Exits the program as soon as two items do not match.
        instance += 1
    return True


def extend(list_1: list[int], list_2: list[int]) -> None:
    instance: int = 0
    while instance < len(list_2):
        list_1.append(
            list_2[instance]
        )  # Will add a new value of list_2 to list_1 as long as the while loop is running. the loop automatically exits when all list_2 variables have been added.
        instance += 1


# no return value needed!
