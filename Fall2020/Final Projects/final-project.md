## Finance 5350: Computational Financial Modeling
### __Final Project__

<br>

**Due Date:** December 18, 2020 at Midnight

<br>

## __Preliminary__


Create a Python module in a file names `options.py`. A sample file is included in the folder for this project. You will add to this module as you progress through the final project. You will import it into various notebooks that will contain your answers to the problems below.

<br>
<br>

## __Part I: The European Binomial Option Pricing Model__

<br>

Write a Jupyter notebook named `Part-One.ipynb` to solve the following problems. You should import the `options.py` module in the first code cell of the notebook as follows:

<br>

```
import options as opt
```

<br>

### __Problem 1__

* __(a)__ Complete the function `european_binomial_pricer` in the `options.py` module to implement the multiperiod European binomial option pricing model. This step is to be completed before you import the module into your notebook.

<br>

* __(b)__ Verify that it works for both call and put options with $n = 1$ (i.e. a single period). Compare against a hand-written solution. Assume the following:
    - Let $S_{0} = \$100$
    - Let $K = \$105$
    - Let $r = 8\%$
    - Let $T = 1$ year
    - Let $\delta = 0.0$ (i.e. no dividends)
    - Let $\sigma = 20\%$


<br>

* __(c)__ Verify that it works for both call and put options with $n = 3$. Compare against a hand-written solution. Use the same parameters as above in __(b)__.  

<br>

* __(d)__ What happens if you set $n = 200$? Solve for both the call and put prices. __DO NOT__ try to solve by hand! Again, use the parameter values from __(b)__.

<br>
<br>


### __Problem 2__

* __(a)__ Use the functions included in `options.py` to price the call and put option from __Problem 1__ part __(b)__ with the Black-Scholes option pricing model. See McDonald Chapter 12 for background on the Black-Scholes option pricing model.

<br>

* __(b)__ Use the `european_binomial_pricer` function with the following values: $n = 20, 40, 60, 80, \ldots, 200$ (i.e. increment by $20$). Compare to the Black-Scholes prices obtained above. Make a table to report the results. 
          What can you say about the European Bimomial model relative to the Black-Scholes model? Discuss the convergence of the European Bimomial to the Black-Scholes model.

<br>
<br>

## __Part II: The American Binomial Option Pricing Model__

<br>

Write a Jupyter notebook named `PartTwo.ipynb` to solve the following problems. You should import the `options.py` module in the first code cell of the notebook as follows:

<br>

```
import options as opt
```

<br>

### __Problem 1__

* Using the functions `european_binomial_call` and `european_binomial_put` as starting points, implement the functions `american_binomial_call` and `american_binomial_put`. These functions should solve the optimal stopping problem implicit in the American option pricing problem. Write your solutions in the `options.py` module. This step is to be completed before you import the module for the problems below. 

<br>

### __Problem 2__

* __Set-up:__ Let $S_{0} = \$100$, $K = \$95$, $r = 8\%$ (continuously compounded), $\sigma = 30\%$, $\delta = 0$, $T = 1$ year, and $n = 3$.

<br>

* __(a)__ Verify that the binomial option price for an American call option is $\$18.283$. Verify that there is never early exercise; hence a European call would have the same price. Compare your Python solution to a hand-written solution.

<br>

* __(b)__ Show that the binomial option price for a European put option is $\$5.979$. Verify that put-call parity is satisfied. 

<br>

* __(c)__ Verify that the price of an American put is $\$6.678$.

<br>

* __(d)__ Repeat each of the above for $n = 200$. How can you be sure there is never early exercise of the American call from part __(a)__? __DO NOT__ attempt to solve this part by hand! 

<br>
<br>

### __Problem 3__

* Repeat the previous problem assuming that the stock pays a continuous dividend of $8\%$ per year (continuously compounded).
* Calculate the prices of the American and European puts and calls. 
* Which options are early-exercised? Explain your answer. 
    

<br>
<br>


```python

```

## __Part III: Simulating Binomial Trees__

<br>

Write a Jupyter notebook named `PartThree.ipynb` to solve the following problems. Make sure to import the `options.py` module at the top of your notebook. You should know how to do that by now, so I won't belabor the point. 

<br>

### __Problem 1__


* Complete the function `binomial_path` in the `options.py` module that simulates a binomial path. 
* This step is to be completed prior to being imported for the problem below.
 


<br>

### __Problem 2__

* __Set-up:__ Let $S_{0} = \$100$, $r = 8\%$ (continuously compounded), $\sigma = 30\%$, $\delta = 5\%$, and $T = 1$ year.
* Set $n = 252$ (i.e. roughly the number of trading days per year so that each sub-period is a single day).
* Simulate a binomial path using your new function. 
* Use the `Matplotlib.pyplot` function `plot` to make a plot of your simulated path. Label your axes appropriately. 

<br>
<br>
