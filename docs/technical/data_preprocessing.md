# Data Preprocessing Techniques

## 1. Feature Scaling

### Standardization (Z-score normalization)
```python
def standardize(X):
    mean = np.mean(X, axis=0)
    std = np.std(X, axis=0)
    return (X - mean) / std

def standardize_with_params(X, mean, std):
    return (X - mean) / std
```

### Min-Max Scaling
```python
def min_max_scale(X):
    min_vals = np.min(X, axis=0)
    max_vals = np.max(X, axis=0)
    return (X - min_vals) / (max_vals - min_vals)
```

## 2. Feature Engineering

### Polynomial Features
```python
def create_polynomial_features(X, degree):
    n_samples, n_features = X.shape
    poly_features = []
    
    for d in range(1, degree + 1):
        for combo in combinations_with_replacement(range(n_features), d):
            poly_features.append(np.prod(X[:, combo], axis=1))
            
    return np.column_stack(poly_features)
```

### One-Hot Encoding
```python
def one_hot_encode(X):
    unique_values = np.unique(X)
    encoding = np.zeros((X.shape[0], len(unique_values)))
    for i, value in enumerate(unique_values):
        encoding[:, i] = (X == value).astype(int)
    return encoding
```

## 3. Data Cleaning

### Handling Missing Values
```python
def handle_missing_values(X, strategy='mean'):
    if strategy == 'mean':
        return np.nan_to_num(X, nan=np.nanmean(X, axis=0))
    elif strategy == 'median':
        return np.nan_to_num(X, nan=np.nanmedian(X, axis=0))
    elif strategy == 'mode':
        mode = stats.mode(X, axis=0, nan_policy='omit')[0]
        return np.nan_to_num(X, nan=mode)
    else:
        raise ValueError('Unknown strategy')
```

### Outlier Detection
```python
def detect_outliers(X, threshold=3):
    z_scores = (X - np.mean(X, axis=0)) / np.std(X, axis=0)
    return np.abs(z_scores) > threshold
```