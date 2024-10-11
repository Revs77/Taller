#Ejercicio 1
entrada = input("Ingresa una palabra o frase: ")

conteo_vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

for caracter in entrada.lower():
    if caracter in conteo_vocales:
        conteo_vocales[caracter] += 1

for vocal, conteo in conteo_vocales.items():
    print(f"La vocal '{vocal}' aparece {conteo} veces.")
