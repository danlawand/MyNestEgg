from fastapi import FastAPI

app = FastAPI()


@app.post("/calculate/{value}")
def calulate(value: int):
    return {"Your value is": value}