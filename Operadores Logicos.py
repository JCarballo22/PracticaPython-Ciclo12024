#Operadores de Comparación
num1 = int(input("Dijite un numero: "))
num2 = int(input("Dijite otro numero: "))
num3 = int(input("Dijite otro numero más: "))
print("\n Operador AND")
if num1 == 7 and num2 >= 4 and num3 != 3:
    print("Ambas condiciones son verdaderas.")

print("\n Operador OR")
if num1 == 7 or num2 >= 4 or num3 !=3:
    print("uno o los tres condicione cumplen con la condición.")

print("\n Operador NOT")

if not num1 > 5:
    print("La condicion a sido invertida")

if num1 < 5:
    print ("La variable es menor")



print("Fin.")