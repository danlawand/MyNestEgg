from fastapi import FastAPI
from enum import Enum

app = FastAPI()

class InterestRate(str, Enum):
    _15 = "15%"
    _10 = "10%"
    _5 = "5%"

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/select_interest_rate/{interest_rate}")
def select_interest_rate(interest_rate: InterestRate):
    if interest_rate is InterestRate._15:
        message = "High option"
    elif interest_rate is InterestRate._10:
        message = "Medium option"
    elif interest_rate is InterestRate._5:
        message = "Low option"
    else:
        return {"ERROR: Interest rate not found"}
    return {"interest rate": interest_rate, "message": message}

@app.get("/get_income/{income}")
def get_income(income: int):
    return {"your income is": income}

@app.get("/files/{file_path:path}")
def read_file(file_path: str):
    return {"file path": file_path}

