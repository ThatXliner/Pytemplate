#!/usr/bin/env python3
# -*- coding: utf-8 -*-
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

sys.path.insert(0, str(Path(Path(Path(__file__).parent).parent / "src")))
import package_name


class TestClass(object):
    def test_factorial(self) -> None:
        assert package_name.factorial(9) == 362880
        assert package_name.factorial(0) == 1
        assert package_name.factorial(-0) == 1
