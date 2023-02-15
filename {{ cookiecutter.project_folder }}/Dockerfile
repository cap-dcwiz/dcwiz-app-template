FROM python:3.11

ENV PYTHONPATH="${PYTHONPATH}:/opt/" \
    PYTHONUNBUFFERED=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=on

RUN pip install poetry
RUN poetry config virtualenvs.create false

WORKDIR /opt

COPY pyproject.toml /opt/
COPY {{ cookiecutter.project_slug }} /opt/{{ cookiecutter.project_slug }}

RUN apt-get update && apt-get upgrade -y &&  apt-get install build-essential -y && \
    poetry install --no-dev && \
    apt-get purge build-essential -y && rm -rf /var/lib/apt/lists/* && \
    rm /opt/poetry.lock /opt/pyproject.toml

COPY alembic.ini /opt/alembic.ini
COPY alembic /opt/alembic

ENTRYPOINT ["{{ cookiecutter.bin_name }}"]