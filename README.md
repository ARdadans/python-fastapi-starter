# Python FastAPI Starter

Simple, portable FastAPI starter.

## Requirements

- Python 3.12+
- pip (for running without uv)
- uv (optional, for development)

## Run without uv

```bash
pip install -r requirements.txt
python run.py
```

Server:

http://127.0.0.1:8000

Swagger:

http://127.0.0.1:8000/docs

## Run with uv

```bash
uv sync
uv run python-fastapi-starter
```

## Environment

```text
HOST=0.0.0.0
PORT=8000
RELOAD=true
```

Environment variables can be provided directly or through `.env`.

## API

- GET /
- GET /health
- GET /api/todos
- GET /api/todos/{id}
- POST /api/todos
- DELETE /api/todos/{id}

Todo data is stored in memory and is lost when the application restarts.

## Test

```bash
pytest
```

## Lint

```bash
ruff check .
```

## Docker

```bash
docker build -t python-fastapi-starter .
docker run --rm -p 8000:8000 python-fastapi-starter
```
