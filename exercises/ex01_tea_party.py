"""tea party assignment"""

__author__ = "730771673"


def main_planner(guests: int) -> None:
    """where the user's input calculates the total cost"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea bags: " + str(tea_bags(guests)))
    print("Treats: " + str(treats(guests)))
    print("Cost: $" + str(cost(tea_bags(guests), treats(guests))))


# the main function has to be at top; runs top to bottom


def tea_bags(people: int) -> int:
    """determining the number of tea bags needed"""
    return people * 2


# teabags=people*2


def treats(people: int) -> int:
    """number of treats needed for the party"""
    return int(tea_bags(people=people) * 1.5)


# call tea_bags to calculate the # of treats needed for the party; teabags*1.5


def cost(tea_count: int, treat_count: int) -> float:
    """determines how much everything is"""
    return tea_count * 0.5 + treat_count * 0.75


# cost=tea*0.5 + treat*0.75

if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party?")))

# where user inputs the number of guests, initiating the program
