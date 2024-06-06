print("Listas Anidadas")

lista = [1,"a",True,[2,"b",False, [3,"c",True]]]
print(lista)

print(lista[0])
print(lista[3][2])
print(lista[3][3][2])

matris = [[1,2,3],
          [4,5,6],
          [7,8,9]]

print(matris[0])
print(matris[1])
print(matris[2])

#mostrar el numero 1
print(matris[0][0])
print(matris[1][0])
print(matris[2][1])
print(matris[0][2])

Matrix = [[[1,2,3],[4,5,6],[7,8,9]],
          [[10,11,12],[13,14,15],[16,17,18]],
          [[19,20,21],[22,23,24],[25,26,27]]]

print(Matrix[1][0][2])


print("Mostrar elementos de la lista fila por fila")
for fila in matris:
    print(fila)

print("Mostrar elementos a elemento")
for fila in matris:
    for columnas in fila:
        print(columnas)

print(matris[0][2])

print("Mostrar elementos a elemento")
for fila in matris:
    for columnas in fila:
        print(columnas, end=" ")
print()
for fila in Matrix:
    for columna in fila:
        for elemento in columna:
            print(elemento, end=", ")