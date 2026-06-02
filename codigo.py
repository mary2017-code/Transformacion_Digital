##6.2 Realiza un código corto en Python que defina una función documentada correctamente con docstrings. El tema es "calcular el promedio de una lista de números".
def calcular_promedio(lista_numeros):
    """
    Calcula el promedio de una lista de números.

    Parámetros:
        lista_numeros (list): Lista de números enteros o decimales.

    Retorna:
        float: Promedio de los números de la lista.
    """
    if len(lista_numeros) == 0:
        return 0
    return sum(lista_numeros) / len(lista_numeros)


if __name__ == "__main__":
    # Ejemplo de uso
    numeros = [10, 20, 30, 40, 50]
    promedio = calcular_promedio(numeros)
    print("El promedio es:", promedio)
