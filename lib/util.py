import re

FULL_BLOCK = '█'

# right, down, left, up
DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

DIAG_DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1),(-1,-1),(1,1),(-1,1),(1,-1)]


def nums(string):
    """
    Generate a list of integers from a string.

    Args:
        string (str): The input string.

    Returns:
        list: A list of integers generated from the string.
    """
    return list(map(int, re.findall(r"-?\d+", string)))


def rm_element(list, index):
    """
        Removes an element from a list at a given index.

        Args:
            list (list): The list from which the element will be removed.
            index (int): The index of the element to be removed.

        Returns:
            list: A new list with the element removed.
    """
    return list[:index] + list[index + 1:]

def split_range(op, n, lo, hi):
    """
    Split a range based on an operator and a number.

    Parameters:
        op (str): The operator to use for splitting the range. It can be one of the following: ">", "<", ">=", "<=".
        n (int): The number to use for splitting the range.
        lo (int): The lower bound of the range.
        hi (int): The upper bound of the range.

    Returns:
        tuple: A tuple containing the new lower bound, new upper bound, opposite lower bound, and opposite upper bound.

    Examples:
        split_range(">", 5, 0, 10) -> (6, 10, 0, 5)
        split_range("<", 5, 0, 10) -> (0, 4, 6, 10)
        split_range(">=", 5, 0, 10) -> (5, 10, 0, 4)
        split_range("<=", 5, 0, 10) -> (0, 5, 6, 10)
    """
    alo, ahi = lo, hi
    if op == ">":
        lo = max(lo, n + 1)
        ahi = min(ahi, n)
    elif op == "<":
        hi = min(hi, n - 1)
        alo = max(alo, n)
    elif op=='>=':
        lo = max(lo, n)
        ahi = min(ahi, n - 1)
    elif op=='<=':
        hi = min(hi, n)
        alo = max(alo, n + 1)
    else:
        assert False

    return lo, hi, alo, ahi

def find_middle(lst):
    """
    Find the middle element(s) of a list.

    Args:
        lst (list): The list from which to find the middle element(s).

    Returns:
        element or tuple: The middle element if the list length is odd,
        otherwise a tuple containing the two middle elements if the list
        length is even.

    Raises:
        ValueError: If the list is empty.
    """
    n = len(lst)
    if n == 0:
        raise ValueError("The list is empty")
    if n % 2 == 1:
        return lst[n // 2]
    else:
        return lst[(n // 2) - 1], lst[n // 2]
