import numpy as np
import numpy_financial as npf


def bond_factory(face: float, coupon: float, frequency: int, maturity: int) -> np.ndarray:
    the_bond = np.full(maturity * frequency, (coupon  * face) / frequency)
    the_bond[-1] += face
    return the_bond

def bond_price(rate: float, the_bond: np.ndarray) -> float:
    disc = np.array([1.0 / ((1.0 + rate) ** i) for i in range(1, the_bond.shape[0] + 1)])
    return np.dot(disc, the_bond)


## Main 
face_value = 1000.0
coupon_rate = 0.08
freq = 2
maturity = 12
ytm = 0.075

the_bond = bond_factory(face_value, coupon_rate, freq, maturity)
the_price = bond_price(0.075/freq, the_bond)
cash_flows = np.concatenate(([-the_price], the_bond), axis=None)
the_yield = npf.irr(cash_flows)
print(f"The YTM is: {the_yield * freq:.3f}")
