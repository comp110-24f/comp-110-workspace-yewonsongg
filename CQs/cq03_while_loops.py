"""while loops"""

__author__ = "730771673"


def num_instances(phrase: str, search_char: str) -> int:
    # this function returns the amount of a specific character in a phrase
    count = 0
    x = 0
    while x < len(phrase):
        if phrase[x] == search_char:
            # count increases by 1 when same character in phrase is found
            count += 1
        x += 1
    return count
