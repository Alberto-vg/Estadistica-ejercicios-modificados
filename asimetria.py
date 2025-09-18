# Datos
numeros =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Calcular suma total
suma = 0
for i in range(len(numeros)):
    suma = suma + numeros[i]

# Calcular media
media = suma / len(numeros)

# Calcular la suma de las desviaciones al cuadrado
suma_cuadrados = 0
for i in range(len(numeros)):
    suma_cuadrados = suma_cuadrados + (numeros[i] - media) ** 2

# Calcular varianza
varianza = suma_cuadrados / len(numeros)

# Calcular la desviación estándar
desv = varianza ** 0.5

# Calcular el numerador de la asimetría (momentos de orden 3)
suma_cubos = 0
for i in range(len(numeros)):
    suma_cubos = suma_cubos + (numeros[i] - media) ** 3
momentos_3 = suma_cubos / len(numeros)

# Calcular asimetría
asimetria = momentos_3 / (desv ** 3)

# Mostrar resultados
print("Números:", numeros)
print("Media:", media)
print("Varianza:", varianza)
print("Desviación estándar:", desv)
print("Asimetría:", asimetria)

