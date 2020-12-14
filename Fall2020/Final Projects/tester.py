import options as opt

args = {'spot': 41.0, 'strike': 40.0, 'expiry': 0.25, 'rate': 0.08, 'div': 0.0, 'vol': 0.3}
the_call = opt.black_scholes_call(**args)
print(f"The BSM call price is: {the_call : 0.3f}")

the_put = opt.black_scholes_put(**args)
print(f"The BSM put price is: {the_put : 0.3f}")


args = {'spot': 100.0, 'strike': 105.0, 'expiry': 1.0, 'rate': 0.08, 'div': 0.0, 'vol': 0.2}
the_call = opt.black_scholes_call(**args)
print(f"The BSM call price is: {the_call : 0.3f}")

the_put = opt.black_scholes_put(**args)
print(f"The BSM put price is: {the_put : 0.3f}")

args = {'spot': 100.0, 'strike': 105.0, 'expiry': 1.0, 'rate': 0.08, 'div': 0.0, 'vol': 0.2, 
        'num': 3, 'payoff': opt.call_payoff}
D = opt.binomial_delta(**args)
        
