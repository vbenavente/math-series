# -*- coding: utf-8 -*-
import pytest


FIBONACCI_TABLE = [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 5),
    (6, 8),
    (7, 13)
    ]

LUCAS_TABLE = [
    (0, 2),
    (1, 1),
    (2, 3),
    (3, 4),
    (4, 7)
]

SUM_SERIES_TABLE = [
    (0, 0, 1, 0),
    (1, 5, 10, 10),
    (2, 8, 89, 97),
    (3, 19, 5, 29),
    (4, 45, 3, 99)
]


@pytest.mark.parametrize('n, result', FIBONACCI_TABLE)
def test_fibonacci(n, result):
    from series import fibonacci
    assert fibonacci(n) == result


@pytest.mark.parametrize('n, result', LUCAS_TABLE)
def test_lucas(n, result):
    from series import lucas
    assert lucas(n) == result


@pytest.mark.parametrize('n, x, y, result', SUM_SERIES_TABLE)
def test_sum_series(n, x, y, result):
    from series import sum_series
    assert sum_series(n, x, y) == result
