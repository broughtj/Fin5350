import numpy as np

def CallPayoff(spot, strike):
    return np.maximum(spot - strike, 0.0)

def HestonSimulation(params, spot, rate, div, expiry, numsteps, numreps):
    prc = np.zeros((numreps, numsteps))
    vol = np.zeros((numreps, numsteps))

    (kappa, theta, sigma, vol0, rho, lamda) = params
    dt = expiry / numsteps
    
    prc[:,0] = spot
    vol[:,0] = vol0 

    ztmp = np.random.normal(size = (numreps, numsteps))
    zv = np.random.normal(size = (numreps, numsteps))
    zs = np.zeros((numreps, numsteps))

    for i in range(1, numreps):
        ## get correlated shocks
        zs[:,i] = rho * zv[:,i] + np.sqrt(1.0 - rho * rho) * ztmp[:,i]

        ## evolve variance paths
        vol[:,i] = vol[:,i-1] + kappa * (theta - vol[:,i-1]) * dt + sigma * np.sqrt(vol[:,i-1] * dt) * zv[:,i]

        ## apply reflection to negative variances
        negvar = (vol[:,i] <= 0.0)
        vol[negvar,i] = np.abs(vol[negvar,i])

        ## evolve asset price
        prc[:,i] = prc[:,i] + np.exp((rate - div - 0.5 * vol[:,i-1]) * dt + np.sqrt(vol[:,i-1] * dt) * zs[:,i]

    ## get terminal call option payoffs
    opt = CallPayoff(prc[:,-1], strike)

    return (prc, vol, opt)

def main():
    
    



