# -*- coding: utf-8 -*-
"""Exercise 3.

Split the dataset based on the given ratio.
"""


import numpy as np


def split_data(x, y, ratio, seed):
    """split the dataset based on the split ratio."""
    # set seed
    # ***************************************************
    # INSERT YOUR CODE HERE
    # split the data based on the given ratio: TODO
    # ***************************************************
    np.random.seed(seed)
    data = np.c_[y,x]
    end_point = np.int_(ratio*len(y))
    np.random.shuffle(data)
    mask = np.random.rand(len(x)) <= ratio
    training_x = data[:end_point,1]
    training_y = data[:end_point,0]
    testing_x = data[end_point:,1]
    testing_y = data[end_point:,0]
    # ***************************************************
    # INSERT YOUR CODE HERE
    # split the data based on the given ratio: TODO
    # ***************************************************
    return training_x, training_y, testing_x, testing_y
    raise NotImplementedError
