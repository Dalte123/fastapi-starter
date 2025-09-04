from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.math_utils import (
    add as add_util,
    subtract as sub_util,
    multiply as mul_util,
    divide as div_util,
    compute,
)
from app.auth import authfunc
from fastapi import Depends



app = FastAPI(title="Fast API")


# Pydantic request models
class Operation(BaseModel):
    a: int
    b: int
    op: str


@app.get("/healthz")
def healthz():
    return {"status": "ok"}


@app.get("/echo")
def echo(msg: str = "hello"):
    return {"msg": msg}


@app.get("/math/add")
def add(a: int | None = None, b: int | None = None, auth: bool = Depends(authfunc)):
    if a is None or b is None:
        # 400 Bad Request if a or b missing
        raise HTTPException(
            status_code=400, detail="Both 'a' and 'b' query params are required"
        )
    # Validate presence
    return {"result": add_util(a, b)}


@app.get("/math/multiply")
def multiply(a: int | None = None, b: int | None = None, auth: bool = Depends(authfunc)):
    if a is None or b is None:
        # 400 Bad Request if a or b missing
        raise HTTPException(
            status_code=400, detail="Both 'a' and 'b' query params are required"
        )
    return {"result": mul_util(a, b)}


@app.get("/math/divide")
def divide(a: float | None = None, b: float | None = None, auth: bool = Depends(authfunc)):
    if a is None or b is None:
        # 400 Bad Request if a or b missing
        raise HTTPException(
            status_code=400, detail="Both 'a' and 'b' query params are required"
        )
    try:
        return {"result": div_util(a, b)}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/math/subtract")
def subtract(a: int | None = None, b: int | None = None, auth: bool = Depends(authfunc)):
    if a is None or b is None:
        # 400 Bad Request if a or b missing
        raise HTTPException(
            status_code=400, detail="Both 'a' and 'b' query params are required"
        )
    return {"result": sub_util(a, b)}


@app.post("/math/operation")
def do_operation(payload: Operation, auth: bool = Depends(authfunc)):
    try:
        return {"result": compute(payload.op, payload.a, payload.b)}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
