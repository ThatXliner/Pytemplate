#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Bryan Hu .
@Bryan Hu .
Made with love by Bryan Hu .
Version: TEST
Desc: YOU SHOULD NOT USE THIS FILE. IT IS A TEST.
"""

import pytest  # noqa

from sys import path

path.insert(0, "../src")
from package_name import example_api_func, __version__  # noqa


class TestClass(object):
    def test_example(self):
        assert __version__ == "0.1.0"
