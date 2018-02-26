# -*- coding: utf-8 -*-

name = str(raw_input('¿Cuál es tu nombre?'))
print('Hola, ' + name + '!')
print('===========')

my_string = 'Platzi'
print(my_string.upper())
print(my_string.lower())
print(my_string.find('i'))
print(my_string[5])
print(my_string[1:])
print(my_string[1:3])
print(my_string[1:5:2])
print(my_string[::-1])
print('===========')

for i in range(2):
    print(i)

print('===========')
for i in range(30):
    if i % 3 != 0:
        continue
    else:
        print(i**2)

print('===== For ======')
for i in range(30):
    if i % 3 == 0:
        print(i)
    elif i == 22:
        break

print('===== While ======')
i = 0
while i < 3:
    print(i)
    i += 1

print('===== Dictionary ======')
mi_diccionario = {}
mi_diccionario['primer_elemento'] = 'Hola'
mi_diccionario['segundo_elemento'] = 'Adios'
print(mi_diccionario['primer_elemento'])

print('===========')
calificaciones = {}
calificaciones['algoritmos'] = 9
calificaciones['matematicas'] = 10
calificaciones['web'] = 8
calificaciones['bases_de_datos'] = 10
suma_cal = 0
for key in calificaciones:
    print(key)
for value in calificaciones.values():
    suma_cal += value
    print(value)
for key, value in calificaciones.iteritems():
    print('Llave: {}, valor: {}'.format(key, value))

promedio = suma_cal / len(calificaciones)

print('Preomedio de calificaciones {}'.format(promedio))

print('===== TUPLE ======')
mi_tupla = (1,2,3)

print('===== SET ======')
s = set([1,2,3])
t = set([3,4,5])

print(s.union(t))
print(s.intersection(t))
print(s.difference(t))
print(t.difference(s))
print(1 in s)

print('===== Dictionary comprehension ======')
pares = []
for num in range(1, 31):
    if num % 2 == 0:
        pares.append(num)

print(pares)

even = [num for num in range(1, 31) if num % 2 == 0]
print(even)

cuadrados = {}
for num in range(1, 11):
    cuadrados[num] = num**2
print(cuadrados)

squares = {num: num**2 for num in range(1,11)}
print(squares)