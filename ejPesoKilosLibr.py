
peso = float (input("Introduce tu peso: "))
opcion = input ("El peso está en kilos o libras , inserta K o L : ")

if opcion.lower() == "k":
    peso = peso
    print(f'{peso}  kilos')
elif opcion.lower() == "l":
    peso= peso / 0.45
    print(f'{peso}  libras')
else :
    input("Introducuzca una K o L");