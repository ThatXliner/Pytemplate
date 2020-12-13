#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# type: ignore
# pylint: disable=C,R0201,R0903
"""Unit tests"""
from src import package_name


class Test_sub_module:
    def test_factorial(self) -> None:
        assert package_name.sub_module.factorial(9) == 362880
        assert package_name.sub_module.factorial(0) == 1
        assert package_name.sub_module.factorial(-0) == 1
