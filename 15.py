def es_palindromo(cadena):
    cadena = cadena.replace(" ", "").lower() 
    return cadena == cadena[::-1]


texto = input("Ingresa una cadena de texto: ")

if es_palindromo(texto):
    print("La cadena es un palíndromo.")
else:
    print("La cadena no es un palíndromo.")