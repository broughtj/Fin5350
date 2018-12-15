import numpy as np
from scipy.stats import norm

def blackScholesCall(spot, strike, rate, vol, div, expiry):
    d1 = (np.log(spot / strike) + (rate - div + 0.5 * vol * vol) * expiry) / (vol * np.sqrt(expiry))
    d2 = d1 - vol * np.sqrt(expiry)
    callPrice = (spot * np.exp(-div * expiry) * norm.cdf(d1)) - (strike * np.exp(-rate * expiry)  * norm.cdf(d2))
    return callPrice

def geometricAsianCall(spot, strike, rate, vol, div, expiry, N):
    dt = expiry / N
    nu = rate - div - 0.5 * vol * vol
    a = N * (N+1) * (2.0 * N + 1.0) / 6.0
    V = np.exp(-rate * expiry) * spot * np.exp(((N + 1.0) * nu / 2.0 + vol * vol * a / (2.0 * N * N)) * dt)
    vavg = vol * np.sqrt(a) / pow(N, 1.5)
    callPrice = blackScholesCall(V, strike, rate, vavg, 0, expiry)
    return callPrice

## Test BSM price
spot = 41.0
strike = 40.0
rate = 0.08
vol = 0.30
div = 0.0
expiry = 1.0
callPrice = blackScholesCall(spot, strike, rate, vol, div, expiry)
print(f"{callPrice}")
