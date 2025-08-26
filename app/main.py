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
 #Validate presense

 if a is None or b is None:
    # 400 Bad Request if a or b missing 
    raise HTTPException(status_code=400, detail="Both 'a' and 'b' query params are required")
    #return sum

 return {"result": a + b}