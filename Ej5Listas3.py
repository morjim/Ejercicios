'''
Pedir al usuario que ingrese los numeros ganadores de la loteria y lo muestre luego por pantalla de menor a mayor
'''
entrada = input("Ingrese 5 números de la lotería separados por espacios: ")

numeros = entrada.split(" ")

if len(numeros)!=5:
    print ("Error, debe ingresar 5 números")
else:
    try:
        numeros= [int(num) for num in numeros]
        numeros.sort()
        print ("Los numeros ganadores son : ", numeros)
    except ValueError:
        print("Error, por favor ingrese un numero entero")





