def busqueda_binaria(lista, objetivo):
    inicio = 0
    fin = len(lista) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            inicio = medio + 1
        else:
            fin = medio - 1
    print(f"Error: el valor {objetivo} no se encuentra en la lista.")
    return None

# Ejemplo de uso
lista_ordenada = [11, 15, 23, 45, 70, 88]
objetivo = 70
resultado = busqueda_binaria(lista_ordenada, objetivo)
if resultado is not None:
    print(f'El objetivo está en el índice: {resultado}')




