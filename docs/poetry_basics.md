# Poetry Basics

## Installing Poetry

Poetry requires Python 2.7 or 3.5+, although Poetry 1.2 will only support Python 3.6+. It is multi-platform and the goal is to make it work equally well on Windows, Linux and OSX.

```console
python --version
```

```console
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python -
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
git commit -m "Initial commit"
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
git commit -m "Add pendulum package"
poetry help add
```

Discuss [Dependency specification](https://python-poetry.org/docs/dependency-specification/) in Poetry.

Check [pendulum version on PyPI](https://pypi.org/project/pendulum/).

```console
poetry add pendulum@2.1.2
git diff
git add poetry.lock pyproject.toml
git commit -m "Pin pendulum to 2.1.2"
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
git commit -m "Pin pytest to 6.2.4"
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
git commit -m "Add command to print current date and time for a timezone"
```

```console
poetry install
poetry shell
poetry-demo
exit
```

## Exporting the Lock File in Requirements Format

```console
poetry export
poetry export --dev
poetry export --output requirements.txt
cat requirements.txt
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
echo "dist/" >> .gitignore
git diff
git status
git add .gitignore
git commit -m "Add dist directory to .gitignore"
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
echo "poetry_demo==$(poetry version --short) \\"
echo "poetry_demo==$(poetry version --short) \\" >> requirements.txt
poetry run python -m pip hash dist/poetry_demo-0.1.0-py3-none-any.whl
poetry run python -m pip hash dist/poetry_demo-0.1.0-py3-none-any.whl | awk 'NR==2' >> requirements.txt
cat requirements.txt
git diff
git status
git add requirements.txt
git commit -m "Add requirements.txt to install project"
```

Start a new terminal and fire up a HTTP server serving the wheel:

```console
cd poetry-demo/dist
python -m http.server 8000 --bind 127.0.0.1
```

Now simulate a deployment:

```console
mkdir /tmp/deploy
cp requirements.txt /tmp/deploy
cd /tmp/deploy
ls -al
python -m venv .venv
.venv/bin/python -m pip install --find-links http://127.0.0.1:8000 --requirement requirements.txt
.venv/bin/python -m pip freeze
.venv/bin/poetry-demo
.venv/bin/python -c "from poetry_demo import main; main()"
cd -
rm -fr /tmp/deploy
```

Don't forget to stop the HTTP server in the other terminal! :wink:
