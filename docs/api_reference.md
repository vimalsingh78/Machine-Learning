# API Reference

## Models

### Neural Network
```python
class NeuralNetwork:
    def __init__(self, layers=[64, 32], learning_rate=0.01):
        """Initialize neural network
        
        Args:
            layers (list): List of neurons in each hidden layer
            learning_rate (float): Learning rate for optimization
        """
        pass

    def train(self, X, y, epochs=100):
        """Train the neural network
        
        Args:
            X (np.array): Training features
            y (np.array): Training labels
            epochs (int): Number of training epochs
        """
        pass
```

### Data Preprocessing
```python
class DataPreprocessor:
    def normalize(self, data):
        """Normalize the input data
        
        Args:
            data (np.array): Input data to normalize
        """
        pass
```

## Utility Functions
- `evaluate_model(model, X_test, y_test)`
- `load_data(path)`
- `save_model(model, path)`