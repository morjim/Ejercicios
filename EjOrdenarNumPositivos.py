
listaNum=[5,7,9,-7,10,5,3,1,4]

def ordena_positivo(listaNum):
    lista = sorted([num for num in listaNum if num > 0])
    print (lista)

ordena_positivo(listaNum)