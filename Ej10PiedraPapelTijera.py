import random

while True:
    lista = ["piedra" , "papel" , "tijera"]
    eleccion = random.choice(lista)
    usuario = input("Escribe piedra, papel o tijera o salir para salir: ").lower()

    if usuario == "salir":
         print ("HASTA LUEGO")
         break


    if usuario not in lista:
        print("Escribe piedra, papel o tijera")
        continue

    if usuario == eleccion:
        print(f"Empate, ambos elegiste {usuario}")
        if eleccion == "papel" and usuario == "tijera":
            print("Papel cubre tijera, el ordenador gana")
        elif eleccion == "papel" and usuario == "piedra":
            print("Piedra cubre papel, el usuario gana")           
        elif eleccion == "tijera" and usuario == "piedra":
            print("Piedra cubre tijera, el usuario gana")
            
        elif eleccion == "tijera" and usuario == "papel":
            print("Tijera corta papel, el usuario gana")
            
        elif eleccion == "piedra" and usuario == "tijera":
            print("Piedra cubre tijera, el usuario gana")
        else :
            print("Papel cubre piedra, el ordenador gana")
     