#Ejercicio 2
def eliminar_duplicados(lista):
    seen = set()
    resultado = []
    for elemento in lista:
        if elemento not in seen:
            seen.add(elemento)
            resultado.append(elemento)
    return resultado

entrada = input("Ingresa una lista de números separados por comas (por ejemplo, 1, 2, 3): ")

numeros_lista = []
for num in entrada.split(","):
    try:
        numeros_lista.append(float(num.strip()))
    except ValueError:
        print(f"Advertencia: '{num.strip()}' no es un número válido y será ignorado.")

resultado = eliminar_duplicados(numeros_lista)
print(f"La lista sin duplicados es: {resultado}")