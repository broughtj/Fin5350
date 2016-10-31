import numpy as np

def EuropeanBinomialPricer(option, spot, rate, sigma, steps):
    expiry = option.expiry
    h = expiry / steps
    nodes = steps
    u = np.exp(rate * h + sigma * np.sqrt(h))
    d = np.exp(rate * h - sigma * np.sqrt(h))
    pstar = (np.exp(rate * h) - d) / (u - d)
    total = 0.0
    disc = np.exp(-rate * expiry)

    for i in range(nodes):
        spotT = spot * (u ** (steps - i)) * (d ** (i))
        callT = option.payoff(spotT)
        probT = binom.pmf(steps - i, steps, pstar)
        total += callT * probT
        
    return disc * total