
def add(a: int , b: int ) -> int:
    if a is None or b is None:
        raise ValueError("Both 'a' and 'b' query params are required")
    return a + b


def multiply(a: int , b: int ) -> int:
    return a * b


def divide(a: float , b: float ) -> float:
    if b == 0:
        raise ValueError("Division by zero not allowed")
    return a / b


def subtract(a: int , b: int ) -> int:
    return a - b


def compute(op: str, a: float, b:float) -> float:
    op = op.lower()
    if op == "add":
        return add(a, b)
    elif op == "subtract": 
        return subtract(a, b)
    elif op == "multiply": 
        return multiply(a, b)
    elif op == "divide": 
        return divide(a, b)
    else:
        raise ValueError("Unsupported operation")
         
    


