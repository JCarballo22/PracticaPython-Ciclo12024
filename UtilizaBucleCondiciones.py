#Ejemplos con Funcion Range()
for x in range(6):
    print("El valor de X: ",x)

for x in range(2,6):
    print("El valor de x: ", x)

for x in range(2,30,8):
    print("Los nuevos valores de x: ",x)

for y in range(9):
    print("El valor de Y: ",y)
else:
    print("El bucle for a finalizado")

for z in range(5):
    if z == 3: break
    print("imprimir Z: ",z)
else: 
    print("bucle finalizado")


frutas = ["Banana","Manzana","Uvas","Fresas"]
animales = ["Monos","Ardillas","Conejos"]

for x in frutas:
    for y in animales:
        print(x,y)

for t in range(7):
    for q in frutas:
        for r in animales:
            print("El valor del primer bucle for: ",t,", El segundo valor del bucle for: ",q,", el valor del tercer bucle: ",r)



for d in [0,1,2]:
    pass


