import pytest_asyncio
from fastapi.testclient import TestClient
from httpx import AsyncClient, ASGITransport

from main import app

client = TestClient(app)


@pytest_asyncio.fixture(scope="session")
async def async_client() -> AsyncClient | None:
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as _client:
        yield _client
