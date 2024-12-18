frutas={
    "Platano": 1.35,
    "Manzana": 0.8,
    "Pera": 0.85,
    "Naranja": 0.7
}

pedido = input("¿Qué fruta quieres comprar? ").title()
if pedido in frutas:
    kilos= int(input("¿Cuántos kilos?"))
    precio = frutas[pedido] * kilos
    print(f"El precio de {pedido} es {precio} euros")
else:
    print("Lo siento, esa fruta no está disponible")