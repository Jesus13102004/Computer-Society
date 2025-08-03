
tareas = {}

def añadirTarea(id):
    id = str(id)
    print("---AÑADIR TAREA---")
    descripcion = input("Ingrese la descripcion de la tarea: ")
    tareas[id] = {"descripcion":  descripcion, "completado": False}
    print(f"ID = {id} \t Descripcion = {descripcion} \t Completado: {False}")
    id = int(id)
    id = id + 1
    id = str(id)
    return id

def lista():
    for tarea in tareas:
        for clave in tareas[tarea]:
            valor = tareas[tarea][clave]
            print(tarea, clave, ":", valor)
        print("-------------------------")

def completar():
    while True:
        id = input("Ingresa el id de la tarea que deseas completar: ")

        if not id.isdigit():
            print("Error: El ID debe ser un número entero positivo.")
            continue

        if id not in tareas:
            print("Error: No existe una tarea con ese ID.")
            continue

        tareas[id] ["completado"] = True

def eliminar():
    while True:
        id = input("Ingresa el id de la tarea que quieres eliminar: ")

        if not id.isdigit():
            print("Error: El ID debe ser un número entero positivo.")
            continue

        if id not in tareas:
            print("Error: No existe una tarea con ese ID.")
            continue

        del tareas[id]

