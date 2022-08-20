
import pytest 
from httpx import AsyncClient

from router.main import app

@pytest.mark.asyncio
async def test_main():
    async with AsyncClient(app=app,base_url="http://test") as ac:
        response=await ac.get("/")
    assert response.status_code == 200
    