"Mutating Functions."

__author__: str = "730402097"


def manual_append(the_list: list[int], the_int: int) -> None:
    a.append(
        the_int
    )  # adds the int value to list A, which will be assigned to the_list


a: list[int] = [1, 2, 3]
manual_append(a, 2)  # Sets the_list = a, 2 = the_int)
print(a)


def double(db_list: list[int]) -> None:
    index_count: int = 0
    while index_count < len(db_list):
        db_list[index_count] *= 2
        index_count += 1


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1
double(list_2)
print(list_1)
print(list_2)
