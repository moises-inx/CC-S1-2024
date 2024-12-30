z= float(input("Defina el valor de z= "))
v = float(input("Defina el valor de v = "))
g = 9.8
for t in range(0,51) :
    x= t/10
    print(x)
    p = z + v * x - 1/2*g*x**2
    print(p)
