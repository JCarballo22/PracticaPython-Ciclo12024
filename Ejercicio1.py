print("*********************")
print("*Sistema de vaciones*")
print("*********************\n")

nomEmpleado = input("Ingrese su nombre: ")
claEmpleado = int(input("Ingrese su departamento: "))
antEmpleado = float(input("Ingrese su antiguedad: "))

if claEmpleado == 1:
    print("Atención al Cliente")
    if antEmpleado >= 1 and antEmpleado < 2:
        print("El empleado", nomEmpleado," tiene derecho 6 dias de descanso")
    
    if antEmpleado >= 2 and antEmpleado <= 7:
        print("El empleado", nomEmpleado," tiene derecho 14 dias de descanso")
    
    if antEmpleado > 7:
        print("El empleado", nomEmpleado," tiene derecho 20 dias de descanso")
    
    if antEmpleado < 1:
        print("El empleado", nomEmpleado," no tiene derecho a descanso")

if claEmpleado == 2:
    print("Ventas")
    if antEmpleado >= 1 and antEmpleado < 2:
        print("El empleado", nomEmpleado," tiene derecho 7 dias de descanso")
    
    if antEmpleado >= 2 and antEmpleado <= 7:
        print("El empleado", nomEmpleado," tiene derecho 15 dias de descanso")
    
    if antEmpleado > 7:
        print("El empleado", nomEmpleado," tiene derecho 22 dias de descanso")
    
    if antEmpleado < 1:
        print("El empleado", nomEmpleado," no tiene derecho a descanso")

if claEmpleado == 3:
    print("Gerencia")
    if antEmpleado >= 1 and antEmpleado < 2:
        print("El empleado", nomEmpleado," tiene derecho 10 dias de descanso")
    
    if antEmpleado >= 2 and antEmpleado <= 7:
        print("El empleado", nomEmpleado," tiene derecho 20 dias de descanso")
    
    if antEmpleado > 7:
        print("El empleado", nomEmpleado," tiene derecho 30 dias de descanso")
    
    if antEmpleado < 1:
        print("El empleado", nomEmpleado," no tiene derecho a descanso")

if claEmpleado <  1 or claEmpleado > 3:
    print("La clave del departamento no existe, vuelve a intentarlo")