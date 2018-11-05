import numpy as np
from scipy.stats import norm

def bsmCallPrice(S, K, r, v, q, T):
    d1 = (np.log(S/K) + (r - q + 0.5 * v * v) * T) / (v * np.sqrt(T))
    d2 = (np.log(S/K) + (r - q - 0.5 * v * v) * T) / (v * np.sqrt(T))
    callPrc = S * np.exp(-q * T) * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    
    return callPrc

def bsmPutPrice(S, K, r, v, q, T):
    d1 = (np.log(S/K) + (r - q + 0.5 * v * v) * T) / (v * np.sqrt(T))
    d2 = (np.log(S/K) + (r - q - 0.5 * v * v) * T) / (v * np.sqrt(T))
    putPrc =  K * np.exp(-r * T) * norm.cdf(-d2) - S * np.exp(-q * T) * norm.cdf(-d1)
    
    return putPrc  

def bsmCallDelta(S, K, r, v, q, tau):
    d1 = (np.log(S/K) + (r - q + 0.5 * v * v) * T) / (v * np.sqrt(T))
    
    return np.exp(-q * T) * norm.cdf(d1)

def AssetPaths(spot, mu, sigma, expiry, div, nreps, nsteps):
    paths = np.empty((nreps, nsteps + 1))
    h = expiry / nsteps
    paths[:, 0] = spot
    mudt = (mu - div - 0.5 * sigma * sigma) * h
    sigmadt = sigma * np.sqrt(h)
    
    for t in range(1, nsteps + 1):
        z = np.random.normal(size=nreps)
        paths[:, t] = paths[:, t-1] * np.exp(mudt + sigmadt * z)

    return paths

def deltaHedging(S, K, mu, sigma, r, T, paths):
    m, n = paths.shape
    cost = np.zeros(m)
    cashFlows = np.zeros(n)
    h = T / n
    df = np.exp(-r * np.arange(n) * h)
    tau = T - np.arange(n) * h
    
    for k in range(m):
        path = paths[k]
        position = 0.0
        deltas = bsmCallDelta(path, K, r, v, q, tau)
        
        for t in range(n):
            cashFlows[t] = (position - deltas[t]) * path[t]
            position = deltas[t]
            
        if (path[-1] >= K):
            cashFlows[-1] = K - (1 - position) * path[-1]
        else:
            cashFlows[-1] = position * path[-1]
        
        cost[k] = -np.dot(df, cashFlows)
        
    return np.mean(cost)

## main
S = 50.0
K = 50.0
r = 0.05
mu = 0.10
v = 0.40
q = 0.0
T = 5.0 / 12.0
m = 100000
n = 110
h = T / n

paths = AssetPaths(S, mu, v, T, q, m, n)
delHdgPrc = deltaHedging(S, K, mu, v, r, T, paths)
bsmPrc = bsmCallPrice(S, K, r, v, q, T)
print(f"The BSM Call Price is: {bsmPrc : 0.4f}")
print(f"The Delta-Hedging Monte Carlo Call Price is: {delHdgPrc : 0.4f}")
