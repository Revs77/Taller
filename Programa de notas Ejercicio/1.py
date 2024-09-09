def calcular_rendimiento_y_costo(notas, costo_matricula):
    """Calcula el rendimiento del estudiante y el costo final de la matrícula."""
    promedio = sum(notas) / len(notas)

    if promedio >= 4:
        rendimiento = "Excelente"
        descuento = 0.20
    elif promedio >= 3:
        rendimiento = "Bien"
        descuento = 0.00
    else:
        rendimiento = "Deficiente"
        descuento = 0.00

    costo_final = costo_matricula * (1 - descuento)
    return promedio, rendimiento, costo_final

def obtener_notas():
    """Solicita y valida las notas del estudiante."""
    notas = []
    for r in range(1, 5):
        while True:
            try:
                nota = float(input(f"Ingrese la nota {r} (entre 1 y 5): "))
                if 1 <= nota <= 5:
                    notas.append(nota)
                    break
                else:
                    print("Nota inválida. Debe estar entre 1 y 5.")
            except ValueError:
                print("Entrada no válida. Ingrese un número.")
    return notas

def obtener_costo_matricula():
    """Solicita y valida el costo total de la matrícula."""
    while True:
        try:
            costo_matricula = float(input("Ingrese el costo total de la matrícula: "))
            if costo_matricula >= 0:
                return costo_matricula
            else:
                print("El costo debe ser un valor positivo.")
        except ValueError:
            print("Entrada no válida. Ingrese un número.")

def mostrar_resultados(promedio, rendimiento, costo_final):
    """Muestra los resultados calculados."""
    print(f"\nPromedio del estudiante: {promedio:.2f}")
    print(f"Rendimiento del estudiante: {rendimiento}")
    print(f"Monto final a pagar por la matrícula: {costo_final:.2f} pesos")

def main():
    notas = obtener_notas()
    costo_matricula = obtener_costo_matricula()
    promedio, rendimiento, costo_final = calcular_rendimiento_y_costo(notas, costo_matricula)
    mostrar_resultados(promedio, rendimiento, costo_final)

if __name__ == "__main__":
    main()
