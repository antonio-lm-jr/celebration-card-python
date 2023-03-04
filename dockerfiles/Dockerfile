FROM python:3.11-slim

ENV POETRY_VIRTUALENVS_CREATE false
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH .

COPY poetry.lock pyproject.toml ./

RUN pip install --no-cache-dir -U pip poetry && \
    poetry install

COPY ./src ./src/

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "3000"]
