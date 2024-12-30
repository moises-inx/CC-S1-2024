x = float(input("ingrese un valor: "))

def mifactorial (x) : 
    q=1
    c1= x>0
    c2 = x<0
    if c1 : 
        for y in range(1, x+1) : 
            x = (x*y)
            return 1
    if c2 : 
        return 1
def sumatoria(x) : 
    suma = 0
    for t in range (0,100) : 
        e = (x** t)/mifactorial(x)
    return suma

resultado = sumatoria(x)

print("El resultado de e^{x} es ", resultado)