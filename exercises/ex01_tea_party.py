"""This program is designed to plan a tea party"""

__author__: str = "730402097"


def main_planner(guests: int) -> None:
    "Lists all supplies for a tea party"
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )

    # Put two spaces to put a space at the end of a string, but the grader will penalize you for the format (?)


def tea_bags(people: int) -> int:
    """Lists how many tea bags are needed for the guest amount."""
    return people * 2
    # Comments have to go on their seperate line, or else it will change the entire line of code
    # Make sure to refresh the website before verifying your code works properly there, as it may not update new code automatically.


def treats(people: int) -> int:
    """Lists how many treats are needed for the guest amount."""
    return int(tea_bags(people=people) * 1.5)


# Set the variable for called functions (here, it's people) equal to itself.


def cost(tea_count: int, treat_count: int) -> float:
    """Calculates the cost of the tea bags and treats for the tea party."""
    return (tea_count * 0.5) + (treat_count * 0.75)


# Don't need to call treats or tea_bags here.

if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
