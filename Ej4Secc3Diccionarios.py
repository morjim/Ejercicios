fecha = input("introduce una fecha en formato dd/mm/aaaa: ")

dia,mes,año = fecha.split("/");

meses={"1": "Enero","2": "Febrero", "3": "Marzo","4": "Abril","5": "Mayo", "6": "Junio"," 7 ": "Julio","8": "Agosto","9": "Septiembre", "10" : "Octubre","11": "Noviembre","12": "Diciembre"}

print(f"{dia} de {meses[mes]} de {año}")