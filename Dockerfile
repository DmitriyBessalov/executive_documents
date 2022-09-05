FROM python:3.10
WORKDIR /var/www/domen.comjournal.domen.com
RUN apt-get update
RUN apt-get install -y cmake build-essential g++ python3-distutils python3-apt python3-dev python3-psycopg2 libpq-dev curl tmux net-tools gcc git alembic
COPY ./pyproject.toml /var/www/domen.comjournal.domen.com/pyproject.toml
RUN pip install --upgrade pip
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry update
