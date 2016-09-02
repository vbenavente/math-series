# -*- coding: utf-8 -*-


def fibonacci(n):
    """Provide the nth value of the fibonacci series."""
    num1 = 0
    num2 = 1
    for i in range(0, n):
        total = num1 + num2
        num1 = num2
        num2 = total
    return num1


def lucas(n):
    """Provide the nth value of the lucas series."""
    num1 = 2
    num2 = 1
    for i in range(0, n):
        total = num1 + num2
        num1 = num2
        num2 = total
    return num1


def sum_series(n, x=0, y=1):
    """Provide the nth number of a sum_series."""
    num1 = x
    num2 = y
    for i in range(0, n):
        total = num1 + num2
        num1 = num2
        num2 = total
    return num1


if __name__ == "__main__":
    print("This module defines functions that implement mathematical")
    print("series, to include fibonacci(n), lucas(n), sum_series(n)")
    print("each returns the nth value of its respective series")
