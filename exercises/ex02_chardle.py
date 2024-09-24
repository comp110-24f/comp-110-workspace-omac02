"""EXO2 - Chardle - A cute step towards Wordle."""

__author__ = "730402097"


def input_word() -> (
    str
):  # Putting None instead of str will make input_word unaccessible to assign to word in line 34
    og_word = str(input("Enter a 5-character word:"))
    if len(og_word) == 5:
        return og_word
    else:  # must be indented to the same line as if
        print("Error: Word must contain 5 characters.")
        exit()


# make sure to save + restart if the code wont work several times in a row, just in case!


def input_letter() -> str:
    og_letter = str(input("Enter a single character:"))
    if len(og_letter) == 1:
        return og_letter  # Forgetting the return statement will make the function uncallable in contains_char
    else:
        print("Error: Character must be a single character.")
        exit()


def contains_char(word: str, letter: str) -> None:
    print("Searching for " + str(letter) + " in " + str(word))
    letter_instances = 0  # Counts number of times letter appears in word.
    if word[0] == letter:
        print(letter + " found at index 0")
        letter_instances += 1
    if word[1] == letter:
        print(letter + " found at index 1")
        letter_instances += 1
    if word[2] == letter:
        print(letter + " found at index 2")
        letter_instances += 1
    if word[3] == letter:
        print(letter + " found at index 3")
        letter_instances += 1
    if word[4] == letter:
        print(letter + " found at index 4")
        letter_instances += 1
    if letter_instances == 0:
        print("No instances of " + letter + " found in " + word)
    else:
        if letter_instances == 1:
            print("1 instance of " + letter + " found in " + word)
        else:
            if letter_instances <= 5:
                print(
                    str(letter_instances)
                    + " instances of "
                    + letter
                    + " found in "
                    + word
                )


def main() -> None:
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()
