#Estrutura condicional anidada
edad = 19

if edad >= 18:
    print("Eres mayor de edad")
else:
    if edad >= 13:
        print("Eres un adolecente")
    else:
        print("Eres un niño")

print("Fin.")

print("=================")
print("Convertir semana")
print("=================")

print("Menú de Opciones")
print("Presione 1 para convertir de numero a dia de la semana")
print("Presione 2 para convertir de dia de la semana a numero")

opcion = int(input("¿Cúal es tu opcion deseada: "))

if opcion == 1:
    print("\n Conversor de numeor a día de la semana")

    opcion1 = int(input("Cual es el numero de la semana: "))
    if opcion1 == 1:
        print("Lunes")
    elif opcion1 == 2:
        print("Martes")
    elif opcion1 == 3:
        print("Miercoles")    
    elif opcion1 == 4:
        print("Jueves")
    elif opcion1 == 5:
        print("Viernes")
    elif opcion1 == 6:
        print("Sábado")
    elif opcion1 == 7:
        print("Domingo")
    else:
        print("El numero no corresponde al de un dia de la semana")

elif opcion == 2:
    print("\n convertir de dia de la semana a numero")

    opcion2 = input("¿Cual es el dia de la semana en numero?")
    if opcion2 == "Lunes":
        print(1)
    elif opcion2 == "Martes":
        print(2)
    elif opcion2 == "Miercoles":
        print(3)
    elif opcion2 == "Jueves":
        print(4)
    elif opcion2 == "Viernes":
        print(5)
    elif opcion2 == "Sábado":
        print(6)
    elif opcion2 == "Domingo":
        print(7)
    else:
        print("El dia de la semana no existe")

else:
    print("El numero de opcion seleccionado no es valido")
