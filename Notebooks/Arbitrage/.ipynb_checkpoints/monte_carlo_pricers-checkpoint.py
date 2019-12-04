import numpy as np
from scipy.stats import norm
from collections import namedtuple


PricerResult = namedtuple('PricerResult', ['price', 'stderr'])

def BlackScholesDelta(spot, t, strike, expiry, volatility, rate, dividend):
    tau = expiry - t
    d1 = (np.log(spot/strike) + (rate - dividend + 0.5 * volatility * volatility) * tau) / (volatility * np.sqrt(tau))
    delta = np.exp(-dividend * tau) * norm.cdf(d1) 
    return delta

def naive_pricer(option, spot, rate, vol, div, steps, reps):
    pass

def control_variate_pricer(option, spot, rate, vol, div, steps, reps, beta):
    expiry = option.expiry
    strike = option.strike
    dt = expiry / steps
    nudt = (rate - div - 0.5 * vol * vol) * dt
    sigsdt = vol * np.sqrt(dt)
    erddt = np.exp((rate - div) * dt)    
    cash_flow_t = np.zeros(reps)
    price = 0.0

    for j in range(reps):
        spot_t = spot
        convar = 0.0
        z = np.random.normal(size=int(steps))

        for i in range(int(steps)):
            t = i * dt
            delta = BlackScholesDelta(spot, t, strike, expiry, vol, rate, div)
            spot_tn = spot_t * np.exp(nudt + sigsdt * z[i])
            convar = convar + delta * (spot_tn - spot_t * erddt)
            spot_t = spot_tn

        cash_flow_t[j] = option.payoff(spot_t) + beta * convar

    prc = np.exp(-rate * expiry) * cash_flow_t.mean()
    se = np.std(cash_flow_t, ddof=1) / np.sqrt(reps)
    
    return PricerResult(prc, se)