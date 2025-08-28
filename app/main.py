from fastapi import FastAPI, HTTPException

app = FastAPI(title="Day1 Starter")

@app.get("/healthz")
def healthz():
    return {"status": "ok"}

@app.get("/echo")
def echo(msg: str = "hello"):
    return {"msg": msg}

@app.get("/math/add")
def add(a: int | None = None, b: int | None = None):
    # Validate presence
    if a is None or b is None:
        # 400 Bad Request if a or b missing 
        raise HTTPException(status_code=400, detail="Both 'a' and 'b' query params are required")
    # Return sum
    return {"result": a + b}

@app.get("/math/multiply")
def multiply(a: int | None = None, b: int | None = None):
    if a is None or b is None:
        raise HTTPException(status_code=400, detail="Both 'a' and 'b' query params are required")
    return {"result": a * b}

@app.get("/math/divide")
def divide(a: float | None = None, b: float | None = None):
    if a is None or b is None:
        raise HTTPException(status_code=400, detail="Both 'a' and 'b' query params are required")

    elif b == 0:
        raise HTTPException(status_code=400, detail="Division by zero not allowed")
    return {"result": a / b}