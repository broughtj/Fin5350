import numpy as np
from scipy.stats import binom
from scipy.stats import norm

def callPayoff(spot, strike):
        return np.maximum(spot - strike, 0.0)
       
def putPayoff(spot, strike):
        return np.maximum(strike - spot, 0.0)

class Option:
    def __init__(self, expiry, strike, payoff):
        self.__expiry = expiry
        self.__strike = strike
        self.__payoff = payoff
        
    @property
    def expiry(self):
        return self.__expiry
    
    @expiry.setter
    def expiry(self, newExpiry):
        self.__expiry = newExpiry
        
    @property
    def strike(self):
        return self.__strike
    
    @strike.setter
    def strike(self, newStrike):
        self.__strike = newStrike
        
    def payoff(self, spot):
        return self.__payoff(spot, self.__strike)  
    
    
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


def binomialPricer(option, S, r, v, q, n):
    nodes = n  + 1
    T = option.expiry
    K = option.strike
    h = T / n
    u = np.exp((r - q) * h + v * np.sqrt(h))
    d = np.exp((r - q) * h - v * np.sqrt(h))
    pstar = (np.exp((r - q) * h) - d) / (u - d)
    
    price = 0.0
    
    for i in range(nodes):
        prob = binom.pmf(i, n, pstar)
        spotT = S * (u ** i) * (d ** (n - i))
        po = option.payoff(spotT) 
        price += po * prob
    
    price *= np.exp(-r * T)
    
    return price

    


