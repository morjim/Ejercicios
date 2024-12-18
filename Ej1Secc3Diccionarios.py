
divisas={'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
eleccion = input("Que divisa quieres ").title()
if eleccion in divisas:
   print("Si existe la divisa y su símbolo es " + divisas[eleccion])
else :
   print("No existe")
