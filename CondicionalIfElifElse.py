print("*********************************")
print("¡¡Covertidor de numero a letras!!")
print("*********************************")

numero = int(input("¿Cual numero quieres convertir? "))

if numero == 1:
    print("El numero es 'UNO'")
elif numero == 2:
    print("El numeor es 'DOS'")
elif numero == 3:
    print("El numero es 'TRES'")
elif numero == 4:
    print("El numero es 'CUATRO'")
elif numero == 5:
    print("El numero es 'CINCO'")
else:
    print("Este programa solo puede convertir hasta el numero 5")


print("Fin.")

#otro ejemplo de if Elif
puntuacion = 50

if puntuacion >= 90:
    print("¡Excelente trabajo! Tu puntuación es A")
elif puntuacion >= 80:
    print("Buen trabajo. Tu puntuación es de B")
elif puntuacion >= 70:
    print("Tu puntuación es de C")
elif puntuacion >= 60:
    print ("Necesitas mejorar. Tu puntuación es de D")
else:
    print("Lo siento. has fallado. tu puntuación es F")

print("Fin.")

