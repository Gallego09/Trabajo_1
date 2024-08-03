num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

suma = num1 + num2
resta = num1 - num2
multiplicación = num1 * num2
división = num1 / num2 if num2 != 0 else "División por cero no permitida"

print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicación}")
print(f"División: {división}")