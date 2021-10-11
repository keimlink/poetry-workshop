# Using Poetry with Docker

This chapter shows how to build a Docker image for different application stages using [multi-stage builds].

## Creating a `Dockerfile` for Poetry

```Dockerfile
FROM python:3.9.7@sha256:09e73c4e10e0558ddbcbf4d1d758d041a4d484585768af1e6f1d3601a3488649 AS python-poetry

ENV POETRY_VERSION=1.1.11
ENV GET_POETRY_URL=https://raw.githubusercontent.com/python-poetry/poetry/656c71d46f5cd35ac7996b00c631e5056c883b55/install-poetry.py
ENV GET_POETRY_SHA256=e8c7f91d5bbf4d0795919cd062eafbb350bec0c7579cb61d05c2112f224935a2

RUN wget "$GET_POETRY_URL" \
    && echo "$GET_POETRY_SHA256 install-poetry.py" | sha256sum --check --strict - \
    && python install-poetry.py \
    && rm -f install-poetry.py \
    && echo 'export PATH="$PATH:$HOME/.local/bin"' >> $HOME/.bashrc

WORKDIR /usr/local/src

SHELL ["bash", "--login", "-c"]

ENTRYPOINT ["bash", "--login", "-c"]

CMD ["poetry"]
```

```console
git add Dockerfile
git commit -m "Add Dockerfile with Poetry stage"
```

### Obtaining the Checksum

```console
docker run -it --rm python:3.9.7 bash -c 'curl https://raw.githubusercontent.com/python-poetry/poetry/656c71d46f5cd35ac7996b00c631e5056c883b55/install-poetry.py | sha256sum'
```

### Building and Running the Poetry Docker Image

```console
docker build --tag poetry-demo-poetry --target python-poetry .
docker images poetry-demo-poetry
docker run -it --rm poetry-demo-poetry
docker run -it --rm poetry-demo-poetry 'poetry about'
docker run -it --rm poetry-demo-poetry bash
```

## Extending the `Dockerfile` for Development

```Dockerfile
diff --git a/Dockerfile b/Dockerfile
index 0f7a456..bb5963e 100644
--- a/Dockerfile
+++ b/Dockerfile
@@ -17,3 +17,19 @@ SHELL ["bash", "--login", "-c"]
 ENTRYPOINT ["bash", "--login", "-c"]
 
 CMD ["poetry"]
+
+FROM python-poetry AS develop
+
+WORKDIR /usr/local/src/poetry-demo
+
+COPY poetry.lock pyproject.toml ./
+
+COPY src src
+
+RUN poetry install
+
+ENV PYTHONUNBUFFERED=True
+
+VOLUME /usr/local/src/poetry-demo
+
+CMD ["poetry run poetry-demo"]
```

```console
git diff
git add Dockerfile
git commit -m "Add develop stage to Dockerfile"
```

### Building and Running the Development Docker Image

```console
docker build --tag poetry-demo-develop --target develop .
docker images poetry-demo-develop
docker run -it --rm -v "$(pwd):/usr/local/src/poetry-demo" poetry-demo-develop
docker run -it --rm -v "$(pwd):/usr/local/src/poetry-demo" poetry-demo-develop \
    'poetry run poetry-demo -tz Asia/Ulaanbaatar'
```

## Extending the `Dockerfile` for Production

```Dockerfile
diff --git a/src/poetry-demo/Dockerfile b/src/poetry-demo/Dockerfile
index 6043828..90ed580 100644
--- a/src/poetry-demo/Dockerfile
+++ b/src/poetry-demo/Dockerfile
@@ -33,3 +33,36 @@ ENV PYTHONUNBUFFERED=True
 VOLUME /usr/local/src/poetry-demo
 
 CMD ["poetry run poetry-demo"]
+
+FROM develop AS build
+
+RUN poetry build --format wheel \
+    && poetry export --output requirements.txt \
+    && echo "poetry_demo==$(poetry version --short) \\" >> requirements.txt \
+    && poetry run python -m pip hash dist/poetry_demo*.whl | awk 'NR==2' >> requirements.txt
+
+FROM python:3.9.7@sha256:09e73c4e10e0558ddbcbf4d1d758d041a4d484585768af1e6f1d3601a3488649
+
+ARG GID=1000
+ARG UID=1000
+
+ENV PIP_DISABLE_PIP_VERSION_CHECK=True
+ENV PIP_NO_CACHE_DIR=False
+ENV PYTHONUNBUFFERED=True
+
+WORKDIR /usr/local/src
+
+COPY --from=build /usr/local/src/poetry-demo/dist/poetry_demo*.whl ./
+COPY --from=build /usr/local/src/poetry-demo/requirements.txt ./
+
+RUN python -m venv poetry-demo \
+    && poetry-demo/bin/python -m pip install --find-links . --requirement requirements.txt \
+    && rm -v poetry_demo*.whl \
+    && ln --symbolic --target-directory=/usr/local/bin /usr/local/src/poetry-demo/bin/poetry-demo
+
+RUN groupadd --gid $GID poetry-demo \
+    && useradd --gid $GID --no-log-init -M --uid $UID poetry-demo
+
+USER $UID
+
+ENTRYPOINT ["poetry-demo"]
```

```console
git diff
git add Dockerfile
git commit -m "Add build and production stages to Dockerfile"
```

### Building and Running the Production Docker Image

```console
docker rmi poetry-demo-develop
docker image prune
docker builder prune
docker build --tag poetry-demo:latest --tag poetry-demo:0.1.0 .
docker images poetry-demo
docker run -it --rm poetry-demo:0.1.0
docker run -it --rm poetry-demo:0.1.0 -tz Asia/Ulaanbaatar
docker run -it --rm poetry-demo:0.1.0 -tz not/found
docker run -it --rm --entrypoint id poetry-demo:0.1.0
docker run -it --rm --entrypoint /usr/local/src/poetry-demo/bin/python poetry-demo:0.1.0 \
    -c "from poetry_demo import main; main()"
docker run -it --rm --entrypoint /usr/local/src/poetry-demo/bin/python poetry-demo:0.1.0 \
    -m pip freeze
docker run -it --rm --entrypoint cat poetry-demo:0.1.0 requirements.txt
```

[multi-stage builds]: https://docs.docker.com/develop/develop-images/multistage-build/
