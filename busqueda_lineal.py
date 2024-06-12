def busqueda_lineal(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    print(f"Error: el valor {objetivo} no se encuentra en la lista.")
    return None

# Ejemplo de uso
lista = [10, 23, 45, 70, 11, 15]
objetivo = 70
resultado = busqueda_lineal(lista, objetivo)
if resultado is not None:
    print(f'El objetivo está en el índice: {resultado}')

