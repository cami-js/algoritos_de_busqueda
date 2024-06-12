import time
import random
from busqueda_lineal import busqueda_lineal
from busqueda_binaria import busqueda_binaria

# Función para medir el tiempo de ejecución
def medir_tiempo(func, lista, objetivo):
    inicio = time.time()
    resultado = func(lista, objetivo)
    fin = time.time()
    return resultado, fin - inicio

# Crear una lista grande de elementos aleatorios
lista_grande = random.sample(range(1, 1000000), 100000)
lista_grande_ordenada = sorted(lista_grande)

# Prueba con búsqueda lineal
objetivo = random.choice(lista_grande)
resultado_lineal, tiempo_lineal = medir_tiempo(busqueda_lineal, lista_grande, objetivo)
if resultado_lineal is not None:
    print(f'Búsqueda Lineal - Resultado: {resultado_lineal}, Tiempo: {tiempo_lineal:.6f} segundos')

# Prueba con búsqueda binaria (necesita lista ordenada)
resultado_binaria, tiempo_binaria = medir_tiempo(busqueda_binaria, lista_grande_ordenada, objetivo)
if resultado_binaria is not None:
    print(f'Búsqueda Binaria - Resultado: {resultado_binaria}, Tiempo: {tiempo_binaria:.6f} segundos')

