"""list util functions"""

__author__ = "730771673"


def all(input: list[int], number: int) -> bool:
    # checks if all the ints in the list are same as given int
    index = 0
    while index < len(input):
        if input[index] != number:
            # checks if number is in list
            return False
        index += 1
    if len(input) == 0:
        # checks if list is empty
        return False
    return True
    # returns True if given int is in list


def max(a: list[int]) -> int:
    # returns the largest number in list
    if len(a) == 0:
        # results in an error if the list is empty
        raise ValueError("max() arg is an empty List")
    index = 0
    max_num: int = a[index]
    while index < len(a):
        # max_num will be largest
        if a[index] > max_num:
            # checks if current number is largest
            max_num = a[index]
        index += 1
    return max_num


def is_equal(a: list[int], b: list[int]) -> bool:
    # checks if every index is equal in both lists
    index = 0
    count = 0  # only goes up if the index at both lists' value is equivalent
    while index < len(a) and index < len(b):
        if a[index] == b[index]:
            # checks if element in each list matches with each other
            count += 1
        index += 1
    if count == len(a) and count == len(b):
        # checks if every single element matches every single element in both lists
        return True
    else:
        return False


def extend(a: list[int], b: list[int]) -> None:
    # mutate the first list by appending second list to end of it
    index = 0
    while index < len(b):
        a.append(b[index])
        # index is included because append does one index at a time
        index += 1
