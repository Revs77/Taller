destino = input("Ingrese el destino de la llamada: ")
duracion = int(input("Ingrese la duracion del la llamada: "))


if destino == "estados unidos":
    tarifa = 900
elif destino == "canada":
    tarifa = 800
elif destino == "europa":
    tarifa = 950
elif destino == "resto del mundo":
    tarifa = 1250
else:
    print("Destino no válido.")
    exit()

# Calcular el costo total antes de descuento
costo_total = tarifa * duracion

if duracion > 15:
    costo_total*=0.80



print(f"El costo de la llamada es:", costo_total)