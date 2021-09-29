#!/usr/bin/env python
# coding: utf-8

# # Operaciones Matemáticas

# ## 1 - Suma
# Variables numericas int
x = 3 
y = 4
z = x+y
print(z)


# ## 2 - Resta
# Variables int
x = 5
y = 10
z = x - y
print(z)


# ## 3 - Multiplicación
# Variable float
x = 8.9
y = 7
z = x * y
print (z)


# ## 4 - División
# Variable float
x = 9
y = 8
z = x / y
print(z)


# # Transformaciones
# De float a int
x = 3.141656569465 #Float
x = int(x)
print(x)

# De String a float
a = "35.5"
print(float(a))


# # Operaciones con Strings
# ## Lógica con String
# Variables numéricas con respuesta que se imprime en String
a = 9
b = 10
if a > b:
    print("El ganador es a")
else:
    print("El ganador es b")

# Variable String en logica
a = 'Hola '
b = 'Mundo.'
z = a + b
print(z)

# ## Booleans
# Lógica True y False
x = 10
y = 11
print(bool(x==y))


a = 5
b = 10
print(bool(a < b))


q = 0
print(bool(q)) 
w = 4
print(bool(w))
e = -94.15
print(bool(e))
