"""tea party assignment"""

__author__ = "730771673"


def main_planner(guests: int) -> None:
    """where users input to initiate the program"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea bags: " + str(tea_bags(guests)))
    print("Treats: " + str(treats(guests)))
    print("Cost: $" + str(cost(tea_bags(guests), treats(guests))))


def tea_bags(people: int) -> int:
    """number of guests attending the tea party"""
    return people * 2


def treats(people: int) -> int:
    """number of treats needed for the party"""
    return int(tea_bags(people=people) * 1.5)


# call tea_bags to calculate the # of treats needed for the party


def cost(tea_count: int, treat_count: int) -> float:
    """determines how much everything is"""
    return tea_count * 0.5 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party?")))
