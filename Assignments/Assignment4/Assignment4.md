---
title: Finance 5350 -  Homework Assignment 4
author: Tyler J. Brough
date: \today{}
---

## Assignment 4

For this assignment your job is the implement the Black-Scholes-Merton model as part of the `dylan` option pricing
module. 

You should have already forked the `dylan` module and have a locally cloned copy of the repository.

The first step is to create a class that inherits from the `PricingEngine` abstract based class as follows:

```python
class AnalyticEngine(PricingEngine):
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


