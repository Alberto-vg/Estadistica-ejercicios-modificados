# Datos
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Ordenar los números
numeros.sort()

# Calcular mediana
n = len(numeros)
if n % 2 == 0:
    # Si la cantidad es par: promedio de los dos del centro
    mediana = (numeros[n//2 - 1] + numeros[n//2]) / 2
else:
    # Si es impar: el del centro
    mediana = numeros[n//2]

# Mostrar resultados
print("Números ordenados:", numeros)
print("Mediana:", mediana)

