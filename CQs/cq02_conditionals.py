"A simple number guessing game"

__author__: str = "730402097"


def guess_a_number() -> None:
    secret: int = 7
    number = int(input("Guess a number: "))
    print("Your guess was " + str(number))
    if number == 7:
        print("You got it!")
    else:
        if number < 7:
            print("Your guess was too low! The secret number is " + str(secret))
        if number > 7:
            print("Your guess was too high! The secret number is " + str(secret))


if __name__ == "__main__":
    guess_a_number()
