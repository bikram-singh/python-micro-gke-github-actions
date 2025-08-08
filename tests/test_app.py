# tests/test_app.py - basic unit test
from app import app

def test_root():
    client = app.test_client()
    res = client.get("/")
    assert res.status_code == 200
    assert res.get_json() == {"message": "Hello from Flask microservice!"}
