print("Resolveremos la ecuación a*x**2+b*x+c=0")
a = float(input("Valor de a = "))
b= float(input("Valor de b = "))
c = float(input("Valor de c = "))
x_1 = - (-b+(b**2-4*a*c)**0.5)/2*a
x_2 = + (-b-(b**2-4*a*c)**0.5)/2*a
print("El valor de x_1 es ",x_1," y el valor de x_2 es ", x_2 )

