# Datos
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Calcular la media
suma = 0
for i in range(len(numeros)):
    suma = suma + numeros[i]
media = suma / len(numeros)

# Calcular la varianza 
suma_cuadrados = 0
for i in range(len(numeros)):
    suma_cuadrados = suma_cuadrados + (numeros[i] - media) ** 2
varianza = suma_cuadrados / len(numeros)

# Desviación estándar
desv = varianza ** 0.5

# Calcular el numerador de la curtosis 
suma_cuartos = 0
for i in range(len(numeros)):
    suma_cuartos = suma_cuartos + (numeros[i] - media) ** 4
momentos_4 = suma_cuartos / len(numeros)

# Curtosis 
curtosis = (momentos_4 / (desv ** 4)) - 3

# Mostrar resultados
print("Números:", numeros)
print("Media:", media)
print("Varianza:", varianza)
print("Curtosis:", curtosis)

