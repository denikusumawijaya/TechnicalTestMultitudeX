import pytest
from httpx import AsyncClient
from app.main import app
from app import Base, engine, SessionLocal

@pytest.fixture(scope="module")
async def db_setup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)

@pytest.mark.asyncio
async def test_create_feedback(db_setup):
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/feedback/", json={"score": 5})
    assert response.status_code == 200
    assert response.json()["score"] == 5
