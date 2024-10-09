"""mutating functions"""

__author__ = "730771673"


def manual_append(a: list[int], b: int) -> None:
    # adding integer b to the end of list a
    a.append(b)


def double(a: list[int]) -> None:
    # doubling the integers in list
    index = 0
    while index < len(a):
        # while loop will go through each integer in list
        a[index] *= 2
        # remember *= is multiply
    index += 1


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1
double(list_2)
print(list_1)
print(list_2)
