from fastapi import FastAPI

from app.routes import calculator, other

app = FastAPI()

app.include_router(calculator.router, prefix="/calculator", tags=["Calculator"])
app.include_router(other.router, prefix="/other", tags=["Other"])

