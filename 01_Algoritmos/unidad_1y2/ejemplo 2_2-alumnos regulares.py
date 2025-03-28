# -*- coding: utf-8 -*-
"""
Hagamos un ejercicio, en uno de los ejemplos ya considerados calculamos 
el promedio de calificaciones obtenidas por un estudiante. 
La implementación en python es la que se encuentra a continuación. 
Realice las modificaciones necesarias a fin de que se presente 
un mensaje indicando si el estudiante ha alcanzado la condición de alumno 
regular (promedio de calificaciones mayor o igual a 4).

"""
print("Ingrese las 3 calificaciones:")
nota_1 = int(input("Primera: "))
nota_2 = int(input("Segunda: "))
nota_3 = int(input("Tercera: "))
prom = (nota_1 + nota_2 + nota_3)  / 3
print(f"La calificación promedio es {prom:.2f}")
if prom>= 4:
    print(f"PROMOCIONO con promedio {prom:.2f}")
else:
    print(f"No le dio el promedio {prom:.2f}")