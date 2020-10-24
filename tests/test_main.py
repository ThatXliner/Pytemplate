#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# type: ignore
"""
Author: Bryan Hu .
@Bryan Hu .
Made with love by Bryan Hu .
Version: TEST
Desc: YOU SHOULD NOT USE THIS FILE. IT IS A TEST.

Modify this file to your needs.
"""

import sys
from pathlib import Path

import pytest  # noqa

import package_name

sys.path.insert(0, str(Path(Path(__file__).parent.parent / "src")))


class Test_sub_module(object):
    def test_factorial(self) -> None:
        assert package_name.sub_module.factorial(9) == 362880
        assert package_name.sub_module.factorial(0) == 1
        assert package_name.sub_module.factorial(-0) == 1
