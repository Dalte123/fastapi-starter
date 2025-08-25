from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_healthz():
    r = client.get("/healthz")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}

def test_echo_default():
    r = client.get("/echo")
    assert r.status_code == 200
    assert r.json() == {"msg": "hello"}

def test_echo_query():
    r = client.get("/echo", params={"msg": "world"})
    assert r.status_code == 200
    assert r.json() == {"msg": "world"}