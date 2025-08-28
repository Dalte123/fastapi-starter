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

def test_add_happy_path():
    r = client.get("/math/add", params={"a": 2, "b": 3})
    assert r.status_code ==200
    assert r.json() == {"result": 5}

def test_add_missing_param():
    r = client.get("/math/add", params={"a": 2})
    assert r.status_code == 400
    assert r.json()["detail"] == "Both 'a' and 'b' query params are required"

def test_multiply_happy_path():
    r = client.get("/math/multiply", params={"a":2, "b": 3})
    assert r.status_code == 200
    assert r.json() == {"result":6}

def test_multiply_missing_param():
    r = client.get("/math/multiply", params={"a": 2})
    assert r.status_code == 400
    assert r.json()["detail"] == "Both 'a' and 'b' query params are required"

def test_divide_happy_path():
   r = client.get("/math/divide", params={"a":10.0, "b": 2.0})
   assert r.status_code == 200
   assert r.json() == {"result": 5.0}

def test_divide_missing_param():
    r = client.get("/math/divide", params={"a": 10.0})
    assert r.status_code == 400
    assert r.json()["detail"] == "Both 'a' and 'b' query params are required"

def test_divide_by_zero():
    r = client.get("/math/divide", params={"a": 10.0, "b": 0.0})
    assert r.status_code == 400
    assert r.json()["detail"] == "Division by zero not allowed"

def test_subtract_happy_path():
    r = client.get("/math/subtract", params={"a": 10, "b": 3})
    assert r.status_code == 200
    assert r.json() == {"result": 7}

def test_subtract_missing_param():
    r = client.get("/math/subtract", params={"a": 10})
    assert r.status_code == 400
    assert r.json()["detail"] == "Both 'a' and 'b' query params are required"

def test_subtract_negative_result():
    r = client.get("/math/subtract", params={"a": 3, "b": 10})
    assert r.status_code == 200
    assert r.json() == {"result": -7}

    