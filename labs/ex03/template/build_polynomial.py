# -*- coding: utf-8 -*-
"""implement a polynomial basis function."""

import numpy as np


def build_poly(x, degree):
    """polynomial basis functions for input data x, for j=0 up to j=degree."""
    M = np.zeros((len(x),degree+1))
    for i in range(degree+1):
        M[:,i] = x**i
    return M
    raise NotImplementedError
