print("Diccionarios vacio")
diccionarioVacio = {}
print(diccionarioVacio)


#lista []
#tupla ()
#diccionario {}
print("Diccionarios Homogenio")
diccionarioHomogenio1 = {"David":21,
                         "Karla":19,
                         "Vanessa":21 }
diccionarioHomogenio2 = {"D":"David",
                         "K":"Karla",
                         "V":"Vanessa" }
diccionarioHomogenio3 = {"D":21,
                         "K":19,
                         "V":21 }
diccionarioHomogenio4 = {123:21,
                         456:19,
                         789:21 }
diccionarioHomogenio5 = {1:"David",
                         2:"Karla",
                         3:"Vanessa" }
print(diccionarioHomogenio1)
print(diccionarioHomogenio2)
print(diccionarioHomogenio3)
print(diccionarioHomogenio4)
print(diccionarioHomogenio5)

print("Diccionatios Heterogenios")
diccionarioHerogenio = {"Nombre":"Anderson",
                        "Apellido":"Tejada",
                        "Edad":22,
                        "Genero":True}
print(diccionarioHerogenio)

print("Diccionatios Heterogenios")
diccionarioHerogenio1 = {"Nombre":"Marisol",
                        "Apellido":"Gallardo",
                        "Edad":20,
                        "Genero":False,
                        "Nombre":"Rosa"}
print(diccionarioHerogenio1)
diccionarioHerogenio2 = {1:"Marisol",
                         2:"Gallardo",
                         3:20,
                         4:False,
                         5:"Rosa"}
print(diccionarioHerogenio2)

print("Diccionarios con diferentes tipos de llaves")
dicDiferente = {1:23,
                "a":47,
                "b":"Sara",
                2:"Hola",
                -1:"Fundamentos"
                }

print(dicDiferente)

diccionario = {"a":"Hola mundo",
               "b":23146}
print(f"La Clave a:{diccionario['a']}")
print(f"La Clave b:{diccionario['b']}")

diccionarioGrupo = {"Numeros":[1,2,3],
                    "Grupo": {"c":11,"d":"Vanessa"}}

print(f"Clave numeros: {diccionarioGrupo['Numeros']}")
print(f"Clave Grupos: {diccionarioGrupo['Grupo']}")