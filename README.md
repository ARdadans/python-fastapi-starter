# Python FastAPI Starter

Minimal and portable FastAPI starter for APIs and small backend projects.

The project is designed to run on different devices with or without `uv`.

## Features

- FastAPI
- Uvicorn
- Pydantic Settings
- In-memory Todo API
- Pytest
- Ruff
- Docker support
- `uv` support (optional)

## Requirements

Python 3.12 or newer.

`uv` is optional.

## Clone

```bash
git clone https://github.com/ARdadans/python-fastapi-starter.git
cd python-fastapi-starter
```

## Run without uv

This is the recommended method for a device that does not have `uv` installed.

Install dependencies:

```bash
pip install -r requirements.txt
```

Run:

```bash
python run.py
```

The server will start on:

```text
http://127.0.0.1:8000
```

API documentation:

```text
http://127.0.0.1:8000/docs
```

## Run with uv

If `uv` is installed:

```bash
uv sync
uv run python-fastapi-starter
```

## Configuration

The default configuration is:

```text
HOST=0.0.0.0
PORT=8000
RELOAD=true
```

You can use environment variables directly or create a `.env` file based on `.env.example`.

Example:

```text
HOST=0.0.0.0
PORT=8080
RELOAD=true
```

On Linux/macOS:

```bash
PORT=8080 python run.py
```

On Windows PowerShell:

```powershell
$env:PORT=8080; python run.py
```

## API Endpoints

| Method | Endpoint | Description |
| --- | --- | --- |
| GET | `/` | API status |
| GET | `/health` | Health check |
| GET | `/api/todos` | Get all todos |
| GET | `/api/todos/{id}` | Get one todo |
| POST | `/api/todos` | Create todo |
| DELETE | `/api/todos/{id}` | Delete todo |

### Create Todo

```bash
curl -X POST http://127.0.0.1:8000/api/todos \
  -H "Content-Type: application/json" \
  -d "{\"title\":\"Learn FastAPI\"}"
```

### Get Todos

```bash
curl http://127.0.0.1:8000/api/todos
```

## Data Storage

Todo data is stored in memory.

Data will be lost when the application restarts.

This is intentional to keep the starter minimal and portable. No database setup is required.

## Testing

Install development dependencies with `uv`:

```bash
uv sync
```

Run tests:

```bash
uv run pytest
```

Run Ruff:

```bash
uv run ruff check .
```

## Docker

Build:

```bash
docker build -t python-fastapi-starter .
```

Run:

```bash
docker run --rm -p 8000:8000 python-fastapi-starter
```

Custom port:

```bash
docker run --rm -p 8080:8080 -e PORT=8080 python-fastapi-starter
```

## Project Structure

```text
python-fastapi-starter/
├── .github/
│   └── workflows/
│       └── test.yml
├── src/
│   └── python_fastapi_starter/
│       ├── __init__.py
│       ├── cli.py
│       ├── config.py
│       └── main.py
├── tests/
│   └── test_todos.py
├── .dockerignore
├── .env.example
├── .gitignore
├── .python-version
├── Dockerfile
├── README.md
├── pyproject.toml
├── requirements.txt
├── run.py
└── uv.lock
```

## License

MIT
