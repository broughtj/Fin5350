---
title: Finance 5350 -  Homework Assignment 4
author: Tyler J. Brough
date: \today{}
---

## Assignment 4


### Problem 1

For this assignment your job is the implement the Black-Scholes-Merton model as part of the `dylan` option pricing
module. 

You should have already forked the `dylan` module and have a locally cloned copy of the repository.

The first step is to create a class that inherits from the `PricingEngine` abstract based class as follows:

```.python
class BlackScholesMertonEngine(PricingEngine):
	def __init__(self, payoff_type, pricer):
		self.__payoff_type = payoff_type
		self.__pricer = pricer

	@property
	def payoff_type(self):
		return self.__payoff_type

	@payoff_type.setter
	def payoff_type(self, new_payoff_type):
		self.__payoff_type = new_payoff_type

	def calculate(self, option, data):
		return self.__pricer(self, option, data)
```

The next step is write a function that we can use with the *Strategy Pattern* to do the actual implementation of the
Black-Scholes-Merton model. It should look something like  this:

```.python
def BlackScholesMertonPricer(pricing_engine, option, data):
	## Your code goes here!
	return price
```

Where you will replace the comment `### Your code goes here!` with the actual code required to implement the model.

Once you have created the function `BlackScholesMertonPricer`, also create the following methods within the class:

- `Delta` 

- `Gamma`

- `Vega`

- `Theta`

- `Rho`

- `Psi`

Where each method implements the appropriate BlackScholesMerton Greek formula (see McDonald Chapter 12). 

Also, please create a Jupyter notebook that reproduces figures 12.1 through 12.10 of McDonald Chapter 12, as well as
reproduces Table 12.2.


### Problem 2


