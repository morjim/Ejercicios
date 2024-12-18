'''
Programa que almacene el abecedatio en una lista, elimine de la lista las letras que ocupen posiciones mútliplos de 3 y mostamos el resultado por pantalla
'''

abc =[
    'a', 'b', 'c', 'd', 'e', 'f', 
    'g', 'h', 'i', 'j', 'k', 'l',
    'm', 'n', 'o', 'p', 'q', 'r',
    's', 't', 'u', 'v', 'w', 'x',
    'y', 'z'
]
abc_vacio = []

for i in range(len(abc)):
   
    if i % 3 != 0:
        abc_vacio.append(abc[i])
      
        print(abc_vacio)

