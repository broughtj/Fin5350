from option import VanillaOption, call_payoff, put_payoff
from monte_carlo_pricers import *

spot = 41.0
strike = 40.0
rate = 0.08
vol = 0.30
div = 0.0
expiry = 1.0
steps = 10
reps = 10000

the_call = VanillaOption(strike, expiry, call_payoff)
results1 = control_variate_pricer(the_call, spot, rate, vol, div, steps, reps, 0.0)
results2 = control_variate_pricer(the_call, spot, rate, vol, div, steps, reps, -1.0)
