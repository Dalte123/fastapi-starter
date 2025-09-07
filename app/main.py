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
from sqlalchemy.orm import Session
from .db import Base, engine, get_db
from . import models, schemas

app = FastAPI(title="Fast API")

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

@app.post("/users/", response_model=schemas.UserRead, status_code=201)
def create_user(payload: schemas.UserCreate, db: Session = Depends(get_db)):
    # check duplicate email
    existing = db.query(models.User).filter(models.User.email == payload.email).first()
    if existing:
        from fastapi import HTTPException
        raise HTTPException(status_code=409, detail="Email already registered")
    user = models.User(name=payload.name, email=payload.email)
    db.add(user)
    db.commit()
    db.refresh(user)  
    return user

@app.get("/users/", response_model=list[schemas.UserRead])
def list_users(db: Session = Depends(get_db)):
    return db.query(models.User).order_by(models.User.id).all()

@app.get("/users/{user_id}", response_model=schemas.UserRead)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.get(models.User, user_id)
    if not user:
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail="User not found")
    return user


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
