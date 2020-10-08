#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""To setup."""
from pathlib import Path
from re import compile as re_compile

from setuptools import find_packages, setup

from package_name import (
    __author__,
    __contact__,
    __description__,
    __title__,
    __version__,
)

# The directory containing this file
HERE: Path = Path(__file__).parent

# Usable variables
USERNAME: str = "ThatXliner"  # Your Github username
PACKAGE: str = __title__  # The name of the repo
REPO = REPOSITORY = f"https://github.com/{USERNAME}/{PACKAGE}"  # type: str

# The text of the README file
README = (HERE / "README.md").read_text()
REQUIREMENTS = (HERE / "requirements.txt").read_text().split("\n")
CLASSIFIERS = [
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: Implementation :: CPython",
    "Programming Language :: Python :: Implementation :: PyPy",
    "Programming Language :: Python :: 3 :: Only",
    #     "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Development Status :: 3 - Alpha",
    "Natural Language :: English",
    "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
    # "Intended Audience :: Developers",
    # "Intended Audience :: End Users/Desktop",
    # "Intended Audience :: System Administrators",
    # "Topic :: Utilities",
]
_EMAIL_REGEX: str = r"""(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`"""
                    r"""{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5"""
                    r"""d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9]"""
                    r"""(?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])"""
                    r"""?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))"""
                    r"""\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|["""
                    r"""a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a"""
                    r"""\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"""
AUTHOR_RE = re_compile(r"(\w+ \w+) <" + _EMAIL_REGEX + ">")
setup(
    name=__title__,
    version=__version__,
    author=AUTHOR_RE.search(__author__)[1],
    author_email=__contact__,
    description=__description__,
    long_description_content_type="text/markdown",
    long_description=README,
    project_urls={
        "Source Code": REPO,
        "Tracker": f"{REPO}/issues",
    },
    packages=find_packages(exclude=["tests"], include=[f"src/{PACKAGE}"]),
    # py_modules=["path/to/the/single/file"],
    classifiers=CLASSIFIERS,
    python_requires=">=3.6",
    include_package_data=True,
    install_requires=[line for line in REQUIREMENTS if not line.startswith("#")],
    # scripts=["bin/package_name_script"],
    # entry_points={"console_scripts": ["package_name=package_name.__main__:_main"]},
    # keywords="",
)
