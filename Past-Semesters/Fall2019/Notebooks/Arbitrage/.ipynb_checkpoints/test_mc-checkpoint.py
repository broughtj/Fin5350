import numpy as np
from option import VanillaOption, call_payoff, put_payoff
from pricers import naive_monte_carlo_pricer, stratified_monte_carlo_pricer
import matplotlib.pyplot as plt

spot = 41.0
strike = 40.0
rate = 0.08
vol = 0.30
div = 0.0
expiry = 1.0
steps = 10
reps = 500
M = 1000

vals1 = np.zeros(M)
vals2 = np.zeros(M)
the_call = VanillaOption(strike, expiry, call_payoff)

for i in range(M):
    results1 = naive_monte_carlo_pricer(the_call, spot, rate, vol, div, reps)
    vals1[i] = results1.price
    #print(f"The call option price via Naive Monte Carlo is: {results1.price : 0.4f}, with standard error: {results1.stderr: 0.4f}")
    
    results2 = stratified_monte_carlo_pricer(the_call, spot, rate, vol, div, reps)
    vals2[i] = results2.price
    #print(f"The call option price via Stratified Monte Carlo is: {results2.price : 0.4f}, with standard error: {results2.stderr: 0.4f}")
    
    
plt.hist(vals1, bins=25);
print(np.std(vals1))
plt.hist(vals2, bins=25);
print(np.std(vals2))