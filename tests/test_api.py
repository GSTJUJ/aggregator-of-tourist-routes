from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Сервер работает!"}

def test_register():
    response = client.post("/register", json={
        "full_name": "Test User",
        "phone": "+700000000",
        "email": "test123@mail.com",
        "region": "Москва",
        "password": "1234"
    })

    assert response.status_code == 200
    assert "Пользователь зарегистрирован" in response.text    

def test_login():
    response = client.post("/login", json={
        "email": "test123@mail.com",
        "password": "1234"
    })

    assert response.status_code == 200    