import numpy as np

class VanillaOption(object):
    def __init__(self, strike, expiry):
        self.__strike = strike
        self.__expiry = expiry
    
    @property
    def strike(self):
        return self.__strike
    
    @strike.setter
    def strike(self, new_strike):
        self.__strike = new_strike
        
    @property
    def expiry(self):
        return self.__expiry
   
    @expiry.setter
    def expiry(self, new_expiry):
        self.__expiry = new_expiry
        
    def payoff(self, spot):
        pass
    
class VanillaCallOption(VanillaOption):
    def payoff(self, spot):
        return np.maximum(spot - self.strike, 0.0)
    
class VanillaPutOption(VanillaOption):
    def payoff(self, spot):
        return np.maximum(self.strike - spot, 0.0)   
    
if __name__ == "__main__":
    print("This code is meant to be imported!")