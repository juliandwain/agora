# -*- coding: utf-8 -*-

from typing import Union

import numpy as np

__all__ = [
    "get_neighbors",
]


# ------------------------------------------------------------------------------------------------------------
# helper functions for the percolation module

def get_neighbors(current: tuple,
                  distance: Union[int, float],
                  x_limit: tuple,
                  y_limit: tuple) -> np.ndarray:
    """Get all direct neighbors of an infected person.

    Parameters
    ----------
    current : tuple
        The current node as (x, y) coordinates.
    distance : int or float
        The distance between two nodes.
    x_limit : tuple
        The limit in x direction as (x_min, x_max).
    y_limit : tuple
        The limit in y direction as (y_min, y_max).

    Returns
    -------
    np.ndarray
        The neighboring coordinates as array in the order top, left, bottom, right. If a node does not have
        all neighbors, the corresponding coordinate is skipped in the order, i.e. top, bottom, left if
        the node is at the left end at x_min.

    """

    x, y = current
    x_min, x_max, y_min, y_max = *x_limit, *y_limit
    if x < x_min or x > x_max:
        raise AssertionError("The node is not within the range.")
    if y < y_min or y > y_max:
        raise AssertionError("The node is not within the range.")
    if x == x_min:
        if y == y_min:
            top = np.array([x, y + distance], dtype=float)
            right = np.array([x + distance, y], dtype=float)
            return np.array([top, right])
        elif y == y_max:
            bottom = np.array([x, y - distance], dtype=float)
            right = np.array([x + distance, y], dtype=float)
            return np.array([bottom, right])
        else:
            top = np.array([x, y + distance], dtype=float)
            bottom = np.array([x, y - distance], dtype=float)
            right = np.array([x + distance, y], dtype=float)
            return np.array([top, bottom, right])
    elif x == x_max:
        if y == y_min:
            top = np.array([x, y + distance], dtype=float)
            left = np.array([x - distance, y], dtype=float)
            return np.array([top, left])
        elif y == y_max:
            left = np.array([x - distance, y], dtype=float)
            bottom = np.array([x, y - distance], dtype=float)
            return np.array([left, bottom])
        else:
            top = np.array([x, y + distance], dtype=float)
            left = np.array([x - distance, y], dtype=float)
            bottom = np.array([x, y - distance], dtype=float)
            return np.array([top, left, bottom])
    else:
        if y == y_min:
            top = np.array([x, y + distance], dtype=float)
            left = np.array([x - distance, y], dtype=float)
            right = np.array([x + distance, y], dtype=float)
            return np.array([top, left, right])
        elif y == y_max:
            left = np.array([x - distance, y], dtype=float)
            bottom = np.array([x, y - distance], dtype=float)
            right = np.array([x + distance, y], dtype=float)
            return np.array([left, bottom, right])
        else:
            top = np.array([x, y + distance], dtype=float)
            left = np.array([x - distance, y], dtype=float)
            bottom = np.array([x, y - distance], dtype=float)
            right = np.array([x + distance, y], dtype=float)
            return np.array([top, left, bottom, right])
