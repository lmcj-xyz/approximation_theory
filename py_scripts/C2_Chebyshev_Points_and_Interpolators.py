# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 12:46:11 2023

@author: mmlmcj
@title: Chebyshev points and Interpolants
"""

import numpy as np
import matplotlib.pyplot as plt

n = 16

# Equally spaced angles theta_j
tt = np.linspace(0, np.pi, n+1)

# Points on the upper half of the unit circle (complex plane)
zz = np.exp(1j*tt)
# Extract real and imaginary part
xx1 = zz.real
yy = zz.imag

# Plot
plt.figure(num="eq_p_1")
plt.title("Equispaced points on the unit circle \n obtained by extracting real part")
plt.xlabel("Real")
plt.ylabel("Imaginary")
plt.plot(xx1, yy, marker='.', color='g')
plt.show()

# Chebyshev points are the real part of the numbers zz, namely xx
# Interm of the original angles we can define them as
xx2 = np.cos(tt)

# Plot
plt.figure(num="eq_p_2")
plt.title("Equispaced points on the unit circle \n obtained by computing the cos of the angles")
plt.xlabel("Real")
plt.ylabel("Imaginary")
plt.plot(xx2, yy, marker='.', color='m')
plt.show()

# NumPy can also get the Chebysev points of the second kind
# with a built in method
xx3 = np.polynomial.chebyshev.chebpts2(n+1)

# Plot
plt.figure(num="eq_p_3")
plt.title("Equispaced points on the unit circle \n obtained with built in NumPy method")
plt.xlabel("Real")
plt.ylabel("Imaginary")
plt.plot(xx3, yy, marker='.', color='r')
plt.show()

# Visualizing the Chebyshev points

# Plot
plt.figure(num="eq_p_4")
plt.title("Equispaced points on the unit circle \n visualizin Chebyshev points on the x axis")
plt.xlabel("Real")
plt.ylabel("Imaginary")
plt.plot(xx1, yy, marker='.')
plt.plot(xx1, np.zeros_like(xx1), marker='.')
plt.show()

# Some points to work with
xx = np.linspace(-1, 1, 1000)
# Defining some functions to find their interpolators
f = lambda x: np.sign(x) - x/2
g = lambda x: np.sin(6*x) + np.sign(np.sin(x + np.exp(2*x)))
# Interpolators coefficients of degree 5 and 25 for f
interp_f_5 = np.polynomial.chebyshev.chebinterpolate(f, 5)
interp_f_25 = np.polynomial.chebyshev.chebinterpolate(f, 25)
# Interpolator coefficients of degree 100 for g
interp_g_100 = np.polynomial.chebyshev.chebinterpolate(g, 100)
# Function evaluation on points
f_eval = f(xx)
g_eval = g(xx)
# Evaluating the interpolators on the points
cheb_eval_f_5 = np.polynomial.chebyshev.chebval(xx, interp_f_5)
cheb_eval_f_25 = np.polynomial.chebyshev.chebval(xx, interp_f_25)
cheb_eval_g_100 = np.polynomial.chebyshev.chebval(xx, interp_g_100)

# Visualisation of f and its degree 5 interpolant
plt.figure(num="interp_1")
plt.title(r"Degree 5 Chebyshev interpolant for $f = sign(x) - x/2$")
plt.plot(xx, f_eval, color='b')
plt.plot(xx, cheb_eval_f_5, color='y')
plt.show()

# Visualisation of f and its degree 25 interpolant
plt.figure(num="interp_2")
plt.title(r"Degree 25 Chebyshev interpolant for $f = sign(x) - x/2$")
plt.plot(xx, f_eval, color='m')
plt.plot(xx, cheb_eval_f_25, color='g')
plt.show()

# Visualisation of g and its degree 100 interpolant
plt.figure(num="interp_3")
plt.title(r"Degree 100 Chebyshev interpolant for $f = \sin(6x) + sign(\sin(x + e^{2x}))$")
plt.plot(xx, g_eval, color='r')
plt.plot(xx, cheb_eval_g_100, color='c')
plt.show()

# Random data
rng = np.random.default_rng(12345) # The seed is to make it reproducible
rn_data = 2*rng.uniform(size=100) - 1
x2 = np.linspace(start=-1, stop=1, num=100)
# Fit Chebyshev interpolant
cheb_coeff_random = np.polynomial.chebyshev.chebfit(x=x2, y=rn_data, deg=100)
# Evaluate the interpolant
cheb_fit_random = np.polynomial.chebyshev.chebval(x2, cheb_coeff_random)

# Plot
plt.figure(num="interp_4")
plt.title("Chebyshev interpolant through random data")
plt.scatter(x2, rn_data, color='b', marker='.', label='Random points')
plt.plot(x2, cheb_fit_random, color='c', label='Interpolant')
plt.legend()
plt.show()