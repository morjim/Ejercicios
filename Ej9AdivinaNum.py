import random

numero = random.randint(1,100)


while (True):
    usuario=int(input("ingresa un numero a ver si lo adivinas"))
    if numero > usuario :
        print ("El numero es mayor al ingresado")
    elif numero < usuario :
        print ("El numero es menor al ingresado")
  
    else :
        print("lo adivinaste")