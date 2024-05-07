import pytest_asyncio

from app import factory


@pytest_asyncio.fixture
async def cli(event_loop, aiohttp_client):
    app = await factory()
    return await aiohttp_client(app)
