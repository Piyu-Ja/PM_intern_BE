from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class InputData(BaseModel):
    text: str

@app.post("/predict")
async def predict(data: InputData):
    # replace this with your AI model logic
    return {"response": f"You sent: {data.text}"}