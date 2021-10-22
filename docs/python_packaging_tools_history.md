# A Brief History of Python Packaging Tools

For a complete list of the most relevant projects in the space of Python installation and packaging see [Project Summaries](https://packaging.python.org/key_projects/), which is part of the [Python Packaging User Guide](https://packaging.python.org/).

## distutils

[distutils](https://docs.python.org/3/library/distutils.html#module-distutils) is the original Python packaging system, added to the standard library in Python 2.0 which has been released in 2001.

No support for declaring project dependencies and entry points. In Python 3.10 and 3.11 usage of distutils is deprecated, it will be removed in 3.12 (see [PEP 632](https://www.python.org/dev/peps/pep-0632/)).

## setuptools

[setuptools](https://pypi.org/project/setuptools) (which includes the now deprecated [easy_install](https://setuptools.readthedocs.io/en/latest/deprecated/easy_install.html)) is a collection of enhancements to distutils that allow you to more easily build and distribute Python distributions, especially ones that have dependencies on other packages. The project had its first release in 2006.

## distribute

[distribute](https://pypi.org/project/distribute) is a fork of setuptools that was merged back into setuptools (in v0.7, released in 2013).

## virtualenv

[virtualenv](https://pypi.org/project/virtualenv/) is a tool to create isolated Python environments, first released in 2007. Since Python 3.3, a subset of it has been integrated into the standard library under the [venv module](https://docs.python.org/3/library/venv.html).

## pip

[pip](https://pypi.org/project/pip/) is the most popular tool for installing Python packages, and the one included with modern versions of Python. It was started in 2008 as a replacement for easy_install.

## wheel

[wheel](https://pypi.org/project/wheel) is the reference implementation of the Python wheel packaging standard, as defined in [PEP 427](https://www.python.org/dev/peps/pep-0427/) which was started in 2012. A wheel may be installed by simply unpacking into site-packages, making it easier to install than sdist.

## pip-tools

[pip-tools](https://pypi.org/project/pip-tools/) is a set of command line tools to manage pinned dependencies and ensure builds are predictable and deterministic. First release was in September 2012.

## Conda

[Conda](https://conda.io/) is the package management tool for Anaconda Python installations, first released in November 2012. Anaconda Python is a distribution from Anaconda, Inc specifically aimed at the scientific community, and in particular on Windows where the installation of binary extensions is often difficult. Conda does not install packages from PyPI and can install only from the official Anaconda repositories, or [anaconda.org](https://anaconda.org/), or a local (e.g. intranet) package server.

## twine

[twine](https://pypi.org/project/twine) is the primary tool developers use to upload packages to the Python Package Index or other Python package indexes, first released in 2013. It’s fast and secure, it’s maintained, and it reliably works.

## PEP 440

[PEP 440](https://www.python.org/dev/peps/pep-0440/) describes a scheme for identifying versions of Python software distributions, and declaring dependencies on particular versions. Created in March 2013, accepted in August 2014.

## flit

[flit](https://pypi.org/project/flit) provides a simple way to build and upload pure Python packages and modules to PyPI and was first released in 2015.

## PEP 517

[PEP 517](https://www.python.org/dev/peps/pep-0517/) describes a build-system independent format for source trees. Created in September 2015, accepted in September 2017.

## PEP 508

[PEP 508](https://www.python.org/dev/peps/pep-0508/) specifies the language used to describe dependencies for packages. It draws a border at the edge of describing a single dependency - the different sorts of dependencies and when they should be installed is a higher level problem. Created and accepted in November 2015.

## Pipfile

[Pipfile](https://github.com/pypa/pipfile) and its sister `Pipfile.lock` are a replacement for the existing standard pip's `requirements.txt` file started in 2016. The project is under active design and development.

## Pipenv

[Pipenv](https://pypi.org/project/pipenv), first released in January 2017, harnesses Pipfile, pip, and virtualenv into one single toolchain, but has been less maintained since late 2018.

## pipx

[pipx](https://pypi.org/project/pipx/) is a tool to install and run Python applications in isolated environments (using virtual environments), first released in July 2017.

## Poetry

[Poetry](https://python-poetry.org/), first released in 2018, is a command-line tool to handle dependency installation and isolation as well as building and packaging of Python packages. It provides its own dependency resolver.

Next: [Poetry Basics](poetry_basics.md)
