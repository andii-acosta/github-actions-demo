from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_suma():
    response = client.post("/sumar", json={"a": 10, "b": 15})
    assert response.status_code == 200
    assert response.json() == {"resultado": 25}
