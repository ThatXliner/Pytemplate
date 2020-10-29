#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Initial author: Bryan Hu .

@ThatXliner .

Version: v0.1.0

Short summary

Long description
"""
import functools
import operator
from typing import Iterable, TypeVar

AnyNum = TypeVar("AnyNum", int, float, complex)
__all__ = ["factorial", "multiply_all"]


def factorial(number: int) -> int:
    """A function that calculates the factorial of a number.

    Parameters
    ----------
    number : int
        The :arg:`number` to calculate the factorial of.

    Returns
    -------
    int
        The factorial of the number.
    """
    if number < 1:
        return 1
    return number * factorial(number - 1)


def multiply_all(some_iter: Iterable[AnyNum]) -> AnyNum:
    """Multiplies all elements in the given iterable.

    Parameters
    ----------
    some_iter : Iterable[AnyNum]
        The iterable whose elements will be multiplied together.

    Returns
    -------
    AnyNum
        The product of all the elements in the given iterable.

    """
    return functools.reduce(operator.mul, some_iter)  # type: ignore
