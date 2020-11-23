# Package_name

Short description.

<!-- TOC depthFrom:1 depthTo:3 withLinks:1 updateOnSave:1 orderedList:0 -->

- [Package_name](#packagename)
	- [What is this?](#what-is-this)
	- [Installation](#installation)
		- [via `git clone`](#via-git-clone)
		- [via `pip install` (recommended)](#via-pip-install-recommended)
	- [Getting started](#getting-started)
	- [Usage](#usage)
	- [Contributing](#contributing)
	- [Help](#help)
		- [FAQ](#faq)
		- [Getting pip](#getting-pip)
	- [License](#license)

<!-- /TOC -->
<p align="center">
	<a href="https://github.com/{{ cookiecutter.username }}/{{ cookiecutter.repo_name }}/actions?query=workflow%3APythonCI">
		<img src="https://github.com/{{ cookiecutter.username }}/{{ cookiecutter.repo_name }}/workflows/PythonCI/badge.svg" alt="PythonCI"></a>
	<a href="https://codecov.io/gh/{{ cookiecutter.username }}/{{ cookiecutter.repo_name }}">
		<img src="https://codecov.io/gh/{{ cookiecutter.username }}/{{ cookiecutter.repo_name }}/branch/master/graph/badge.svg" alt="codecov"></a>
	<a href="https://saythanks.io/to/{{ cookiecutter.email }}">
		<img src="https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg" alt="Say Thanks!"></a>
	<a href="https://github.com/PyCQA/bandit">
		<img src="https://img.shields.io/badge/security-bandit-yellow.svg" alt="security: bandit"></a>
	<a href="https://github.com/psf/black">
		<img src="https://img.shields.io/badge/code%20style-black-000000.svg" alt="Code style: black"></a>
	<a href="https://gitmoji.carloscuesta.me">
		<img src="https://img.shields.io/badge/gitmoji-%20😜%20😍-FFDD67.svg?style=flat-square" alt="Gitmoji">
	</a>
</p>



## What is this?

> _"Optional quote" - Johnny Appleseed_

Long desc.

## Installation

Optional notice

**NOTE: If you don't have `pip` or `/usr/bin/pip` or `/usr/bin/pip3` (and have tried `/usr/bin/python3 -m pip`), you will need to install pip. See [here](#getting-pip) to find out how to get pip.**

### via `pip install` (recommended)

You can easily install this package via `pip install {{ cookiecutter.pypi_name }}` (or `python3 -m pip install {{ cookiecutter.pypi_name }}`).

## Getting started

Only have this sub-heading if the package is an importable python module.

## Usage

```python
pass
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

[CONTRIBUTING.md](https://github.com/{{ cookiecutter.username }}/{{ cookiecutter.repo_name }}/blob/master/CONTRIBUTING.md)

## Help

### FAQ

No questions were asked.

### Getting pip

This project supports python 3.6 and higher. To install pip for python 3.6 (or higher) execute the following command in your shell (replace `python3` with your python executable):

```bash
python3 -m ensurepip --upgrade
```

OR, as a last resort:

```bash
{/usr/bin/curl https://bootstrap.pypa.io/get-pip.py | /usr/bin/python3} || {wget https://bootstrap.pypa.io/get-pip.py | /usr/bin/python3} ||  {/usr/bin/curl https://bootstrap.pypa.io/get-pip.py | /usr/bin/python} ||  {wget https://bootstrap.pypa.io/get-pip.py | /usr/bin/python}
```


## License

[GNU GPL v3.0](https://choosealicense.com/licenses/gpl-3.0/) unless noted otherwise. If you want to use this code for proprietary use, [contact me](https://github.com/{{ cookiecutter.username }}/{{ cookiecutter.repo_name }}/blob/master/CONTRIBUTING.md#owner-{{ cookiecutter.username.lower().replace('(', '').replace(')', '') }}-{{ cookiecutter.real_name.lower().replace(" ", "-") }})
