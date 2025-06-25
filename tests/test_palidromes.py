#!/usr/bin/env python3

# imports
import pytest
import random
from palindrome import palindrome, list_palindrome


@pytest.mark.parametrize(
    "integer",
    [
        1334331,
        101,
        3,  # test single-digit numbers
        676,
        13577531,  # test even-numbered integers
        230076670032,  # test numbers with 0
        -121,  # test negative numbers
        -304505403,  # test number with 0 in the middle
        100000000000001,
        8388647318947362637498137468838,  # test loooong number
    ],
)
@pytest.mark.parametrize("palin", [palindrome, list_palindrome])
def test_single_int(palin, integer):
    assert palin(integer)


@pytest.mark.parametrize(
    "iterable",
    [
        [313, 4, 1001, 56465],  # test list
        (44, 12121, 666, 2002002),  # test tuple
        range(10),  # test range
        {434: "palindrome", 10001: "also palindrome"},  # test dictionaries
    ],
)
@pytest.mark.parametrize("palin", [palindrome, list_palindrome])
def test_iterables(palin, iterable):
    assert all(palin(iterable))


@pytest.mark.parametrize("palin", [palindrome, list_palindrome])
def test_edge_cases(palin):
    assert palin([]) == []  # test empty list
    assert palin([232, [1, 975579, 32]]) == [True, [True, True, False]]
    with pytest.raises(TypeError):
        palin()  # empty input


@pytest.mark.parametrize(
    "integer",
    [
        22222212222,  # almost palindrome
        3898300000,  # test trailing zeroes
        38492838,
        393383,
    ],
)
@pytest.mark.parametrize("palin", [palindrome, list_palindrome])
def test_non_palindrome_int(palin, integer):
    assert not palin(integer)


@pytest.mark.parametrize(
    "iterable",
    [
        [23, 45, 54, 32],  # "palindromic" list
        [676, 998, 414, 998, 676],  # another "palindromic" list
        (838, 11111, 10801, 123282321, 6766, 22322),  # mostly palindromes
    ],
)
@pytest.mark.parametrize("palin", [palindrome, list_palindrome])
def test_non_palindrome_iterable(palin, iterable):
    assert not all(palin(iterable))


@pytest.mark.parametrize(
    "value",
    [
        3.4,  # float
        None,  # None
        99.99,  # palindrome float
        [1, 2, 3, 4, 8 / 7],  # list with invalid value
    ],
)
@pytest.mark.parametrize("palin", [palindrome, list_palindrome])
def test_fails(palin, value):
    with pytest.raises(TypeError):
        palin(value)


def gen_palindrome():
    """Generate a random palindrome of length 1-23 for the upcoming test."""
    beginning = str(random.randint(0, 99999999999))  # generate the first part
    end = beginning[::-1]  # generate the second part
    if random.randint(0, 1) == 1:
        middle = str(random.randint(0, 9))  # sometimes generate a middle
    else:
        middle = ""
    return int(f"{beginning}{middle}{end}")  # return the palindrome as an int


@pytest.mark.parametrize("palin", [palindrome, list_palindrome])
def test_random(palin):
    for _ in range(30):
        p = gen_palindrome()
        assert palindrome(p)
