# Datos
numeros =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Calcular suma total
suma = 0
for i in range(len(numeros)):
    suma = suma + numeros[i]

# Calcular media
media = suma / len(numeros)

# Mostrar resultados
print("Números:", numeros)
print("Suma total:", suma)
print("Media aritmética:", media)
