from functools import reduce

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

def extended_gcd(a, b):
    """
    Compute the greatest common divisor (gcd) of two numbers a and b,
    along with coefficients x and y that satisfy the equation:

        a * x + b * y = gcd(a, b)

    This function implements the Extended Euclidean Algorithm.

    Parameters:
    a (int): The first integer.
    b (int): The second integer.

    Returns:
    tuple: (gcd, x, y) where:
        - gcd is the greatest common divisor of a and b,
        - x and y are the coefficients satisfying the equation.
    """

    # Base case: when b is 0, gcd(a, 0) = a
    # The equation becomes a * 1 + b * 0 = a, so x = 1, y = 0
    if b == 0:
        return a, 1, 0

    # Recursive case: Perform the Euclidean step
    # a = b * q + r, where q = a // b and r = a % b
    # gcd(a, b) is the same as gcd(b, r)
    gcd, x1, y1 = extended_gcd(b, a % b)

    # Now, backtrack to compute the coefficients for the current step
    # Using the result from the recursive call, we know:
    #     b * x1 + r * y1 = gcd
    # Substituting r = a - b * (a // b), we get:
    #     b * x1 + (a - b * (a // b)) * y1 = gcd
    #     a * y1 + b * (x1 - (a // b) * y1) = gcd
    # Therefore, x = y1 and y = x1 - (a // b) * y1
    x = y1
    y = x1 - (a // b) * y1

    # Return the gcd and the updated coefficients x and y
    return gcd, x, y


def crt(congruences):
    """
    Solve a system of congruences using the Chinese Remainder Theorem.

    Parameters:
    congruences (list of tuples): List of tuples [(v1, m1), (v2, m2), ...]
        where x ≡ v (mod m).

    Returns:
    int: The smallest non-negative solution to the system of congruences.
    """

    # Combine congruences step by step
    def combine(c1, c2):
        """
        Combine two congruences into one.

        Parameters:
        c1 (tuple): First congruence (v1, m1) where x ≡ v1 (mod m1).
        c2 (tuple): Second congruence (v2, m2) where x ≡ v2 (mod m2).

        Returns:
        tuple: Combined congruence (v, m) where x ≡ v (mod m).
        """
        v1, m1 = c1
        v2, m2 = c2
        gcd, x1, _ = extended_gcd(m1, m2)

        m = (m1 * m2) // gcd

        if (v2 - v1) % gcd != 0:
            raise ValueError("No solution exists for the given system of congruences")

        # x ≡ v1 (mod m1) -> x = v1 + m1 * t for some integer t
        # substitute into x ≡ v2 (mod m2) to get
        # v1 + m1 * t ≡ v2 (mod m2) -> m1 * t ≡ v2 - v1 (mod m2)
        # -> t * (m1/g) ≡ (v2 - v1) / g (mod m2/g)

        # let the modular inverse of m1/g (mod m2/g) be x1 satisfying
        # m1/g * x1 ≡ 1 (mod m2/g)
        # then t = x1 * (v2 - v1) / g (mod m2/g)

        # substitute t into x = v1 + m1 * t to get
        # x = v1 + m1 * (x1 * (v2 - v1) / g (mod m2/g))
        k = v1 + m1 * ((x1 * (v2 - v1) // gcd) % (m2 // gcd))
        return k % m, m

    # Reduce the list of congruences iteratively
    return reduce(combine, congruences)[0]
