#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Package summary.

Long description.
"""
from . import sub_module  # noqa: F401

# from .sub_module import *  # noqa

# Do the above ONLY when:

# sub_module is required to have an __all__ variable declared
# The reason for this is that the package root directory __init__.py
# should not declare an __all__ variable due to code style.
# It would make it easier to maintain: nobody wants to update the
# __init__.py every single time there is a new conponent.

# But, from sub_module import * should only be used if the
# implementation is split across files. Otherwise, we do nothing
# The reason for this is that if it makes sense to categorize
# module-level APIs into different files.
