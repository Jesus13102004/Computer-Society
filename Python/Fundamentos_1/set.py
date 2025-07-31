# De laracion de un set

my_set = {6, "Hola", True, 3.0}
print(my_set)

my_set.add("Python") # Añade el elemento "Python" al set
my_set.remove(6) # Elimina el elemento 6 del set 
my_set.discard(10) # Elimina el elemento 10 del set
my_set.pop() # Elimina un elemento aleatorio de la tupla

# Operaciones con set
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)  # Unión → {1, 2, 3, 4, 5}
print(a & b)  # Intersección → {3}
print(a - b)  # Diferencia → {1, 2}
print(a ^ b)  # Diferencia simétrica → {1, 2, 4, 5}
