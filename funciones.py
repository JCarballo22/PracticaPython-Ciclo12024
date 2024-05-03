#Funciones dentro de Python
#print("Programando en Python")


def miFuncion():
    print("Programando en Python")

miFuncion()
miFuncion()
miFuncion()

print("Ejecutado por un bucle")

a = 0
while a <= 6:
    miFuncion()
    a += 1 

print("Fin")



def miNuevaFuncion(nombre):
    print("Tu nombre es "+ nombre)

miNuevaFuncion("Karla")
miNuevaFuncion("Marisol")
miNuevaFuncion("Sara")
miNuevaFuncion("Angel")

print("utilizando for con la funciones")
for i in ["David","Anderson","Vanessa","Brandon"]:
    miNuevaFuncion(i)

print("Fin")

def miOtraFuncion(nombre,edad):
    print(f"Su nombre es: {nombre} y su edad es: {edad}")
    print("Su nombre es:",nombre,"y su edad es:",edad)
    print("Su nombre es: {0} y su edad es: {1}".format(nombre,edad))

miOtraFuncion("Brandon",22)

#miOtraFuncion("Rosa") #Da error por que solo hay 1 argumento y requiero 2
#miOtraFuncion("Rosa",21,"F") #Da error por que solo requiere 2 argumentos y se pasan 3
miOtraFuncion("Rosa",21)#Se ejecura correctamente por que tiene los mismos parametros requeridos


def miNuevaOtraFuncion(pais = "El Salvador"):
    print("Yo soy del "+ pais)


miNuevaOtraFuncion("Mexico")
miNuevaOtraFuncion("Argentina")
miNuevaOtraFuncion()
miNuevaOtraFuncion("Honduras")
miNuevaOtraFuncion()
miNuevaOtraFuncion("España")

def miUltimaFuncion(x):
    return x*4
    #return 4*x

print(miUltimaFuncion(5))

def miFuncionPass():
    pass

miFuncionPass()