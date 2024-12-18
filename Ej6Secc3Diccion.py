

datos = {}

while True:
    nombre = input("Introduce tu nombre: ")
    datos["nombre"] = nombre
    print(datos)
    
    eleccion = input("¿Quieres añadir más información (S/N)? ")
    
    if eleccion.upper() == "S":
        edad = input("Introduce tu edad: ")
        datos["edad"] = edad
        print(datos)
        
        eleccion = input("¿Quieres añadir más información (S/N)? ")
        
        if eleccion.upper() == "S":
            sexo = input("Introduce tu sexo: ")
            datos["sexo"] = sexo
            print(datos)
            
            eleccion = input("¿Quieres añadir más información (S/N)? ")
            
            if eleccion.upper() == "S":
                nacionalidad = input("Introduce tu nacionalidad: ")
                datos["nacionalidad"] = nacionalidad
                print(datos)
                
                eleccion = input("¿Quieres añadir más información (S/N)? ")
    
    if eleccion.upper() != "S":
        print("Información final:", datos)
        break
    