entrada = input("Ingresa una lista de palabras separadas por comas: ")
letra = input("Ingresa la letra con la que deben comenzar las palabras: ").lower()

palabras_lista = [palabra.strip() for palabra in entrada.split(",")]

palabras_filtradas = [palabra for palabra in palabras_lista if palabra.lower().startswith(letra)]

print(f"Palabras que comienzan con la letra '{letra}':")
for palabra in palabras_filtradas:
    print(palabra)
