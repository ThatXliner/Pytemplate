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

from pathlib import Path
from sys import path

import pytest  # noqa

path.insert(0, str(Path(Path(Path(__file__).parent).parent / "src")))
from package_name import __version__  # noqa


class TestClass(object):
    def test_example(self):
        assert __version__ == "0.1.0"
