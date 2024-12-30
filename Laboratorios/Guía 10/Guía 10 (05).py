# codiciones iniciales
g = 9.8
v0 = 1 
z0 = 3

# tiempo inicial
t = 0 
zt = z0
# usar el while de está forma queda más eficiente
while zt>0 : 
    print("Los valores de la altura son: ", zt, " y los valores del tiempo son: ", t)
    t = t + 0.01
    # el orden importa
    zt = z0 + v0 * t - 0.5 * g* t**2