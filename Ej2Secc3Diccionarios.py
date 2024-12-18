nombre = input("ingresa tu nombre: ")
edad = int(input("ingresa tu edad: "))
direccion = input("ingresa tu dirección: ")
telefono = input ("ingresa tu teléfono: ")

persona={"nombre":nombre, "edad":edad, "direccion":direccion, "telefono":telefono}

print(nombre + " tiene " + str(edad) +" años "+ " vive en " + direccion + " y su número de teléfono es " + str(telefono))