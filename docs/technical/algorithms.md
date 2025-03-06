# Machine Learning Algorithms

## 1. Neural Networks

### Architecture Components

#### Layers
- **Input Layer**: Initial data entry point
- **Hidden Layers**: Intermediate processing layers
  - Dense/Fully Connected
  - Convolutional
  - Recurrent
- **Output Layer**: Final prediction layer

#### Activation Functions
```python
def relu(x):
    return max(0, x)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def tanh(x):
    return np.tanh(x)

def softmax(x):
    exp_x = np.exp(x - np.max(x))
    return exp_x / exp_x.sum()
```

### Backpropagation Algorithm
1. **Forward Pass**
   ```python
   def forward_pass(self, X):
       self.layer1 = np.dot(X, self.weights1)
       self.activation1 = self.relu(self.layer1)
       self.layer2 = np.dot(self.activation1, self.weights2)
       self.output = self.softmax(self.layer2)
   ```

2. **Backward Pass**
   ```python
   def backward_pass(self, X, y, learning_rate):
       self.output_error = self.output - y
       self.output_delta = self.output_error * self.derivative_softmax(self.layer2)
       
       self.layer1_error = np.dot(self.output_delta, self.weights2.T)
       self.layer1_delta = self.layer1_error * self.derivative_relu(self.layer1)
       
       # Update weights
       self.weights2 -= learning_rate * np.dot(self.activation1.T, self.output_delta)
       self.weights1 -= learning_rate * np.dot(X.T, self.layer1_delta)
   ```

## 2. Optimization Algorithms

### Gradient Descent Variants
1. **Batch Gradient Descent**
   ```python
   def batch_gradient_descent(X, y, learning_rate, epochs):
       weights = np.zeros(X.shape[1])
       for _ in range(epochs):
           gradient = compute_gradient(X, y, weights)
           weights -= learning_rate * gradient
       return weights
   ```

2. **Stochastic Gradient Descent (SGD)**
   ```python
   def sgd(X, y, learning_rate, epochs):
       weights = np.zeros(X.shape[1])
       for _ in range(epochs):
           for i in range(len(X)):
               gradient = compute_gradient(X[i:i+1], y[i:i+1], weights)
               weights -= learning_rate * gradient
       return weights
   ```

3. **Mini-batch Gradient Descent**
   ```python
   def mini_batch_gd(X, y, batch_size, learning_rate, epochs):
       weights = np.zeros(X.shape[1])
       for _ in range(epochs):
           for i in range(0, len(X), batch_size):
               batch_X = X[i:i+batch_size]
               batch_y = y[i:i+batch_size]
               gradient = compute_gradient(batch_X, batch_y, weights)
               weights -= learning_rate * gradient
       return weights
   ```

## 3. Model Evaluation Metrics

### Classification Metrics
```python
def accuracy(y_true, y_pred):
    return np.mean(y_true == y_pred)

def precision(y_true, y_pred):
    true_positives = np.sum((y_true == 1) & (y_pred == 1))
    predicted_positives = np.sum(y_pred == 1)
    return true_positives / predicted_positives

def recall(y_true, y_pred):
    true_positives = np.sum((y_true == 1) & (y_pred == 1))
    actual_positives = np.sum(y_true == 1)
    return true_positives / actual_positives

def f1_score(y_true, y_pred):
    prec = precision(y_true, y_pred)
    rec = recall(y_true, y_pred)
    return 2 * (prec * rec) / (prec + rec)
```