#Ejercicio 3
def invertir_lista(lista):
    return lista[::-1]

entrada = input("Ingresa una lista de elementos separados por comas: ")

elementos_lista = []
for elemento in entrada.split(","):
    try:
        elementos_lista.append(elemento.strip())
    except Exception as e:
        print(f"Advertencia: '{elemento.strip()}' no se pudo agregar.")

resultado = invertir_lista(elementos_lista)
print(f"La lista invertida es: {resultado}")