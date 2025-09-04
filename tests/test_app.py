from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)
VALID_HEADERS = {"Authorization": "Bearer superSecret123"}
WRONG_SCHEME_HEADERS = {"Authorization": "Token superSecret123"}  # not "Bearer"
WRONG_TOKEN_HEADERS = {"Authorization": "Bearer nottherighttoken"}

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
    r = client.get("/math/add", params={"a": 2, "b": 3}, headers=VALID_HEADERS)
    assert r.status_code == 200
    assert r.json() == {"result": 5}

def test_add_no_header():
    r = client.get("/math/add", params={"a": 2, "b": 3})
    assert r.status_code == 401
    assert r.json()["detail"] == "Token was not sent"

def test_wrong_scheme_add():
    r = client.get("/math/add", params={"a": 2, "b": 3}, headers=WRONG_SCHEME_HEADERS)
    assert r.status_code == 400
    assert r.json()["detail"] == "Token does not start with Bearer"

def test_wrong_token_add():
    r = client.get ("/math/add", params={"a": 2, "b": 3}, headers=WRONG_TOKEN_HEADERS)  
    assert r.status_code == 401
    assert r.json()["detail"] == "Unauthorized"


def test_add_missing_param():
    r = client.get("/math/add", params={"a": 2}, headers=VALID_HEADERS)
    assert r.status_code == 400
    assert r.json()["detail"] == "Both 'a' and 'b' query params are required"

def test_multiply_happy_path():
    r = client.get("/math/multiply", params={"a":2, "b": 3}, headers=VALID_HEADERS)
    assert r.status_code == 200
    assert r.json() == {"result":6}

def test_multiply_missing_param():
    r = client.get("/math/multiply", params={"a": 2}, headers=VALID_HEADERS)
    assert r.status_code == 400
    assert r.json()["detail"] == "Both 'a' and 'b' query params are required"

def test_divide_happy_path():
   r = client.get("/math/divide", params={"a":10.0, "b": 2.0}, headers=VALID_HEADERS)
   assert r.status_code == 200
   assert r.json() == {"result": 5.0}

def test_divide_missing_param():
    r = client.get("/math/divide", params={"a": 10.0}, headers=VALID_HEADERS)
    assert r.status_code == 400
    assert r.json()["detail"] == "Both 'a' and 'b' query params are required"

def test_divide_by_zero():
    r = client.get("/math/divide", params={"a": 10.0, "b": 0.0}, headers=VALID_HEADERS)
    assert r.status_code == 400
    assert r.json()["detail"] == "Division by zero not allowed"

def test_subtract_happy_path():
    r = client.get("/math/subtract", params={"a": 10, "b": 3}, headers=VALID_HEADERS)
    assert r.status_code == 200
    assert r.json() == {"result": 7}

def test_subtract_missing_param():
    r = client.get("/math/subtract", params={"a": 10}, headers=VALID_HEADERS)
    assert r.status_code == 400
    assert r.json()["detail"] == "Both 'a' and 'b' query params are required"

def test_subtract_negative_result():
    r = client.get("/math/subtract", params={"a": 3, "b": 10}, headers=VALID_HEADERS)
    assert r.status_code == 200
    assert r.json() == {"result": -7}

def test_operation_add():
   r = client.post("/math/operation", json={"a":10, "b": 3, "op":"add"}, headers=VALID_HEADERS)
   assert r.status_code == 200
   assert r.json() == {"result": 13}

def test_operation_subtract():
    r = client.post("/math/operation", json={"a":10, "b": 3, "op":"subtract"}, headers=VALID_HEADERS)
    assert r.status_code == 200
    assert r.json() == {"result": 7}

def test_operation_multiply():
    r = client.post("/math/operation", json={"a":10, "b": 3, "op":"multiply"}, headers=VALID_HEADERS)
    assert r.status_code == 200
    assert r.json() == {"result": 30}

def test_operation_divide():
    r = client.post("/math/operation", json={"a":12, "b": 3, "op":"divide"}, headers=VALID_HEADERS)
    assert r.status_code == 200
    assert r.json() == {"result": 4.0}

def test_operation_divide_zero():
    r = client.post("/math/operation", json={"a": 5, "b": 0, "op":"divide"}, headers=VALID_HEADERS)
    assert r.status_code == 400
    assert r.json()["detail"] == "Division by zero not allowed"


def test_operation_unsupported():
    r = client.post("/math/operation", json={"a": 5, "b": 1, "op":"carrot"}, headers=VALID_HEADERS)
    assert r.status_code == 400
    assert r.json()["detail"] == "Unsupported operation"

def test_operation_case_insensitive():
    r = client.post("/math/operation", json={"a": 10, "b": 5, "op":"Add"}, headers=VALID_HEADERS)
    assert r.status_code == 200
    assert r.json() == {"result": 15}

def test_operation_wrong_input():
    r = client.post("/math/operation", json={"a": "ten", "b": "five", "op":"Add"}, headers=VALID_HEADERS)
    assert r.status_code == 422
    # converts HTTP to Python dictionary 
    body = r.json()
    assert "integer" in body["detail"][0]["msg"].lower()
    

def test_operation_wrong_string_int():
    r = client.post("/math/operation", json={"a": "TEN", "b": 5, "op":"Add"}, headers=VALID_HEADERS)
    assert r.status_code == 422
    body = r.json()
    assert "integer" in body["detail"][0]["msg"].lower()

def test_add_no_header_op():
    r = client.post("/math/operation", json={"a": 10, "b": 5, "op":"add"})
    assert r.status_code == 401
    assert r.json()["detail"] == "Token was not sent"

def test_wrong_scheme_op():
    r = client.post("/math/operation", json={"a": 10, "b": 5, "op":"add"}, headers=WRONG_SCHEME_HEADERS)
    assert r.status_code == 400
    assert r.json()["detail"] == "Token does not start with Bearer"

def test_wrong_token_op():
    r = client.post("/math/operation", json={"a": 10, "b": 5, "op":"add"}, headers=WRONG_TOKEN_HEADERS)  
    assert r.status_code == 401
    assert r.json()["detail"] == "Unauthorized"    
   

def test_operation_json_error():
    r = client.post(
        "/math/operation",
        data='{"a": TEN, "b": 5, "op": "add"}',
        headers={"Content-Type": "application/json"}
        )
    assert r.status_code == 422
    body = r.json()
    assert body["detail"][0]["type"] == "json_invalid"
    assert "JSON decode error" in body["detail"][0]["msg"]