FROM python:3.11

WORKDIR /usr/src/app

RUN pip install poetry && poetry config virtualenvs.create false

COPY poetry.lock ./
COPY pyproject.toml ./

RUN poetry install --no-dev

COPY . /usr/src/app

RUN poetry run pytest

CMD gunicorn app:factory --bind=$HOST:$PORT --worker-class=aiohttp.GunicornWebWorker --log-config=./etc/logging.conf