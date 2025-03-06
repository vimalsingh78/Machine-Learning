# Model Deployment Guide

## 1. Model Serialization

### Using Pickle
```python
import pickle

def save_model(model, filepath):
    with open(filepath, 'wb') as f:
        pickle.dump(model, f)

def load_model(filepath):
    with open(filepath, 'rb') as f:
        return pickle.load(f)
```

## 2. API Development

### FastAPI Implementation
```python
from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np

app = FastAPI()

class PredictionInput(BaseModel):
    features: list[float]

class PredictionOutput(BaseModel):
    prediction: float
    probability: float

@app.post('/predict', response_model=PredictionOutput)
async def predict(input_data: PredictionInput):
    features = np.array(input_data.features).reshape(1, -1)
    prediction = model.predict(features)
    probability = model.predict_proba(features).max()
    
    return PredictionOutput(
        prediction=float(prediction[0]),
        probability=float(probability)
    )
```

## 3. Model Monitoring

### Performance Metrics Tracking
```python
def monitor_model_performance(model, X, y, metrics_log):
    predictions = model.predict(X)
    current_accuracy = accuracy_score(y, predictions)
    
    metrics_log['timestamp'].append(datetime.now())
    metrics_log['accuracy'].append(current_accuracy)
    
    if current_accuracy < 0.9 * metrics_log['accuracy'][0]:
        send_alert('Model performance degradation detected')
```

### Data Drift Detection
```python
def detect_data_drift(reference_data, current_data, threshold=0.05):
    from scipy import stats
    
    drift_detected = False
    for feature in range(reference_data.shape[1]):
        stat, p_value = stats.ks_2samp(
            reference_data[:, feature],
            current_data[:, feature]
        )
        if p_value < threshold:
            drift_detected = True
            break
            
    return drift_detected
```