import numpy as np
from option import VanillaOption, call_payoff, put_payoff
from collections import namedtuple

PricerResult = namedtuple('PricerResult', ['price', 'stderr'])

def NaiveMonteCarloPricer(option, spot, rate, vol, div, nreps):
    expiry = option.expiry
    strike = option.strike
    dt = expiry 
    disc = np.exp(-rate * dt)
    spot_t = np.empty(nreps)
    z = np.random.normal(size = nreps)

    for j in range(1, nreps):
        
        spot_t[j] = spot *  np.exp((rate - div - 0.5 * vol * vol) * dt + vol * np.sqrt(dt) * z[j])

    payoff_t = option.payoff(spot_t)

    prc = payoff_t.mean() * disc
    se = payoff_t.std(ddof=1) / np.sqrt(nreps)

    return PricerResult(prc, se)


## Main
spot = 41.0
strike = 40.0
expiry = 1.0
rate = 0.08
vol = 0.30
div = 0.0
nreps = 500000

the_call = VanillaOption(strike, expiry, call_payoff)
result = NaiveMonteCarloPricer(the_call, spot, rate, vol, div, nreps)


