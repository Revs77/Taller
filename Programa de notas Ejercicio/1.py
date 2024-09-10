# Función para calcular el rendimiento y el costo final de la matrícula
def calcular_rendimiento_y_costo(notas, costo_matricula):
    # Calcular el promedio de las notas
    promedio = sum(notas) / len(notas)

    # Clasificar el rendimiento
    if promedio >= 4:
        rendimiento = "Excelente"
        descuento = 0.20
    elif promedio >= 3:
        rendimiento = "Bien"
        descuento = 0.00
    else:
        rendimiento = "Deficiente"
        descuento = 0.00

    # Calcular el costo final de la matrícula
    costo_final = costo_matricula * (1 - descuento)

    return promedio, rendimiento, costo_final

notas = []
for i in range(1, 5):
    while True:
        try:
            nota = float(input(f"Ingrese la nota {i} (entre 1 y 5): "))
            if 1 <= nota <= 5:
                notas.append(nota)
                break
            else:
                print("Nota inválida. Debe estar entre 1 y 5.")
        except ValueError:
            print("Entrada no válida. Ingrese un número.")


while True:
    try:
        costo_matricula = float(input("Ingrese el costo total de la matrícula: "))
        if costo_matricula >= 0:
            break
        else:
            print("El costo debe ser un valor positivo.")
    except ValueError:
        print("Entrada no válida. Ingrese un número.")


promedio, rendimiento, costo_final = calcular_rendimiento_y_costo(notas, costo_matricula)

# Mostrar los resultados
print(f"\nPromedio del estudiante: {promedio:.2f}")
print(f"Rendimiento del estudiante: {rendimiento}")
print(f"Monto final a pagar por la matrícula: {costo_final:.2f} pesos")
