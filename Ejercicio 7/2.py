def obtener_nota(nota,peso):
    while True:
        try:
            comida=float(input("Ingrese la comida que desea"))
            if comida== ("arroz, arepa, huevo"):
                return comida
            print("Esta comida no esta disponible, ingresa otra")
        except ValueError:
            print("No disponible")

float(obtener_nota("Ingrese la comida"))