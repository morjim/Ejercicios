'''
Almacenar las asignaturas de un curso en una lista, preguntar al usuario que nota ha sacado por asignatura y elimine de la lista las asignaturas que tengan una nota mayor a 5
'''

asignaturas=["Matemáticas", "Física", "Química", "Historia", "Lengua"]
notas=[]
asignaturasNoAprobadas=[]
print (asignaturas)
for asignatura in asignaturas:
    nota=float(input(f"¿Qué nota has sacado en {asignatura}? "))
    notas.append(nota)
    if nota>5:
       asignaturasNoAprobadas.append(asignatura)
     
print ("Asignaturas no aprobadas:", asignaturasNoAprobadas)
    