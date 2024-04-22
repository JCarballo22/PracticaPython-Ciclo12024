#Ejemplo

contador = 0

while contador <= 10:
    print("El valor actual de X es: ", contador)
    contador += 5
print("Fin.")

fruta = "Naranja"
contador2 = 0

while fruta != "Naranja":
    print("La fruta tiene que ser naranja")
    print(contador2)
    contador2 += 1
    if contador2 == 300:
        break
else:
    print("Por fin escojistes naranja")


print("Fin")

