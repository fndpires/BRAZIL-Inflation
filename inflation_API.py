import pickle
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()
model = pickle.load(open("model_ipca.pkl", "rb"))

class Factors(BaseModel):
    food: float
    housing: float
    house_items: float
    clothing: float
    transport: float 
    communication: float 
    health: float
    personal: float
    education: float
    int_rate: float
    min_wages: float
    
    
@app.post("/inflation")   
async def predict_inflation(factor: Factors):
    data = factor.dict()
    data_in = [[data["food"], data["housing"], data["house_items"], data["clothing"],
    data["transport"], data["communication"], data["health"], data["personal"],
    data["education"], data["int_rate"], data["min_wages"]]]
    
    prediction = model.predict(data_in)
     
    return {"prediction": prediction[0]}