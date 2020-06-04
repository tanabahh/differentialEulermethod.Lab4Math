import math


def f(x, y):
    return math.sin(x)


def f_true(x):
    return -math.cos(x)


def g(x, y):
    return 5/(x**2 + 2)


def g_true(x):
    return 5*math.atan(x/math.sqrt(x))/math.sqrt(x)


def z(x, y):
    return math.sin(x) - y


def z_true(x):
    return math.exp(-x) + math.sin(x)/2 - math.cos(x)/2


def s(x, y):
    return x**2 + 2*y


def s_true(x):
    return math.exp(2*x) - x^2/2 - x/2 - 1/4

