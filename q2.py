import numpy as np
import scipy.optimize as spop

def f(x):
    y =  np.sin(np.cos(np.exp(x)))
    return(y)
def df(x):
    y = -(np.cos(np.cos(np.exp(x))))*np.sin(np.exp(x))*np.exp(x)
    return(y)

root = spop.bisect(f,-1,1,xtol=2e-12)

print("The root(by bisection) is:",root)
print("Value of function at the root found by bisection is : ",f(root))

root = spop.newton(f,-1,df)

print("The root(by NRM initial guess x=-1) is:",root)
print("Value of function at the root found by NRM is : ",f(root))

root = spop.newton(f,-0.1,df)

print("The root(by NRM initial guess x=-0.1) is:",root)
print("Value of function at the root found by NRM is : ",f(root))

root = spop.newton(f,-0.1)

print("The root(by Secant initial guess x=-0.1) is:",root)
print("Value of function at the root found by Secant is : ",f(root))








