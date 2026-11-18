from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "Welcome to CI/CD Practical"
    }


def test_users():
    response = client.get("/users")

    assert response.status_code == 200
    assert len(response.json()) == 2


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"