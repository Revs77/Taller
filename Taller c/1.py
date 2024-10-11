#Ejercicio 1
def suma_numeros_pares(numeros):
    if not isinstance(numeros, list):
        raise ValueError("El argumento debe ser una lista.")

    suma = 0
    for numero in numeros:
        if isinstance(numero, (int, float)) and numero % 2 == 0:
            suma += numero
    return suma


entrada = input("Ingresa una lista de números separados por comas (por ejemplo, 1, 2, 3): ")

numeros_lista = []
for num in entrada.split(","):
    try:
        numeros_lista.append(float(num.strip()))
    except ValueError:
        print(f"Advertencia: '{num.strip()}' no es un número válido y será ignorado.")

resultado = suma_numeros_pares(numeros_lista)
print(f"La suma de los números pares es: {resultado}")








