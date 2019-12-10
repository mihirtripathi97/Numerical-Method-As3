import scipy as sp
import numpy as np
from scipy import integrate

def f(x):
    y = np.exp(x)
    return(y)

x = np.linspace(0,1,100,endpoint=True)
y = f(x)

I = np.trapz(y,x,dx=(x[1]-x[0]))

print("Intigration by trapazoidal rule : ",I)

I = integrate.simps(y, x,dx=(x[1]-x[0]),even='avg')

print("Intigration by simpson rule : ",I)

I = integrate.romberg(f,0,1)

print("Intigration by Romburg method : ",I)

I = integrate.fixed_quad(f, 0.0, 1.0, n=5)

print("Intigration by Gaussian quadrature method : ",I)


'''

I = integrate.simps(y,x,even='first')

print("Intigration by simpson rule : ",I)

I = integrate.simps(y,x,even='last')

print("Intigration by simpson rule : ",I)'''


