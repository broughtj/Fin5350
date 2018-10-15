import numpy as np
import matplotlib.pyplot as plt

def AssetPaths(spot, mu, sigma, expiry, div, nreps, nsteps):
    paths = np.empty((nreps, nsteps + 1))
    h = expiry / nsteps
    u = np.exp((mu - div) * h + sigma * np.sqrt(h))
    d = np.exp((mu - div) * h - sigma * np.sqrt(h))
    p = (np.exp((mu - div) * h) - d) / (u - d)
    print((u, d, p))
    
    paths[:,0] = spot

    for i in range(nreps):
        w = np.random.uniform(size=nsteps)
        for j in range(nsteps):
            if w[j] >= p: 
                paths[i, j + 1] = paths[i, j] * u
            else:
                paths[i, j + 1] = paths[i, j] * d

    return paths

def plotPricePath(path):
    nsteps = path.shape[0]
    plt.plot(paths[0], 'b', linewidth = 2.5)
    plt.title("Simulated Binomial Price Path")
    plt.xlabel("Time Steps")
    plt.ylabel("Stock Price ($)")
    plt.xlim((0, nsteps))
    plt.grid(True)
    plt.show()

## main

### Basic Data
spot = 100.0
mu = 0.10
sigma = 0.30
expiry = 1.0
div = 0.0
nreps = 10
nsteps = 2500

### Get Paths and Plot One of Them 
paths = AssetPaths(spot, mu, sigma, expiry, div, nreps, nsteps)
plotPricePath(paths[0])
