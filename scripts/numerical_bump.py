# Numerical example from the article; estimates are not certified bounds.
from math import exp, expm1, log, pi, sqrt
import numpy as np
from scipy.integrate import quad

def h(u):
    return exp(-1 / (1 - u*u)) if abs(u) < 1 else 0.0

def R(v):
    if abs(v) >= 2:
        return 0.0
    return quad(lambda u: h(u)*h(u+v), -1, 1,
                epsabs=1e-12, limit=200)[0]

I = quad(lambda u: h(u)*exp(u/2), -1, 1, epsabs=1e-12)[0]
R0 = R(0)
pole = 2*I*I
powers = [(2, 2), (3, 3), (4, 2), (5, 5), (7, 7)]
prime = 2*sum(log(p)/sqrt(q)*R(log(q)) for q, p in powers)

def integrand(u):
    return (2*exp(-u/2)*R(u) - 2*exp(-u)*R0) / (-expm1(-2*u))

integral = (quad(integrand, 0, 2, epsabs=1e-10, limit=200)[0]
            + quad(integrand, 2, np.inf, epsabs=1e-10)[0])
real_place = -(log(4*pi) + np.euler_gamma)*R0 - integral
print('pole:', pole, 'real:', real_place, 'prime:', -prime)
print('Q:', pole + real_place - prime)

