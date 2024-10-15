### Tuples ###

# Definición
print("***Definición de tuplas vacías***")
my_tuple = tuple()
my_other_tuple = ()

print("***Asignación de valores a my_tuple y my_other_tuple***")
my_tuple = (30, 1.77, "Nombre", "Apellido", "Segundo_nombre")
my_other_tuple = (35, 60, 30)

print(my_tuple)
print(type(my_tuple))
print("------")


# Acceso a elementos y búsqueda
print("***Acceso a elementos y búsqueda en my_tuple***")
print(my_tuple[0])
print(my_tuple[-1])
# print(my_tuple[4]) IndexError
# print(my_tuple[-6]) IndexError

print(my_tuple.count("Nombre"))
print(my_tuple.index("Apellido"))
print(my_tuple.index("Nombre"))

# my_tuple[1] = 1.80 'tuple' object does not support item assignment
print("------")
# Concatenación
print("***Concatenación de my_tuple y my_other_tuple***")
my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

# Subtuplas
print("***Obtención de una subtupla de my_sum_tuple***")
print(my_sum_tuple[3:6])

# Tupla mutable con conversión a lista
print("***Conversión de my_tuple a lista para hacerla mutable***")
my_tuple = list(my_tuple)
print(type(my_tuple))
print("------")

print("***Modificación de elementos en la lista convertida***")
my_tuple[4] = "Nombre_Marca"
my_tuple.insert(1, "Azul")
my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))
print("------")
# Eliminación
print("***Eliminación de la tupla my_tuple***")
# del my_tuple[2] TypeError: 'tuple' object doesn't support item deletion

del my_tuple
# print(my_tuple) NameError: name 'my_tuple' is not defined
print("------")
"""
1.Crear una tupla vacía
2. Crear una tupla que contenga los nombre de tus hermanos y hermanas
3.Unir ambas tuplas
4. ¿Cuántos hermanos tienes? 
5. Modificar la tupla de hermanos y agregar el nombre de tu padre y madre y asignarlo a familia_miembros

"""

# TAREA
print("***Creación de una tupla vacía***")
tuple1 = tuple()
print("------")
print("***Creación de una tupla que contenga los nombres de los hermanos***")
tuple2 = ("oscar", "raul", "maria", "juan")
print(tuple2)
print("------")
print("***Unión de ambas tuplas***")
tuple3 = tuple1 + tuple2
print(tuple3)
print("------")
print("***Conteo de hermanos***")
numero_hermanos = len(tuple2)
print(numero_hermanos)
print("------")
print("***Inicialización de tuplas vacías para hermanos y padres***")
tuple_hermanos = tuple()
tuple_hermanas = tuple()
tuple_hermanos_total = tuple()
tuple_padres = tuple()
familia_total = tuple()

print(f"Tupla hermanos: {tuple_hermanos}")
print(f"Tupla hermanas: {tuple_hermanas}")
print(f" ")

print("Asignación de nombres a las tuplas de hermanos y hermanas")
tuple_hermanos = ["Hugo", "Paco", "Luis"]
tuple_hermanas = ["Juanita", "Lulu", "Estela"]
print(f"Tupla hermanos: {tuple_hermanos}")
print(f"Tupla hermanas: {tuple_hermanas}")
print(f" ")

print("Unión de las tuplas de hermanos y hermanas")
tuple_hermanos_total = tuple(tuple_hermanos) + tuple(tuple_hermanas)
print(f"Todos mis hermanos: {tuple_hermanos_total}")
print(f" ")
print(f"Total de hermanos: {len(tuple_hermanos_total)}")

"""
En python, las tuplas son inmutables, por lo que no podemos modificar una tupla directamente
por lo que nos arroja un error de tipos en la consola.
"""
print("Creación de la tupla padres y unión con la tupla de hermanos")
padres = ("Mamá", "Papá")
familia_miembros = tuple_hermanos_total + padres
print(f"Miembros de la familia: {familia_miembros}")