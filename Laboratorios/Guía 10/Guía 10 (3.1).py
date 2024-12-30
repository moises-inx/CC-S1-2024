n = int(input("Ingrese valor de n, para calcular su factorial = "))
x=1
c1= n>0
c2 = n<0
if c1 : 
    for y in range(1, n+1) : 
        x = (x*y)
print("El factorial de n es ", x)
if c2 : 
    print("El valor ingresado no es válido")