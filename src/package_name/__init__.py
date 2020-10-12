#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Package summary.

Long description.
"""
from typing import List

from .__main__ import *  # noqa

# We do this because we're assuming that __main__.py defines an __all__ list
# (all modules should)
# But if it doesn't, we'll specify the stuff to import

__title__: str = "package_name"  # The name of the package
__version__: str = "0.1.0"  # VERSION_BUMP_ANCHOR

# The email of the initial author
__contact__: str = "bryan.hu.2020@gmail.com"

# The initial author of this project
__author__: str = f"Bryan Hu <{__contact__}>"
# NOTE: THE FORMAT OF `__author__` SHOULD ALWAYS BE
# "FIRST LAST <EMAIL ADDRESS>"
__credits__: List[str] = []  # Other contributors
