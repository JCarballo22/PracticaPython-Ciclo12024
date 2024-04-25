#Ejemplo Bucle For Testigo
import random

print("Ejemplo Testigo")

sacarCinco = False

for i in range(3):
    dado = random.randrange(1,7)
    print(f"Tiro {i + 1}: {dado}")
    if dado == 5:
        sacarCinco = True
if sacarCinco:
    print("Ha salido al menos una vez 5")
else:
    print("No ha salido ni una vez 5")

print("Fin")

#Ejemplo For Contador
print("Ejemplo For Contador")
cuentaCinco = 0

for i in range(100):
    dado = random.randrange(1,7)
    print(f"Lanzamiento {i+1}: {dado}")
    if dado == 5:
        cuentaCinco += 1

print(f"En total a salido {cuentaCinco} cinco(s)")

print("Fin")


#Ejemplo For Acumulador

print("Bucle for Acumulador")
total = 0

for i in range(5):
    dado = random.randrange(1,7)
    print(f"Tiro {i+1}: {dado}")
    total += dado

print(f"En total se obtuvo {total} punto(s)")
print("Fin")


#Ejemplo validador de Correo
email = False
correo = input("Ingresa tu correo: ")

for i in correo:
    if i == "@" or i == ".com":
        email = True
if email == True:
    print("El correo es correcto")
else:
    print("Es incorrecto el correo")
