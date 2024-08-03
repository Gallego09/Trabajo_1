def media_aritmetica(numeros):
    return sum(numeros) / len(numeros) if numeros else 0

lista_numeros = [10, 20, 30, 40, 50]
print(f"La media aritmética es: {media_aritmetica(lista_numeros)}")