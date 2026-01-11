import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.ar_model import AutoReg
from sklearn.linear_model import LinearRegression

def trend_component(x):
    return (x*x-250*x+125*125)/1000

def seasonal_component(x):
    return x * np.sin(2 * np.pi * x / 12)/30

def residual_component(size):
    return np.random.normal(0, 2, size)

np.random.seed(0)
time = np.arange(0, 360)
trend = trend_component(time)
seasonal = seasonal_component(time)
residual = residual_component(len(time))
data = trend + seasonal + residual

def forward_stepwise_ar(data, p_max, k_features):
    n = len(data)
    X = np.column_stack([data[p_max-i-1:n-i-1] for i in range(p_max)])
    y = data[p_max:]
    
    selected_indices = []
    remaining_indices = list(range(p_max))
    
    for _ in range(k_features):
        best_score = float('inf')
        best_idx = None
        
        for idx in remaining_indices:
            current_indices = selected_indices + [idx]
            model = LinearRegression().fit(X[:, current_indices], y)
            ssr = np.sum((y - model.predict(X[:, current_indices]))**2)
            
            if ssr < best_score:
                best_score = ssr
                best_idx = idx
        
        selected_indices.append(best_idx)
        remaining_indices.remove(best_idx)
        
    return selected_indices, LinearRegression().fit(X[:, selected_indices], y)

indices, model_greedy = forward_stepwise_ar(data, p_max=10, k_features=3)
print(f"Lag-uri selectate (Greedy): {indices}")

from sklearn.linear_model import Lasso

def lasso_ar(data, p_max, alpha=0.1):
    n = len(data)
    X = np.column_stack([data[p_max-i-1:n-i-1] for i in range(p_max)])
    y = data[p_max:]
    lasso = Lasso(alpha=alpha)
    lasso.fit(X, y)
    active_lags = np.where(np.abs(lasso.coef_) > 1e-5)[0]
    return active_lags, lasso

lags_lasso, model_lasso = lasso_ar(data, p_max=10, alpha=0.5)
print(f"Lag-uri selectate (Lasso): {lags_lasso}")

import numpy as np

def roots_companion(coeficienti):
    c = np.trim_zeros(np.array(coeficienti, dtype=float), 'f')
    
    n = len(c) - 1
    if n < 1:
        return np.array([])
    c_monic = c[1:] / c[0]
    C = np.zeros((n, n))
    if n > 1:
        C[1:, :-1] = np.eye(n - 1)
    C[0, :] = -c_monic
    roots = np.linalg.eigvals(C)
    return roots

# For P(x) = x^2 - 5x + 6 (roots: 2, 3)
coef = [1, -5, 6]
print(f"Rădăcinile sunt: {roots_companion(coef)}")