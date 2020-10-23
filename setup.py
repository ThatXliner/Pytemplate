#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# type: ignore
"""To setup."""

from pathlib import Path

import setuptools

try:
    from src.package_name import __author__, __contact__, __version__
except ModuleNotFoundError:  # package_name imports a dependancy which is imported in the __init__.py
    try:
        import regex as re
    except ModuleNotFoundError:
        import re

        VERSION_RE, AUTHOR_RE, CONTACT_RE = (
            f'__{type}__ = "(.*)"' for type in ["version", "author", "contact"]
        )

        (__version__,) = re.findall(
            VERSION_RE, open("src/package_name/__init__.py").read()
        )
        (__author__,) = re.findall(
            AUTHOR_RE, open("src/package_name/__init__.py").read()
        )
        (__contact__,) = re.findall(
            CONTACT_RE, open("src/package_name/__init__.py").read()
        )

# The directory containing this file
HERE = Path(__file__).parent

# Usable variables
USERNAME = "ThatXliner"  # Your Github username
PACKAGE = "Pytemplate"  # The name of the repo
REPO = f"https://github.com/{USERNAME}/{PACKAGE}"

# The text of the README file
README = (HERE / "README.md").read_text()
REQUIREMENTS = (HERE / "requirements.txt").read_text().split("\n")
# Pinned (i.e. requirements for pytest) should be in pin-req.txt
DESC = "Short description shown on Pypi."

CLASSIFIERS = [
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: Implementation :: CPython",
    "Programming Language :: Python :: Implementation :: PyPy",  # Optional support
    "Programming Language :: Python :: 3 :: Only",
    # "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Development Status :: 3 - Alpha",
    "Natural Language :: English",
    "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
    # "Intended Audience :: Developers",
    # "Intended Audience :: End Users/Desktop",
    # "Intended Audience :: System Administrators",
    # "Topic :: Utilities",
]

setuptools.setup(
    name="some_package_name_avalible_on_pypi",
    version=__version__,
    author=__author__,
    author_email=__contact__,
    license="GNU GPLv3",
    description=DESC,
    long_description_content_type="text/markdown",
    long_description=README,
    project_urls={
        "Source Code": REPO,
        "Tracker": f"{REPO}/issues",
        "Say Thanks!": f"https://saythanks.io/to/{__contact__}",  # If possible
        "Travis CI": f"https://travis-ci.com/github/{USERNAME}/{PACKAGE}",
    },
    url=REPO,  # Homepage
    packages=setuptools.find_packages(exclude=["tests"], where="src"),
    # replace where="src" with include=["path/to/pkg_dir"]
    # if you have packages/modules elsewhere (you shouldn't)
    package_dir={"": "src"},
    classifiers=CLASSIFIERS,
    setup_requires=[
        "wheel",
        "setuptools",
    ],  # or flit/hatch if you use them... see ISSUE#10
    python_requires=">=3.6",  # This project supports python >=3.6 < 4
    include_package_data=True,  # To include paths specified in MANIFEST.ini
    install_requires=[line for line in REQUIREMENTS if not line.startswith("#")],
    # py_modules=["path/to/the/single/file"],
    # scripts=[os.listdir(str(Path("bin")))],  # Recommended to use entry_points instead
    # entry_points={"console_scripts": ["package_name=package_name.__main__:_main"]},
    # keywords="",
)
