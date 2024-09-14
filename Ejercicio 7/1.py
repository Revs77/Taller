#7.	Cálculo de nota final en curso de fundamentos de algoritmos
def obtener_nota(nombre, peso):
    while True:
        try:
            nota = float(input(f"Ingrese la nota para {nombre} (peso {peso}%): "))
            if 1.0 <= nota <= 5.0:
                return nota
            print("Nota fuera de rango. Debe estar entre 1.0 y 5.0.")
        except ValueError:
            print("Entrada no válida. Inténtelo de nuevo.")


def main():
    actividades = [
        {"nombre": "Taller 1", "peso": 0.20},
        {"nombre": "Taller 2", "peso": 0.15},
        {"nombre": "Cuestionario 1", "peso": 0.22},
        {"nombre": "Cuestionario 2", "peso": 0.10},
        {"nombre": "Proyecto final", "peso": 0.33}
    ]

    nota_final = round(sum(obtener_nota(a['nombre'], a['peso']) * a['peso'] for a in actividades), 2)

    evaluacion = (
        "Excelente" if nota_final >= 4.5 else
        "Bueno" if nota_final >= 3.5 else
        "Regular" if nota_final >= 2.5 else
        "Insuficiente"
    )

    print(f"Nota final: {nota_final}")
    print(f"Evaluación: {evaluacion}")


if __name__ == "__main__":
    main()
