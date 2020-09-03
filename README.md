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

## What is this?

> _"Optional quote" - Johnny Appleseed_

Long desc.

## Installation

Optional notice

### via `git clone`

You can clone this repository, run `cd package_root_folder_name`, and then run `pip install .` or `pip3 install .` (or `python3 -m pip install .`).

Here's the complete installation script:

```bash
/usr/bin/git clone https://github.com/ThatXliner/package_name.git
/bin/bash cd package_root_folder_name
/usr/bin/pip3 install .
/usr/bin/python3 -m pip install .
```

or, a one-liner installation script:

```bash
/usr/bin/git clone https://github.com/ThatXliner/package_name.git && /bin/bash cd package_root_folder_name && /usr/bin/pip3 install . ; /usr/bin/python3 -m pip install .
```

**NOTE: If you don't have `pip` or `/usr/bin/pip` or `/usr/bin/pip3` and have tried `/usr/bin/python3 -m pip`, you will need to install pip. See [here](#getting-pip) to find out how to get pip.**

### via `pip install` (recommended)

You can easily install this package via `pip install package_name` (or `python3 -m pip install package_name`).

## Getting started

Only have this sub-heading if the package is an importable python module.

## Usage

```python
pass
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

[CONTRIBUTING.md](./CONTRIBUTING.md)

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

[MIT](https://choosealicense.com/licenses/mit/)
