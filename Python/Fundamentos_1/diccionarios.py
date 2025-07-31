# Declaracion de Diccionario

persona = {
    "nombre": "Juan",
    "edad": 20,
    "ciudad": "Mexico"
}

persona["nombre"] = "Francisco"
persona["calificacion"] = 10

personas = {
    "persona1": {"nombre": "Jose", "edad": 22},
    "persona2": {"nombre": "Diego", "edad": 30},
    "persona3": {"nombre": "Luis", "edad": 25}
}

print(personas["persona1"]["nombre"])
