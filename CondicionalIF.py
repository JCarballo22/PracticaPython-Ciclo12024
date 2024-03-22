#Condicional IF
#Verificar si un numero es Positivo

numero = -1

if numero > 0:
    print("Tu numero es positivo")
    print("Sigo en la estructura de control")

print("Estoy fuera del IF")


print("Sistema de notas")
nombre = input ("Para iniciar, ¿Cual es su nombre?")

funPro = float(input("¿Cual es tu nota de Fundamentos?"))
mate  = float(input("¿Cual es tu nota de Matematicas?"))
ingles  = float(input("¿Cual es tu nota de Ingles?"))

promedio = (funPro + mate + ingles) / 3

if promedio >= 6:
    print(f"felidades {nombre} 'aprobastes' con un promedio de {promedio}")
    print(f'felidades {nombre} "aprobastes" con un promedio de {promedio}')

print("Fin.")