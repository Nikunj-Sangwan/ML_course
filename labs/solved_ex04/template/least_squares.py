# -*- coding: utf-8 -*-
"""Exercise 3.

Least Square
"""

import numpy as np


def least_squares(y, tx):
    """calculate the least squares."""
    # ***************************************************
    # INSERT YOUR CODE HERE
    # least squares: TODO
    # returns optimal weights, MSE
    # ***************************************************
    w = np.linalg.solve(tx.T@tx, tx.T@y)
    return w, np.sqrt(np.mean((y-(tx@w))**2))
    raise NotImplementedError
