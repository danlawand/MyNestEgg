from fastapi import APIRouter
from enum import Enum
from pydantic import BaseModel

router = APIRouter()

class InterestRate(str, Enum):
    _15 = "15%"
    _10 = "10%"
    _5 = "5%"

@router.get("/")
def root():
    return {"message": "Hello World"}

@router.get("/select_interest_rate/{interest_rate}")
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

@router.get("/get_income/{income}")
def get_income(income: int):
    return {"your income is": income}

@router.get("/files/{file_path:path}")
def read_file(file_path: str):
    return {"file path": file_path}

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@router.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@router.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.model_dump()}


@router.post("/calculate/{value}")
def calulate(init_amount: float, monthly_contributions: float, interest_rate: float, is_interest_rate_annual: bool, duration: int, is_duration_in_years: bool, annual_contribution_growth):
    return {'hello'}