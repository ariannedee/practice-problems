"""
Return whether the given number is even (True) or odd (False)
"""
from test_helper import equals


def is_even(number):
    pass


equals(is_even(0), True)
equals(is_even(2), True)
equals(is_even(23456), True)
equals(is_even(-100), True)
equals(is_even(1), False)
equals(is_even(-1), False)
equals(is_even(123), False)
equals(is_even(1.2), False)
