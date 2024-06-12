import os

empleados = []

while True:
    print("Menú")
    print("1. Registrar trabajador")
    print("2. Listar todos los trabajadores")
    print("3. Imprimir plantilla de sueldos ")
    print("4. Salir del programa ")
    opc = int(input("Ingrese opción: "))
    
    if opc == 1:
        print("Registrar Trabajador")
        nombre = input("Ingrese nombre: ")
        apellido = input("Ingrese apellido: ")
        cargo = input("Ingrese su cargo: ")
        sueldo = int(input("Ingrese su sueldo bruto: "))
        empleados.append({
            'nombre': nombre,
            'apellido': apellido,
            'cargo': cargo,
            'sueldo': sueldo
        })
    elif opc == 2:
        print("Listar todos los trabajadores")
        for x in empleados:
            print(f"NOMBRE: {x['nombre']}, APELLIDO: {x['apellido']}, CARGO: {x['cargo']}, SUELDO: {x['sueldo']}")
    elif opc == 3:
        print("Imprimir plantilla de sueldos")
    elif opc == 4:
        print("Hasta luego!")
        break
    else:
        print("Opción no válida")
