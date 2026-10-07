import pytest
from httpx import ASGITransport, AsyncClient

from python_fastapi_starter.main import app, todos


@pytest.fixture(autouse=True)
def reset_todos():
    todos.clear()


@pytest.mark.asyncio
async def test_root():
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test",
    ) as client:
        response = await client.get("/")

    assert response.status_code == 200
    assert response.json()["status"] == "ok"


@pytest.mark.asyncio
async def test_health():
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test",
    ) as client:
        response = await client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


@pytest.mark.asyncio
async def test_get_todos():
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test",
    ) as client:
        response = await client.get("/api/todos")

    assert response.status_code == 200
    assert response.json() == []


@pytest.mark.asyncio
async def test_create_todo():
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test",
    ) as client:
        response = await client.post("/api/todos", json={"title": "Test"})

    assert response.status_code == 201
    assert response.json() == {"id": 1, "title": "Test", "completed": False}


@pytest.mark.asyncio
async def test_get_todo():
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test",
    ) as client:
        await client.post("/api/todos", json={"title": "Test"})
        response = await client.get("/api/todos/1")

    assert response.status_code == 200
    assert response.json()["title"] == "Test"


@pytest.mark.asyncio
async def test_delete_todo():
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test",
    ) as client:
        await client.post("/api/todos", json={"title": "Test"})
        response = await client.delete("/api/todos/1")

    assert response.status_code == 200
    assert response.json()["message"] == "Todo deleted"
