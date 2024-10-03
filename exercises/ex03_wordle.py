"An exercise coding the game Wordle"

__author__: str = "730402097"


def input_guess(secret_word_len: int) -> str:
    "Takes an inputted word and verifies it's at the appropriate length for the program."
    og_word = input(f"Enter a {secret_word_len} character word:")
    while len(og_word) != secret_word_len:
        og_word = input(
            f"That wasn't {secret_word_len} chars! Try again:"
        )  # If the parameters are met properly, the loop can close itself
    return og_word


def contains_char(input_str: str, input_char: str) -> bool:
    "Checks for a specific character in any index within the given word"
    assert len(input_char) == 1  # Ensures each character is only equal to 1
    index_path: int = (
        0  # Counts the number of times inputted string is checked for the given character.
    )
    while index_path < len(
        input_str
    ):  # This is important as it stops the loop from repeating infinitely
        if input_char == input_str[index_path]:
            return True
        index_path += 1
    return False  # Because bool is our return type, must have boolean returns


def emojified(guess: str, secret: str) -> str:
    "Gives a string of emojis signifying if an inputted word has matching characters to a secret word at each interval"
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    instance: int = (
        0  # Counts the number of times the while loop runs. At the end of the loop, it should = len(secret)
    )
    printed_string: str = (
        ""  # Will accumulate all boxes returned from the loop below, and is the returned string at the end.
    )
    while instance < len(
        secret
    ):  # stops the program from running when instance is greater than len(secret)
        if guess[instance] == secret[instance]:
            printed_string += GREEN_BOX
        else:
            if contains_char(input_char=guess[instance], input_str=secret):
                printed_string += YELLOW_BOX
            else:
                printed_string += WHITE_BOX
        instance += 1
    return printed_string


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turns: int = 1
    while turns <= 6:
        print(f"=== Turn {turns}/6 ===")
        player_guess: str = input_guess(secret_word_len=len(secret))
        result_string: str = emojified(guess=player_guess, secret=secret)
        print(result_string)  # Prints the emoji string after each guess
        if (
            result_string == len(secret) * "\U0001F7E9"
        ):  # Must put the string value instead of GREEN_BOX. Unsure why, but can be used when GREEN_BOX is "unreachable"
            print(f"You won in {turns}/6 turns!")
            return  # Ends the program if the player wins
        else:
            turns += 1
    print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
