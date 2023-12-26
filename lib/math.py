import numpy as np


def evaluate_quadratic_equation(points, x):
    """
    Fit a quadratic polynomial to the given points and evaluate it at the given x value.

    Parameters:
        points (list): A list of points used to fit a quadratic polynomial.
            Each point should be a tuple of x and y coordinates.
        x (float): The x value at which to evaluate the quadratic equation.

    Returns:
        int: The result of the quadratic equation evaluation, rounded to the nearest integer.
    """
    # Fit a quadratic polynomial (degree=2) through the points
    coefficients = np.polyfit(*zip(*points), 2)

    # Evaluate the quadratic equation at the given x value
    result = np.polyval(coefficients, x)
    return round(result)
