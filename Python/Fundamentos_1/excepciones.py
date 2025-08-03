try:
    numero = int(input("Dame un número: "))
    resultado = 10 / numero
    print("Resultado:", resultado)
except ZeroDivisionError:
    print("No se puede dividir entre cero.")
except ValueError:
    print("Eso no es un número.")
