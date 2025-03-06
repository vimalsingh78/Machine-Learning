# Building a Basic Neural Network

## Introduction
This tutorial will guide you through creating and training a simple neural network for classification tasks.

## Steps

### 1. Data Preparation
```python
import numpy as np
from src.preprocessing import DataPreprocessor

# Load and preprocess data
X, y = load_data('path/to/data')
preprocessor = DataPreprocessor()
X_processed = preprocessor.normalize(X)
```

### 2. Model Creation
```python
from src.models import NeuralNetwork

# Create model
model = NeuralNetwork(
    layers=[64, 32],
    learning_rate=0.01
)
```

### 3. Training
```python
# Train model
model.train(X_processed, y, epochs=100)
```

### 4. Evaluation
```python
# Evaluate model
accuracy = model.evaluate(X_test, y_test)
print(f'Model accuracy: {accuracy}')
```

## Best Practices
- Always normalize your input data
- Use cross-validation
- Monitor training progress
- Save model checkpoints