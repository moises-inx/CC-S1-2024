z= 1
v = 24
g = 9.8 
for t in range(0,51) :
    x= t/10
    p = z + v * x - 1/2*g*x**2
    print(p)