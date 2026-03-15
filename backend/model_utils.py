import joblib
import numpy as np
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()  

MODEL_PATH = os.getenv("MODEL_PATH")

# Load your trained model (.pkl)
model = joblib.load(MODEL_PATH)

def predict_heart_disease(features: list):
    """
    Predict heart disease based on patient features.
    Parameters:
        features (list): list of numerical inputs in the same order as training data
    Returns:
        int: 1 if heart disease is predicted, else 0
    """
    data = np.array(features).reshape(1, -1)
    prediction = model.predict(data)[0]
    probability = model.predict_proba(data)[0][1]
    return int(prediction), round(probability, 3)

