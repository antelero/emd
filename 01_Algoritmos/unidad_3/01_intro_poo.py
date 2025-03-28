# -*- coding: utf-8 -*-
"""
Un docente desea procesar las calificaciones de un conjunto de estudiantes de grado que toma 
uno de sus cursos. Durante el desarrollo del curso, cada participante es evaluado en tres 
instancias, obteniendo por esto 3 calificaciones. La universidad ha estipulado un régimen 
que contempla la aprobación de los cursos de grado a través de las siguientes posibilidades:
- Aprobación directa: el alumno obtiene una calificación igual o superior a 6 en cada examen.
- Aprobación indirecta: el alumno obtiene una calificación igual o mayor a 4 en cada parcial 
y promedio mayor a 6.
- No aprobación: no se cumplen las condiciones de aprobación indirecta.
Es de interés generar y mostrar por pantalla 3 listados (uno por cada condición) que incluya
 los nombres de los estudiantes que se encuentran en cada una de las condiciones antes
 mencionadas. El listado debe presentarse luego de finalizar la carga de datos de todos los 
 alumnos de interés. Considere que la finalización de la carga de datos es identificado 
 ingresando la palabra fin como nombre de un alumno.
Desarrolle una clase que represente a los estudiantes, incluyendo atributos que permitan 
almacenar su nombre y calificaciones así métodos (uno o más) que permitan saber su condición 
a partir de las notas obtenidas.
"""
class Estudiante():
    
    def __init__(self, nombre, nota1, nota2, nota3):
       self.nombre = nombre
       self.nota1 = nota1
       self.nota2 = nota2
       self.nota3 = nota3
       _promedio = 0
       
    def condicion(self):
        _promedio = (self.nota1 + self.nota2 + self.nota3) / 3
        if self.nota1 >= 6 and self.nota2 >= 6 and self.nota3 >= 6 :
            return "Aprobación directa"
        elif (self.nota1 >= 4 and self.nota2 >= 4 and self.nota3 >= 4) and _promedio >= 6:
            return "Aprobación indirecta"
        else :
            return "No aprobación"
        
def mostrarCondicion(Alumnos):
        for x in range((len(Alumnos))):
            print(Alumnos[x].nombre + " " + Alumnos[x].condicion())
        
        
def main():
   nom = input("Ingrese Nombre: ")
   Alumnos = []
   while (nom != "fin"):
       nota1 = int(input("Nota 1 "))
       nota2 = int(input("Nota 2 "))
       nota3 = int(input("Nota 3 "))
       alumno = Estudiante(nom, nota1, nota2, nota3)
       Alumnos.append(alumno)
       nom = input("Ingrese Nombre: ")
    
   print(mostrarCondicion(Alumnos) )
if (__name__ == "__main__"):
    main()
