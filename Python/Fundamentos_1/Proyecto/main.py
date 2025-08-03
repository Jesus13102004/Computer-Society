
repetir = True
opcion = 0

while repetir==True:

    print("---GESTOR DE TAREAS---")
    print("1. Agregar Tareas")
    print("2. Ver la lista de tareas")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea por ID")
    print("5. Salir")

    try:
        opcion = int(input("Seleccione una opción: "))
    except ValueError:
        print("Ingrese un dato correcto ...")
        continue

    if opcion == 1:
        print("Tarea Agregada")
    elif opcion == 2:
        print("Mostrando la lista")
    elif opcion == 3:
        print("Tarea completada")
    elif opcion == 4:
        print("Tarea Eliminada")
    elif opcion == 5:
        print("Saliendo del programa ...")
        repetir = False
    else:
        print("Ingresa un dato valido")
        repetir = True


    while True:
        decision = input("Desea realizar otra accion: (si / no): ").lower()

        if decision == "si":
            break
        elif decision == "no":
            print("Saliendo del programa ...")
            repetir = False
            break
        else:
            print("Ingrese un valor correcto")

print("continua el codigo")





