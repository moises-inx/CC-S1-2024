x = float(input("Ingrese un valor: "))

def mifactorial(n):
    if n == 0:
        return 1
    else:
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i
        return factorial

def sumatoria(x):
    suma = 0
    for t in range(100): 
        suma += (x ** t) / mifactorial(t)
    return suma

resultado = sumatoria(x)

print(f"El resultado de e^{x} es {resultado}")
