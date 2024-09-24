"Practice using a while loop to iterate over a string"

__author__: str = "730402097"


def num_instances(phrase: str, search_char: str) -> None:
    index: int = 0  # To count the length of "phrase"
    instance: int = 0  # for search_char (instances "search_char" appears)
    while index < len(
        phrase
    ):  # as long as the length of index is less than/equal to phrase (putting <= will bug the code, just use <)
        if (
            phrase[index] == search_char
        ):  # will count everytime search_char appears in phrase
            instance = instance + 1
        index = index + 1
    print(instance)


num_instances(phrase="Happy Tuesday!", search_char="z")
# Does this need to be a user input? Directions unclear
