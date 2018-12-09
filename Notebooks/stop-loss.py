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
    

    

def stopLoss(S, K, mu, sigma, r, T, paths):
    df = np.exp(-r * np.arange(n) * h)
    covered = False
    costs = np.zeros(m)

    for k in range(m):
        path = paths[k]
        cashFlows = np.zeros(n)
        if path[0] >= K: 
            covered = True
            cashFlows[0] = -path[0]

        for t in range(1, n):
            if covered and (path[t] < K):
                covered = False
                cashFlows[t] = path[t]
            elif not covered and (path[t] > K):
                covered = True
                cashFlows[t] = -path[t]
            else:
                continue

        if (path[-1] >= K):
            cashFlows[-1] = cashFlows[-1] + K

        costs[k] = -np.dot(df, cashFlows)

    return np.mean(costs)
    
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
stopLossPrc = stopLoss(S, K, mu, v, r, T, paths)
bsmPrc = bsmCallPrice(S, K, r, v, q, T)
print(f"The BSM Call Price is: {bsmPrc : 0.4f}")
print(f"The Stop-Loss Monte Carlo Call Price is: {stopLossPrc : 0.4f}")