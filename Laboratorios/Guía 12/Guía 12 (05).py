import numpy as np

x = np.arange(101)
f = 0.5 
suma = np.sum(1 * f ** x)

print(suma)

x = np.arange(11)
y = x**2
for i in x:
    print ("la componente "+str(i)+" de y es igual a "+str(y[i]))
