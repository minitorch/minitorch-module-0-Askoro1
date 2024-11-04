"""Collection of the core mathematical operators used throughout the code base."""

import math


def mul(a, b):
    return a * b


def id(x):
    return x


def add(a, b):
    return a + b


def neg(x):
    return -x


def lt(a, b):
    return a < b


def eq(a, b):
    return a == b


def max(a, b):
    if a >= b:
        return a
    else:
        return b


def is_close(a, b):
    return abs(a - b) < 1e-2


def sigmoid(x):
    if x >= 0:
        return 1.0 / (1.0 + math.exp(-x))
    else:
        return math.exp(x) / (1.0 + math.exp(x))


def relu(x):
    return max(0.0, x)


def log(x):
    return math.log(x)


def exp(x):
    return math.exp(x)


def inv(x):
    return 1.0 / x


def log_back(a, b):
    return b / a


def inv_back(a, b):
    return -b / (a**2)


def relu_back(a, b):
    if a <= 0:
        return 0
    else:
        return b


# ## Task 0.3

# Small practice library of elementary higher-order functions.

# Implement the following core functions
# - map
# - zipWith
# - reduce
#
# Use these to implement
# - negList : negate a list
# - addLists : add two lists together
# - sum: sum lists
# - prod: take the product of lists


# TODO: Implement for Task 0.3.
