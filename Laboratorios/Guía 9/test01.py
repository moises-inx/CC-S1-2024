print("Resolveremos la ecuación a*x**2+b*x+c=0")
a = float(input("Valor de a = "))
b= float(input("Valor de b = "))
c = float(input("Valor de c = "))
x_1 = - (-b+(b**2-4*a*c)**0.5)/2*a
x_2 = + (-b-(b**2-4*a*c)**0.5)/2*a
c1 = b**2-4*a*c>0 
c2 = b**2-4*a*c==0
c3 = b**2-4*a*c<0 
if c1 :
	print(x_1, x_2)
if c2 : 
	print(x_1)
if c3 :
	print("no existe soluciones reales")

