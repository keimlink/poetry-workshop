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

FROM python-poetry AS develop

WORKDIR /usr/local/src/poetry-demo

COPY poetry.lock pyproject.toml ./

COPY src src

RUN poetry install

ENV PYTHONUNBUFFERED=True

VOLUME /usr/local/src/poetry-demo

CMD ["poetry run poetry-demo"]
