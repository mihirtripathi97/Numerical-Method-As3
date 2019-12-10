import numpy as np
import scipy.interpolate as sp
import matplotlib.pyplot as plt

def f(x):
    y =  np.sin(np.cos(np.exp(x)))
    return(y)
def df(x):
    y = -(np.cos(np.cos(np.exp(x))))*np.sin(np.exp(x))*np.exp(x)
    return(y)

def line(x,a1):
    m=df(a1)
    c=f(a1) -a1*df(a1)
    y = m*x+c
    return(y)

x= np.linspace(-2,10,num=1000,endpoint=True)
y = f(x)

l1 = line(x,-1)
l2= line(x,0.1)


plt.plot(x,y,'b',label='Y')
plt.plot(x,l1,'r',label='line with slope dY/dx(x=-1)')
plt.plot(x,l2,'g',label='line with slope dY/dx(x=0.1)')
plt.axhline(y=0, xmin=0, xmax=10,c='k')

'''
From plot shown by this program we can see that function f has multiple roots for x>0
clearly if you look at slope at x=-1 it seems that tengent to this point will coinside at x>10
on x axes and hence next point in iteration gained from newton ralfson method can again be
anywhere and so on as in this region function behaves very oscilatory and we eventually get
root near x=9 .
But at x = 0.1 the same method will give a new x lying inside the first trough (first from left)
and hence we get a root in between -1 and 1 from newton ralphson method.

The root found by bisection is not giving 0 value when evaluated is because of round of error.
'''

plt.legend()
plt.show()
