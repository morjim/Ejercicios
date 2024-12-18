asignaturas={
    "Matematicas" : 6,
    "Fisica" : 4,
    "Quimica" : 5
}

totalCreditos=0

for asignatura in asignaturas:
    print (f"{asignatura} tiene {asignaturas[asignatura]} creditos")
    totalCreditos += asignaturas[asignatura]
print(f"total creditos {totalCreditos}")