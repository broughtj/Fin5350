from payoffs import VanillaOption, call_payoff, put_payoff, american_binomial

spot = 41.0 
strike = 40.0
rate = 0.08
vol = 0.30
div = 0.0
expiry = 1.0
steps = 3

the_call = VanillaOption(strike, expiry, call_payoff)
price = american_binomial(the_call, spot, rate, vol, div, steps)
price2 = european_binomial(the_call, spot, rate, vol, div, steps)
print(f"The Call Option Price is: {price : 0.3f}")
