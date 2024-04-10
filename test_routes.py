from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_register_user():
    payload = {
        "name": "John Doe",
        "age": 30,
        "gender": "Male",
        "ismarried": False,
        "profile_picture": ("afr.png", open("uploaded_images/afr.png", "rb"), "image/png")
    }
    response = client.post("/register", files=payload)
    assert response.status_code == 200
    assert response.json()["name"] == "John Doe"

def test_get_user_by_id():
    response = client.get("/users/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1

    response = client.get("/users/999")
    assert response.status_code == 404