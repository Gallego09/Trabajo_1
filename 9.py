filas = 3
columnas = 4
matriz = [[(j + i * columnas + 1) for j in range(columnas)] for i in range(filas)]

for fila in matriz:
    print(fila)