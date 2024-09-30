#Sistema de venta de motos con promociones
def calcular_descuento_base(marca, precio_base):
    descuentos_marca = {
        "Honda": 0.05,
        "Yamaha": 0.08,
        "Suzuki": 0.10,
        "Otra": 0.02
    }
    return precio_base * descuentos_marca.get(marca, 0)

def calcular_descuento_dia(dia_semana, es_feriado):
    if es_feriado:
        return 0.25
    elif dia_semana.lower() == "martes":
        return 0.12
    elif dia_semana.lower() == "sábado":
        return 0.18
    else:
        return 0

def main():
    precio_base = float(input("Ingrese el precio base de la motocicleta: "))
    marca = input("Ingrese la marca de la motocicleta (Honda, Yamaha, Suzuki, Otra): ")
    es_feriado = input("¿El día de la compra es feriado? (sí/no): ").lower() == "sí"
    dia_semana = input("Ingrese el día de la semana de la compra: ")

    # Calcular descuentos
    descuento_marca = calcular_descuento_base(marca, precio_base)
    descuento_dia = calcular_descuento_dia(dia_semana, es_feriado)

    # Total de descuento antes de aplicar el límite
    total_descuento = descuento_marca + (descuento_dia * precio_base)

    # Aplicar límite máximo de descuento
    if total_descuento > 0.30 * precio_base:
        total_descuento = 0.30 * precio_base

    # Calcular precio final
    precio_final = precio_base - total_descuento
    ahorro_total = total_descuento

    # Mostrar resultados
    print("\n--- Resultados de la compra ---")
    print(f"Precio base de la motocicleta: ${precio_base:.2f}")
    print(f"Descuento por marca: ${descuento_marca:.2f}")
    print(f"Descuento por día: ${descuento_dia * precio_base:.2f}")
    print(f"Descuento total aplicado: ${ahorro_total:.2f}")
    print(f"Precio final de la motocicleta: ${precio_final:.2f}")

if __name__ == "__main__":
    main()
