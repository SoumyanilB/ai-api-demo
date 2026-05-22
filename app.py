from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def home():
    return {
        "message":"your AI Model's API is running"
    }

@app.post("/predict")
def predict(data : dict): #type-hinting for the input data
    user_input = data.get("text")
    prediction = f"Processed your input: {user_input}" #actual model prediction logic would go here

    return {

        "prediction": prediction
    }       

