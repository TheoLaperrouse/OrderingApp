# Etape de construction (Builder)
FROM python:3.9

RUN pip install --upgrade pip && \
    pip install poetry

WORKDIR /app
COPY . .

RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi --no-dev

EXPOSE 8000

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]