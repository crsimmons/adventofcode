import math
import operator
from functools import reduce

from lib.util import FULL_BLOCK


def poly_area(points, perimeter):
    """
    Calculate the area of a polygon given a list of points including the points along the permiter.

    Args:
        points (list): A list of coordinates representing the points of the polygon.
        perimeter (int): The perimeter of the polygon.

    Returns:
        int: The area of the polygon.

    Example:
        >>> poly_area([(0, 0), (0, 2), (2, 2), (2, 0)],8)
        9
    """
    area = shoe_area(points)
    interior = interior_points(area, perimeter)
    return interior + perimeter

def shoe_area(points):
    """
    Calculates the area of a shoe given a list of points using the shoelace formula.

    Args:
        points (List[Tuple[int, int]]): A list of points representing the vertices of the shoe.

    Returns:
        int: The area of the polygon.
    """
    # shoelace formula
    # https://en.wikipedia.org/wiki/Shoelace_formula
    # sum of deteminants of pairs of points
    return abs(sum(x[0]*y[1] - x[1]*y[0] for x, y in zip(points, points[1:])))//2

def interior_points(area, boundary):
    """
    Calculate the number of interior points in a given area via Pick's theorem.

    Parameters:
    - area: An integer representing the total number of points in the area.
    - boundary: An integer representing the total number of points on the boundary of the area.

    Returns:
    - An integer representing the number of interior points in the area.
    """
    # pick's theorem
    # A = i + b/2 -1 -> i = A + 1 - b/2
    # boundary points (b) = perimeter
    # interior = area + 1 - perimeter // 2
    return area + 1 - boundary // 2

def dist(p1, p2):
    """
    Calculates the Manhattan distance between two points.

    :param p1: A tuple representing the coordinates of the first point.
    :param p2: A tuple representing the coordinates of the second point.
    :return: The Manhattan distance between the two points.
    """
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def order_points(points):
    """
    Orders a list of points in clockwise order around the center of the polygon.

    :param points: A list of tuples representing the coordinates of the points.
    :return: A list of tuples representing the ordered points in clockwise order around the center of the polygon.
    """
    center = tuple(map(operator.truediv, reduce(lambda x, y: map(operator.add, x, y), points), [len(points)] * 2))
    return sorted(points, key=lambda point: (-135 - math.degrees(math.atan2(*tuple(map(operator.sub, point, center))[::-1]))) % 360)

def pg(grid, points):
    """
    Generates a grid representation of points on a 2D plane.

    Parameters:
    - grid (List[List[str]]): A 2D grid of characters representing the layout.
    - points (List[Tuple[int, int]]): A list of coordinate tuples representing points on the grid.

    Returns:
    - None

    """
    R = len(grid)
    C = len(grid[0])
    for r in range(R):
        print()
        for c in range(C):
            if (r,c) in points:
                print(FULL_BLOCK, end="")
            else:
                print(grid[r][c], end="")
        print()
