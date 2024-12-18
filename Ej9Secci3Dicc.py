clientes={}
opcion =''

while opcion != 6:
    opcion = input('Menú de opciones\n(1) Añadir cliente\n(2) Eliminar cliente\n(3) Mostrar cliente\n(4) Listar clientes\n(5) Listar clientes vip\n(6) Terminar\nElige una opción:')
    if opcion == 1:
        nif = input("Ingrese su NIF: ")
        nombre = input(" Ingrese su nombre: ")
        direccion = input("Introduce su dirección")
        telefono = input("Introduce su telefono")
        correo = input("Introduce su correo")
        vip = input("¿Es VIP ? (S/N)")
        cliente ={
            "nif": nif,
            "nombre": nombre,
            "direccion":direccion,
            "telefono":telefono,
            "correo":correo,
            "vip":vip.upper()=='S'
        }
        clientes[nif]=cliente
    if opcion ==2:
        nif = input("Ingrese su NIF: ")
        if nif in clientes:
            del clientes[nif]
        else:
            print("El cliente no existe")
    if opcion ==3:
        nif = input("Ingrese su NIF: ")
        if nif in clientes:
            print(clientes[nif])
        else:
            print("El cliente no existe")

    if opcion == '4':
        print('Lista de clientes')
        for clave, valor in clientes.items():
            print(clave, valor['nombre'])
    if opcion == '5':
        print('Lista de clientes vips')
        for clave, valor in clientes.items():
            if valor['vip']:
                print(clave, valor['nombre'])
    elif opcion == '6':
        print("Terminando el programa.")
    else:
        print("Opción no válida. Por favor, elige una opción del menú.")

