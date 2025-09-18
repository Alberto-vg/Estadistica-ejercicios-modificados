# Datos
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Calcular la media
suma = 0
for i in range(len(numeros)):
    suma = suma + numeros[i]
media = suma / len(numeros)

# Calcular la suma de las desviaciones al cuadrado
suma_cuadrados = 0
for i in range(len(numeros)):
    suma_cuadrados = suma_cuadrados + (numeros[i] - media) ** 2

# Calcular varianza
varianza = suma_cuadrados / len(numeros)

# Mostrar resultados
print("Números:", numeros)
print("Media:", media)
print("Varianza:", varianza)

