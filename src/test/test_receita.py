import pytest

from httpx import AsyncClient

from router.main import app


@pytest.mark.asyncio
async def test_receita():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/receita/cadastro", json={
            "descricao": "string",
            "valor": 0,
            "data": "2022-10-18"})
        response2 = await ac.post("/receita/cadastro", json={
            "descricao": "string",
            "valor": 0,
            "data": "2022-10-18"})
        response3= await ac.put(f"/receita/{response.id}",data={
            "descricao": "string",
            "valor": 200,
            "data": "2022-10-18"})
    assert response.status_code == 200
    assert response2.status_code == 406
    assert response3.status_code == 200