# score.py
import json
import numpy as np
import joblib
import os

def init():
    global model
    model_path = os.path.join(os.getenv('AZUREML_MODEL_DIR'), 'car_price_model.pkl')
    model = joblib.load(model_path)

def run(raw_data):
    try:
        data = json.loads(raw_data)['data']
        data = np.array(data)
        result = model.predict(data)
        print("Prediction:", result.tolist())  # <-- This will appear in std_log.txt
        return result.tolist()
    except Exception as e:
        print("Error:", str(e))  # <-- Also helpful for debugging
        return str(e)

# Optional: local test only (this won't execute in Azure ML job)
if __name__ == "__main__":
    init()
    test_input = {
        "data": [[15, 4, 150, 100, 30, 1200]]
    }
    raw_data = json.dumps(test_input)
    prediction = run(raw_data)
    print("Prediction Result:", prediction)
