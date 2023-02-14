# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 12:46:11 2023

@author: mmlmcj
@title: Chebyshev points and Interpolants
"""

#%%
import numpy as np
import matplotlib.pyplot as plt

#%%
n = 16

# Equally spaced angles theta_j
tt = np.linspace(0, np.pi, n+1)

# Points on the upper half of the unit circle (complex plane)
zz = np.exp(1j*tt)
# Extract real and imaginary part
xx = zz.real
yy = zz.imag

# Plot
plt.figure()
plt.title("Equispaced points on the unit circle")
plt.xlabel("Real")
plt.ylabel("Imaginary")
plt.plot(xx, yy, marker='.', color='g')
plt.show()

#%%
# Chebyshev points are the real part of the numbers zz, namely xx
# Interm of the original angles we can define them as
xx2 = np.cos(tt)

# Plot
plt.figure()
plt.title("Equispaced points on the unit circle")
plt.xlabel("Real")
plt.ylabel("Imaginary")
plt.plot(xx2, yy, marker='.', color='m')
plt.show()

#%%
# NumPy can also get the Chebysev points of the second kind
# with a built in method
xx3 = np.polynomial.chebyshev.chebpts2(n+1)

# Plot
plt.figure()
plt.title("Equispaced points on the unit circle")
plt.xlabel("Real")
plt.ylabel("Imaginary")
plt.plot(xx3, yy, marker='.', color='r')
plt.show()

#%%
# Visualizing the Chebyshev points

# Plot
plt.figure()
plt.title("Equispaced points on the unit circle")
plt.xlabel("Real")
plt.ylabel("Imaginary")
plt.plot(xx, yy, marker='.')
plt.plot(xx, np.zeros_like(xx), marker='.')
plt.show()

