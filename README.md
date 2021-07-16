# Poetry Workshop

## A Brief History of Python Packaging Tools

For a complete list of the most relevant projects in the space of Python installation and packaging see [Project Summaries](https://packaging.python.org/key_projects/), which is part of the [Python Packaging User Guide](https://packaging.python.org/).

### distutils

[distutils](https://docs.python.org/3/library/distutils.html#module-distutils) is the original Python packaging system, added to the standard library in Python 2.0 which has been released in 2001.

No support for declaring project dependencies and entry points, so direct usage of distutils is now actively discouraged.

### setuptools

[setuptools](https://pypi.org/project/setuptools) (which includes the now deprecated [easy_install](https://setuptools.readthedocs.io/en/latest/deprecated/easy_install.html)) is a collection of enhancements to distutils that allow you to more easily build and distribute Python distributions, especially ones that have dependencies on other packages. The project had its first release in 2006.

### distribute

[distribute](https://pypi.org/project/distribute) is a fork of setuptools that was merged back into setuptools (in v0.7, released in 2013).

### virtualenv

[virtualenv](https://pypi.org/project/virtualenv/) is a tool to create isolated Python environments, first released in 2007. Since Python 3.3, a subset of it has been integrated into the standard library under the [venv module](https://docs.python.org/3/library/venv.html).

### pip

[pip](https://pypi.org/project/pip/) is the most popular tool for installing Python packages, and the one included with modern versions of Python. It was started in 2008 as a replacement for easy_install.

### wheel

[wheel](https://pypi.org/project/wheel) is the reference implementation of the Python wheel packaging standard, as defined in [PEP 427](https://www.python.org/dev/peps/pep-0427/) which was started in 2012. A wheel may be installed by simply unpacking into site-packages, making it easier to install than sdist.

### pip-tools

[pip-tools](https://pypi.org/project/pip-tools/) is a set of command line tools to manage pinned dependencies and ensure builds are predictable and deterministic. First release was in September 2012.

### Conda

[Conda](https://conda.io/) is the package management tool for Anaconda Python installations, first released in November 2012. Anaconda Python is a distribution from Anaconda, Inc specifically aimed at the scientific community, and in particular on Windows where the installation of binary extensions is often difficult. Conda does not install packages from PyPI and can install only from the official Anaconda repositories, or [anaconda.org](https://anaconda.org/), or a local (e.g. intranet) package server.

### twine

[twine](https://pypi.org/project/twine) is the primary tool developers use to upload packages to the Python Package Index or other Python package indexes, first released in 2013. It’s fast and secure, it’s maintained, and it reliably works.

### PEP 440

[PEP 440](https://www.python.org/dev/peps/pep-0440/) describes a scheme for identifying versions of Python software distributions, and declaring dependencies on particular versions. Created in March 2013, accepted in August 2014.

### flit

[flit](https://pypi.org/project/flit) provides a simple way to build and upload pure Python packages and modules to PyPI and was first released in 2015.

### PEP 517

[PEP 517](https://www.python.org/dev/peps/pep-0517/) describes a build-system independent format for source trees. Created in September 2015, accepted in September 2017.

### PEP 508

[PEP 508](https://www.python.org/dev/peps/pep-0508/) specifies the language used to describe dependencies for packages. It draws a border at the edge of describing a single dependency - the different sorts of dependencies and when they should be installed is a higher level problem. Created and accepted in November 2015.

### Pipfile

[Pipfile](https://github.com/pypa/pipfile) and its sister `Pipfile.lock` are a replacement for the existing standard pip's `requirements.txt` file started in 2016. The project is under active design and development.

### Pipenv

[Pipenv](https://pypi.org/project/pipenv), first released in January 2017, harnesses Pipfile, pip, and virtualenv into one single toolchain, but has been less maintained since late 2018.

### pipx

[pipx](https://pypi.org/project/pipx/) is a tool to install and run Python applications in isolated environments (using virtual environments), first released in July 2017.

### Poetry

[Poetry](https://python-poetry.org/), first released in 2018, is a command-line tool to handle dependency installation and isolation as well as building and packaging of Python packages. It provides its own dependency resolver.

## Installing Poetry

Poetry requires Python 2.7 or 3.5+, although Poetry 1.2 will only support Python 3.6+. It is multi-platform and the goal is to make it work equally well on Windows, Linux and OSX.

```console
python --version
```

```console
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
```

```console
poetry --version
```

For installing a specific version, Windows installation instructions and alternative installation methods see [Poetry Introduction](https://python-poetry.org/docs/).

## Creating a New Project with Poetry

```console
poetry new --src poetry-demo
poetry help new
```

```console
poetry-demo
├── pyproject.toml
├── README.rst
├── src
│  └── poetry_demo
│     └── __init__.py
└── tests
   ├── __init__.py
   └── test_poetry_demo.py
```

```console
cd poetry-demo
cat pyproject.toml
git init
echo "__pycache__" > .gitignore
git add .
git commit
```

See [`pyproject.toml` file documentation](https://python-poetry.org/docs/pyproject/) for all options.

```console
poetry help init

```

## Using the Virtual Environment

```console
poetry install
poetry help install
poetry env info
poetry help env
poetry run python -m pytest
poetry help run
```

The virtual environment will either be created in a global cache directory or inside the project’s root directory, depending on the value of the [`virtualenvs.in-project` setting](https://python-poetry.org/docs/configuration/#virtualenvsin-project). It's also possible to configure Poetry to not create the virtual environment at all using the [`virtualenvs.create` setting](https://python-poetry.org/docs/configuration/#virtualenvscreate).

```console
poetry shell
which python
python -m pytest
exit
poetry help shell
```

## Installing the First Dependency

```console
poetry add pendulum
git diff
git status
git add poetry.lock pyproject.toml
git commit
poetry help add
```

Discuss [Dependency specification](https://python-poetry.org/docs/dependency-specification/) in Poetry.

Check [pendulum version on PyPI](https://pypi.org/project/pendulum/).

```console
poetry add pendulum@2.1.2
git diff
git add poetry.lock pyproject.toml
git commit
```

## Updating Dependencies

```console
poetry show
poetry show pytest
poetry help show
```

```console
poetry update --dry-run pytest
poetry help update
```

Check [pytest version on PyPI](https://pypi.org/project/pytest/).

```console
poetry add --dev pytest@6.2.4
poetry run python -m pytest
git diff
git add poetry.lock pyproject.toml
git commit
```

## Adding a Feature

```diff
diff --git a/poetry_demo/__init__.py b/poetry_demo/__init__.py
index b794fd4..8cf17cf 100644
--- a/src/poetry_demo/__init__.py
+++ b/src/poetry_demo/__init__.py
@@ -1 +1,13 @@
 __version__ = '0.1.0'
+
+import pendulum
+
+
+def main():
+    now = pendulum.now("Europe/Paris")
+    print(now)
+    print(now.in_timezone("America/Toronto"))
+
+
+if "__name__" == "__main__":
+    main()
diff --git a/pyproject.toml b/pyproject.toml
index e502597..93f08be 100644
--- a/pyproject.toml
+++ b/pyproject.toml
@@ -11,6 +11,9 @@ pendulum = "2.1.2"
 [tool.poetry.dev-dependencies]
 pytest = "6.2.4"
 
+[tool.poetry.scripts]
+poetry-demo = "poetry_demo:main"
+
 [build-system]
 requires = ["poetry-core>=1.0.0"]
 build-backend = "poetry.core.masonry.api"
```

```console
poetry run poetry-demo
git diff
git add src/poetry_demo/__init__.py pyproject.toml
git commit
```

## Exporting the Lock File in Requirements Format

```console
poetry export
poetry export --dev
poetry export --output requirements.txt
rm requirements.txt
poetry help export
```

## Building Source and Wheels Archives

```console
poetry build
ls -al dist
rm -fr dist
poetry build --format wheel
ls -al dist
poetry help build
poetry help publish
```

## Inspecting the Wheel

```console
cd dist
unzip poetry_demo-0.1.0-py3-none-any.whl
cat poetry_demo/__init__.py
cat poetry_demo-0.1.0.dist-info/METADATA
cat poetry_demo-0.1.0.dist-info/entry_points.txt
rm -fr poetry_demo poetry_demo-0.1.0.dist-info
cd -
```

## Installing the Project with All Dependencies Pinned

```console
poetry export --output requirements.txt
echo "poetry_demo==$(poetry version --short) \\" >> requirements.txt
poetry run python -m pip hash dist/poetry_demo-0.1.0-py3-none-any.whl | awk 'NR==2' >> requirements.txt
cat requirements.txt
python -m venv .venv
.venv/bin/python -m pip install --find-links dist --requirement requirements.txt
.venv/bin/python -m pip freeze
.venv/bin/poetry-demo
```
