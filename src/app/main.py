from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from src.model import predict

app = FastAPI()

class InputData(BaseModel):
  days: int

class PredictionOutput(BaseModel):
  ds: str
  yhat: float
  yhat_lower: float
  yhat_upper: float

@app.post('/predict', response_model=List[PredictionOutput])
async def get_prediction(data: InputData):
    results = predict(data.days)
    return results.to_dict('records')
