"""coordinates"""

__author__ = "730771673"


def get_coords(xs: str, ys: str) -> None:
    """input becomes coordinates"""
    index = 0
    while index < len(xs):
        """creates a loop to match each character by x"""
        index1 = 0
        while index1 < len(ys):
            """creates a loop to each character by y"""
            print("(" + xs[index] + "," + ys[index1] + ")")
            index1 += 1
        index += 1
