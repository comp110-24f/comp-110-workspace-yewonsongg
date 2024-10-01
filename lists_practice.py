"""basic syntax of lists"""

# list() is a function that returns the literal []
# [] returns it directly

my_numbers: list[float] = []  # literal
my_numbers: list[float] = list()  # constructor

# add a number to a list
my_numbers.append(1.5)

# create an already populated list
game_points: list[int] = [102, 86, 94]

# subscription notation/indexing
# print(game_points[2])
last_game: int = game_points[2]

# modifying elements (because lists are mutable)
game_points[1] = 76

# getting the length
# print(len(game_points))

# remove an element
game_points.pop(1)


def display(input: list[int]) -> None:
    index = 0
    while index < len(input):
        print(input[index])
        index += 1


display(input=game_points)
