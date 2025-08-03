def saludar(nombre):
    print("Hola", nombre)

saludar("Jorge")  # Llama a la función con el argumento "Jorge"


def multiplicar(num):
    for i in range(1, 11):
        print(i, "*", num, "=", i*num)

multiplicar(5)
multiplicar(10)
multiplicar(3)