usuario = "David"
contra = "12345"

i = 0
while i < 3:
    i += 1
    nombre = input("Introduce tu nombre: ")
    cont = input("Introduce tu contraseña: ")
    if usuario != nombre or contra != cont:
        print("No eres un usuario valido")
    else:
        print(f"Bienvenido usuario: '{nombre}'")
        break
else:
    print("\nSe excedio el numero de intentos")
