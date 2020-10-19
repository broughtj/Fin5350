import numpy as np

def bond_factory(face: float, coupon: float, frequency: int, maturity: int) -> np.ndarray:
    the_bond = np.full(maturity * frequency, (coupon  * face) / frequency)
    the_bond[-1] += face
    return the_bond

def bond_price(rate: float, the_bond: np.ndarray) -> float:
    disc = np.array([1.0 / ((1.0 + rate) ** i) for i in range(1, the_bond.shape[0] + 1)])
    return np.sum(disc * the_bond)


## main
face_value = 1000.0
coupon_rate = .10
frequency = 2
maturity = 20
ytm = .12 / frequency

the_bond = bond_factory(face_value, coupon_rate, frequency, maturity)
the_price = bond_price(ytm, the_bond)
print(f"The bond price is: ${the_price:,.2f}")