n = int(input("Ingrese un número para saber los números primos que hay hasta ese número: "))
print("Los números primos hasta ", n, "son:")
for p in range(2, n + 1) : 
    primo = True
    for j in range(2, int(p ** 0.5)+ 1) : 
        if p%j==0 : 
            primo = False
            break
    if primo : 
        print(p)