import numpy as np
from payoffs import * 

strike = 40.0
expiry = 1.0
spot = 41.0
rate = 0.08
vol = 0.30
div = 0.0
steps = 200



the_call = VanillaOption(strike, expiry, call_payoff)
the_put = VanillaOption(strike, expiry, put_payoff)

call_price = european_binomial(the_call, spot, rate, vol, div, steps)
print(f"The Call Option Price is: {call_price : 0.2f}")

put_price = european_binomial(the_put, spot, rate, vol, div, steps)
print(f"The Put Option Price is: {put_price : 0.2f}")


