#!/usr/bin/env python3

# imports
import pytest
from palindrome import int_len
import random


@pytest.mark.parametrize(
    "integer, length",
    [
        (28394, 5),
        (241, 3),
        (0, 1),
        (-392, 3),
        (1234567890, 10),
        (10**8, 9),
    ],
)
def test_integers(integer, length):
    assert int_len(integer) == length


@pytest.mark.parametrize(
    "value",
    [
        1.0,
        [4, 3, 2],
        (8,),
        None,
        {"d": 3},
        "409",
    ],
)
def test_types(value):
    with pytest.raises(TypeError):
        int_len(value)


def test_random():
    for i in range(30):
        length = random.randint(1, 100)
        n = str(random.randint(1, 9))
        for _ in range(length - 1):
            n += str(random.randint(0, 9))
        n = int(n)
        assert int_len(n) == length
