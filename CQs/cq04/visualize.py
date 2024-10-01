from CQs.cq04.concatenation import concat

"""imports concat function from concatenation file"""
from CQs.cq04.coordinates import get_coords

"""imports get_coords function from coordinates file"""

"""visualize"""

__author__ = "730771673"

x: str = "123"
y: str = "abc"
"""prints x and y with the import concat function"""
print(concat(x, y))

"""prints x and y with the import get_coords function"""
print(get_coords(x, y))
