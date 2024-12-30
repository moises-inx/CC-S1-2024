def es_primo(numero):
    if numero <= 1:
        return False
    elif numero <= 3:
        return True
    elif numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True

def imprimir_primos(hasta):
    primos = []
    for numero in range(2, hasta + 1):
        if es_primo(numero):
            primos.append(numero)
    print("Los números primos hasta", hasta, "son:", primos)

numero = int(input("Ingrese un número natural: "))
imprimir_primos(numero)