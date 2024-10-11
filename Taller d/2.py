nombres_lista = []

while True:
    entrada = input("Ingresa una lista de nombres separados por comas: ")
    try:
        for nombre in entrada.split(","):
            nombre_strip = nombre.strip()
            if not nombre_strip:
                raise ValueError("El nombre no puede estar vacío.")
            nombres_lista.append(nombre_strip)
        break
    except ValueError as e:
        print(f"Advertencia: {e} - intenta nuevamente.")

nombres_lista.sort()
print("Lista de nombres en orden alfabético:")
for nombre in nombres_lista:
    print(nombre)

