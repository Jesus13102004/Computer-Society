# Ejemplo de ciclo for

tab = 7
for i in range(1, 11):
    print(i, "*", tab, "=", i*tab)


personas = {
    "persona1": {"nombre": "Jose", "edad": 22},
    "persona2": {"nombre": "Diego", "edad": 30},
    "persona3": {"nombre": "Luis", "edad": 25}
}

for persona in personas:
    for clave in personas[persona]:
        valor = personas[persona][clave]
        print(persona, " ", clave, " ", valor)



# Ejemplo del ciclo while

i = 1
while i <= 5:
    print("Valor de i:", i)
    i += 1


j = 0
mul=8
while j <= 10:
    print(j, "*", mul, "=", j*mul)
    j += 1

