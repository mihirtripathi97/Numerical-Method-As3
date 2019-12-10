import numpy as np
import scipy.interpolate as sp
import matplotlib.pyplot as plt
x= np.linspace(0,5,num=6,endpoint=True)
y=np.array([1.0,2.0,1.0,0.5,4.0,8.0])

spl = sp.InterpolatedUnivariateSpline(x,y,k=1)
qdspl = sp.InterpolatedUnivariateSpline(x,y,k=2)
cbspl = sp.CubicSpline(x,y)
lp = sp.lagrange(x,y)


#printing the polynomial
print("The langrange polynomial is : ", lp[0]," + (",lp[1],")x + (",lp[2],") x^2 + (",lp[3]," ) x^3 +(",lp[4],")x^4 + (",lp[5],") x^5")

xsp = np.linspace(0.0,5.0,1000,endpoint=True)
plt.plot(x,y,'b',marker='o',label='Y')
plt.plot(xsp,spl(xsp),'r',label='Linear SplineY')
plt.plot(xsp,qdspl(xsp),'y',label='Quadratic SplineY')
plt.plot(xsp,cbspl(xsp),'g',label='Cubic SplineY',linestyle="--")
plt.plot(xsp,lp(xsp),'k',label='Lagrange polynomial')

plt.xlabel('X')
plt.ylabel('Y')

plt.title('Spline interpolation')

plt.legend()
plt.show()
