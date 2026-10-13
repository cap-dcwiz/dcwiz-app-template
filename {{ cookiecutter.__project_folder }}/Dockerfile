FROM python:3.12

ENV PYTHONPATH="${PYTHONPATH}:/opt/" \
    PYTHONUNBUFFERED=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=on

RUN pip install poetry
RUN poetry config virtualenvs.create false

WORKDIR /opt

COPY pyproject.toml /opt/
COPY {{ cookiecutter.__project_slug }} /opt/{{ cookiecutter.__project_slug }}

# Optional GITHUB_TOKEN secret (passed by CI) lets poetry fetch private git dependencies.
RUN --mount=type=secret,id=GITHUB_TOKEN \
    apt-get update && apt-get upgrade -y &&  apt-get install build-essential -y && \
    if [ -s /run/secrets/GITHUB_TOKEN ]; then \
        echo "https://x-access-token:$(cat /run/secrets/GITHUB_TOKEN)@github.com" > ${HOME}/.git-credentials && \
        git config --global credential.helper store; \
    fi && \
    poetry install --only main --no-cache && \
    apt-get purge build-essential -y && rm -rf /var/lib/apt/lists/* && \
    rm /opt/poetry.lock /opt/pyproject.toml && \
    rm -f ${HOME}/.git-credentials

COPY alembic.ini /opt/alembic.ini
COPY alembic /opt/alembic

ENTRYPOINT ["{{ cookiecutter.__bin_name }}"]