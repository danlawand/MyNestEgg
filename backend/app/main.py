from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import calculator, other

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ou ["http://localhost:3000"] para segurança
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(calculator.router, prefix="/calculator", tags=["Calculator"])
# app.include_router(other.router, prefix="/other", tags=["Other"])

