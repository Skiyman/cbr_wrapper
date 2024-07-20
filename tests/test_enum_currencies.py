import pytest

from tests.conftest import async_client


@pytest.mark.asyncio
async def test_enum_currencies_route(async_client):
    result = await async_client.get("/enum_currencies")

    assert result.status_code == 200
    assert len(result.json()) > 0