
#version 1

'''
n=2
numero=int(input("Dime un número a ver si aciertas"))
if numero==n:
    print("¡Lo has acertado!")
else:
    print("Lo siento, no has acertado")

#version 2

for i in range(0,10):
    numero = int(input("Dime un número a ver si aciertas"))
    if numero!=n:
       
        print("Lo siento, no has acertado")
    else:
        print("¡Lo has acertado!")
'''
#version 3
n=2
while(True ):

    numero = int(input("Dime un número a ver si aciertas"))
    if numero == n :
        print("¡Lo has acertado!")
        break
    else:
       
        print("Lo siento, no has acertado")