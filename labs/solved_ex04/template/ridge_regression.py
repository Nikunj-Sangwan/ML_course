# -*- coding: utf-8 -*-
"""Exercise 3.

Ridge Regression
"""

import numpy as np


def ridge_regression(y, tx, lambda_):
    """implement ridge regression."""
    # ***************************************************
    # INSERT YOUR CODE HERE
    # ridge regression: TODO
    # ***************************************************
    w = np.linalg.solve(( tx.T@tx + 2*len(y)*lambda_*np.identity(len(tx[0,:])) ), tx.T@y)
    return w
    raise NotImplementedError
