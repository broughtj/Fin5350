import numpy as np
from scipy.stats import binom

class VanillaCallOption:
    def __init__(self, strike, expiry):
        self.strike = strike
        self.expiry = expiry
        
    def payoff(self, spot):
        return np.maximum(spot - self.strike, 0.0)

class VanillaPutOption:
    def __init__(self, strike, expiry):
        self.strike = strike
        self.expiry = expiry
        
    def payoff(self, spot):
        return np.maximum(self.strike - spot, 0.0)

def european_binomial(option, spot, rate, vol, div, steps):
    strike = option.strike
    expiry = option.expiry
    call_t = 0.0
    spot_t = 0.0
    h = expiry / steps
    num_nodes = steps + 1
    u = np.exp((rate - div) * h + vol * np.sqrt(h))
    d = np.exp((rate - div) * h - vol * np.sqrt(h))
    pstar = (np.exp(rate * h) - d) / ( u - d)
    
    for i in range(num_nodes):
        spot_t = spot * (u ** (steps - i)) * (d ** (i))
        call_t += option.payoff(spot_t) * binom.pmf(steps - i, steps, pstar)

    call_t *= np.exp(-rate * expiry)
    
    return call_t

if __name__ == "__main__":
    print("This is a module. Not intended to be run standalone.")