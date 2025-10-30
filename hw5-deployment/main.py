
from fastapi import FastAPI
from pydantic import BaseModel
import pickle

# Load the model
with open('pipeline_v1.bin', 'rb') as f:
    pipeline = pickle.load(f)

# Define request model
class ClientData(BaseModel):
    lead_source: str
    number_of_courses_viewed: int
    annual_income: float

# Create FastAPI app
app = FastAPI()

@app.post("/predict")
def predict(client: ClientData):
    # Convert to dict
    client_dict = client.dict()

    # Prepare for prediction (needs to be a list of one record)
    X = [client_dict]

    # Get probability
    proba = pipeline.predict_proba(X)[0, 1]

    return {"conversion_probability": round(proba, 3)}

@app.get("/")
def root():
    return {"message": "Lead Scoring API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
