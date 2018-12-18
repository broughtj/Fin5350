import numpy as np

def callPayoff(spot, strike):
    return np.maximum(spot - strike, 0.0)


def ArithmeticAsianControlVariate(spot, strike, rate, vol, div, expiry, nreps, nsteps):
    paths = np.empty((nreps, nsteps + 1))
    h = expiry / nsteps
    paths[:, 0] = spot
    mudt = (mu - div - 0.5 * sigma * sigma) * h
    sigmadt = sigma * np.sqrt(h)


    astar = np.zeros(nreps)
    Gstar = 3.14


    for j in range(nreps):
        z = np.random.normal(size=nsteps)
        for t in range(1, nsteps + 1):
            z = np.random.normal(size=nreps)
            paths[j, t] = paths[j, t-1] * np.exp(mudt + sigmadt * z[t])

        spotArith = np.mean(path[j])
        spotGeo = gmean(path[j])

        astar[j] = callPayoff(spotArith, K) - (Gstar - callPayoff(spotGeo, K))


    prc = astar.mean() * np.exp(-rate * expiry)
    se = astar.std(ddof=1) / np.sqrt(nreps)

    return (prc, se)
    

    return paths
 

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
    
    
## Main
S = 41.0
K = 40.0
r = 0.08
v = 0.3
T = 1.0
q =  0.0

### Naive Monte Carlo in BSM World
paths = AssetPaths(S, r, v, T, q, 20000, 252)
callT = callPayoff(paths[:,-1], K)
se = np.std(callT, ddof=1) / np.sqrt(20000)
prc = callT.mean()
prc *= np.exp(-r * T)
print((prc, se))


### Naive Monte CArlo in BSM World for Arithmetic Asian Call
paths = AssetPaths(S, r, v, T, q, 20000, 252)
callT = callPayoff(paths.mean(axis=1), K)
se2 = np.std(callT, ddof=1) / np.sqrt(20000)
prc2 = callT.mean()
prc2 *= np.exp(-r * T)
print((prc2, se2))

### Naive Monte CArlo in BSM World for Arithmetic Asian Call
paths = AssetPaths(S, r, v, T, q, 20000, 252)
callT = callPayoff(paths.max(axis=1), K)
se3 = np.std(callT, ddof=1) / np.sqrt(20000)
prc3 = callT.mean()
prc3 *= np.exp(-r * T)
print((prc3, se3))
