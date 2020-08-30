#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""To setup."""
from pathlib import Path
from setuptools import setup, find_packages
from package_name import __version__

# The directory containing this file
HERE = Path(__file__).parent

PACKAGE = "package_name"
USERNAME = "ThatXliner"
EMAIL = "bryan.hu.2020@gmail.com"

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
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Development Status :: 3 - Alpha",
    "Natural Language :: English",
    # "Intended Audience :: Developers",
    # "Intended Audience :: End Users/Desktop",
    # "Intended Audience :: System Administrators",
    # "Topic :: Utilities",
]
setup(
    name=PACKAGE,
    version=__version__,
    author="Bryan Hu",
    author_email=EMAIL,
    description="Short description",
    long_description=README,
    long_description_content_type="text/markdown",
    project_urls={
        "Source Code": f"https://github.com/{USERNAME}/{PACKAGE}",
        "Tracker": f"https://github.com/{USERNAME}/{PACKAGE}/issues",
    },
    packages=find_packages(exclude=["tests"], include=[f"src/{PACKAGE}"]),
    classifiers=CLASSIFIERS,
    python_requires=">=3.6",
    include_package_data=True,
    install_requires=[line for line in REQUIREMENTS if not line.startswith("#")],
    # scripts=["bin/package_name_script"],
    # entry_points={"console_scripts": ["package_name=package_name.__main__:_main"]},
    # keywords="",
)