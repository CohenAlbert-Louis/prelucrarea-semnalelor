import numpy as np

def create_hankel(data, L):
    N = len(data)
    K = N - L + 1
    X = np.zeros((L, K))
    for i in range(K):
        X[:, i] = data[i:i + L]
    return X

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
L = 40
X = create_hankel(data, L)
print(X)

U, Sigma, VT = np.linalg.svd(X, full_matrices=False)
S_cov = X @ X.T
evals, evecs = np.linalg.eigh(S_cov)
evals = evals[::-1]
evecs = evecs[:, ::-1]

# Verification: evals should be Sigma**2
print(np.allclose(evals, Sigma**2))

def ssa_decomposition(data, L, groups):
    N = len(data)
    K = N - L + 1
    X = create_hankel(data, L)
    U, Sigma, VT = np.linalg.svd(X, full_matrices=False)
    reconstructed_components = []
    
    for group in groups:
        X_group = np.zeros_like(X)
        for i in group:
            X_group += Sigma[i] * np.outer(U[:, i], VT[i, :])
        
        component = []
        for i in range(N):
            vals = []
            for r in range(L):
                c = i - r
                if 0 <= c < K:
                    vals.append(X_group[r, c])
            component.append(np.mean(vals))
        
        reconstructed_components.append(np.array(component))
        
    return reconstructed_components

groups = [[0, 1], list(range(2, L))]
components = ssa_decomposition(data, L, groups)