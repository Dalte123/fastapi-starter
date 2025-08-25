from fastapi import FastAPI

app = FastAPI(title="Day1 Starter")

@app.get("/healthz")
def healthz():
    return {"status": "ok"}
    
@app.get("/echo")
def echo(msg: str = "hello"):
    return {"msg": msg}