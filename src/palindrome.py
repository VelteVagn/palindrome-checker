#!/usr//bin/env python3

# imports
from collections.abc import Iterable
from numbers import Integral


def int_len(x: int) -> int:
    """Finds the length, not including signs, of an integer-like."""

    # check that input is of correct type
    if not isinstance(x, Integral):
        raise TypeError(f"int_len() expected an integer, not {type(x)}")

    x = abs(x)
    l = 1  # length counter starting at 1

    # remove one integer at a time until only one is left
    while x > 9:
        x = x // 10
        l += 1

    return l


# purely mathematical solution
def palindrome(x):
    """Checks if an integer is a palindrome. Accepts iterables."""

    # iterate over iterables
    if isinstance(x, Iterable):
        return [palindrome(n) for n in x]

    # check that input is an integer-like
    if not isinstance(x, Integral):
        raise TypeError("palidrome() requires integers or iterables")
    # make sure x is positive
    if x < 0:
        x = abs(x)
    # if x is a single digit, it must be a palindrome
    if x < 10:
        return True

    l = int_len(x)  # find the length of input

    # Two-digit numbers are palindromes iff they're divisible by 11
    if l == 2:
        if x % 11 == 0:
            return True
        else:
            return False

    # find the first and last digits
    first_digit = x // (10 ** (l - 1))
    last_digit = x % 10

    # first and last digits must be equal
    if first_digit == last_digit:
        # remove the first and last digit
        next_it = x - (first_digit * (10 ** (l - 1))) - last_digit
        # when the length is one less, the 2nd digit was non-zero
        if int_len(next_it) == l - 1:
            return palindrome(next_it // 10)  # reiterate
        else:
            zeroes = l - int_len(next_it)  # find number of preceeding zeroes
            # make sure they match the number of trailing zeroes:
            for _ in range(zeroes):
                if next_it % 10 == 0:
                    next_it = next_it // 10
                else:
                    return False
            return palindrome(next_it)  # continue reccursion on success
    else:
        return False


# method using lists
def list_palindrome(x):
    """Checks if an integer is a palindrome. Accepts iterables."""

    # iterate over iterables
    if isinstance(x, Iterable):
        return [palindrome(n) for n in x]

    # check that input is an integer-like
    if not isinstance(x, Integral):
        raise TypeError("palidrome() requires integers or iterables")
    # make sure x is positive
    if x < 0:
        x = abs(x)
    # if x is a single digit, it must be a palindrome
    if x < 10:
        return True

    # create a list to be filled with digits in reversed order
    x_reverse = []
    while x != 0:
        x_reverse.append(x % 10)  # append last digit to list
        x = x // 10  # remove last digit from integer

    x_list = x_reverse.copy()  # make a new list
    x_list.reverse()  # and reverse it

    # if they're equal, return True, otherwise False
    if x_list == x_reverse:
        return True
    else:
        return False
