#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Package summary.

Long description.
"""
from typing import List


# from .sub_module import *  # noqa

# Do the above ONLY when:

# sub_module is required to have an __all__ variable declared
# The reason for this is that the package root directory __init__.py
# should not declare an __all__ variable due to code style.
# It would make it easier to maintain: nobody wants to update the
# __init__.py every single time there is a new conponent.

# BECAUSE:

# But, from sub_module import * should only be used if the
# implementation is split across files. Otherwise, we do nothing
# The reason for this is that if it makes sense to categorize
# module-level APIs into different files.

__title__: str = "package_name"  # The name of the package
__version__: str = "0.1.0"  # VERSION_BUMP_ANCHOR

# The email of the initial author
__contact__: str = "bryan.hu.2020@gmail.com"

# The initial author of this project
__author__: str = f"Bryan Hu <{__contact__}>"
# NOTE: THE FORMAT OF `__author__` SHOULD ALWAYS BE
# "FIRST LAST <EMAIL ADDRESS>"
__credits__: List[str] = []  # Other contributors
