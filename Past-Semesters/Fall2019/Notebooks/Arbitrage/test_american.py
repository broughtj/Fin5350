from payoffs import VanillaOption, call_payoff, put_payoff, american_binomial, european_binomial

spot = 100.0
strike = 95.0
rate = 0.08
vol = 0.30
div = 0.0
expiry = 1.0
steps = 200

the_call = VanillaOption(strike, expiry, put_payoff)
price = american_binomial(the_call, spot, rate, vol, div, steps)
price2 = european_binomial(the_call, spot, rate, vol, div, steps)
print(f"The American Call Option Price is: {price : 0.3f}")
print(f"The European Call Option Price is: {price2 : 0.3f}")


