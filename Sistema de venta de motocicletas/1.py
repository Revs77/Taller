#Sistema de venta de motos con promociones
def calculate_brand_discount(brand, base_price):
    brand_discounts = {
        "Honda": 0.05,
        "Yamaha": 0.08,
        "Suzuki": 0.10,
        "Otra": 0.02
    }
    return base_price * brand_discounts.get(brand, 0)


def calculate_day_discount(day, is_holiday):
    if is_holiday:
        return 0.25
    elif day.lower() == "martes":
        return 0.12
    elif day.lower() == "sabado":
        return 0.18
    else:
        return 0


def get_base_price():
    while True:
        try:
            base_price = float(input("Ingrese el precio base de la motocicleta: "))
            if base_price <= 0:
                print("El precio base debe ser mayor que cero.")
            else:
                return base_price
        except ValueError:
            print("El precio base debe ser un número válido.")


def get_brand():
    while True:
        brand = input("Ingrese la marca de la motocicleta (Honda, Yamaha, Suzuki, Otra): ")
        if brand in ["Honda", "Yamaha", "Suzuki", "Otra"]:
            return brand
        else:
            print("La marca debe ser una de las siguientes: Honda, Yamaha, Suzuki, Otra")


def get_is_holiday():
    while True:
        is_holiday = input("¿El día de la compra es feriado? (sí/no): ").lower()
        if is_holiday == "sí" or "si":
            return True
        elif is_holiday == "no":
            return False
        else:
            print("La respuesta debe ser sí o no")


def get_day():
    while True:
        day = input("Ingrese el día de la semana de la compra: ")
        if day.lower() in ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]:
            return day
        else:
            print("El día debe ser uno de los siguientes: lunes, martes, miércoles, jueves, viernes, sábado, domingo")


def main():
    base_price = get_base_price()
    brand = get_brand()
    is_holiday = get_is_holiday()
    day = get_day()

    brand_discount = calculate_brand_discount(brand, base_price)
    day_discount = calculate_day_discount(day, is_holiday)

    total_discount = brand_discount + (day_discount * base_price)

    if total_discount > 0.30 * base_price:
        total_discount = 0.30 * base_price

    final_price = base_price - total_discount
    total_savings = total_discount

    print("\n--- Resultados de la compra ---")
    print(f"Precio base de la motocicleta: ${base_price:.2f}")
    print(f"Descuento por marca: ${brand_discount:.2f}")
    print(f"Descuento por día: ${day_discount * base_price:.2f}")
    print(f"Descuento total aplicado: ${total_savings:.2f}")
    print(f"Precio final de la motocicleta: ${final_price:.2f}")


if __name__ == "__main__":
    main()