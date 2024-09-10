#4.	Realizar un algoritmo que permita convertir metros a millas.
metros=float(input("Ingrese la cantidad de metros que desea convertir: "))
Millas= metros/1609.344
print(f"{metros} son aproximadamente {Millas} millas")

#5. Elabore un algoritmo que muestre el nuevo salario mínimo para el siguiente año.
Salario=float(input("Ingrese la cantidad de salario: "))
Aumento= 4.2
porcentaje=Salario* (Aumento/100)
Salario_nuevo=Salario+porcentaje
print(f"el salario minimo del proximo año sera {Salario_nuevo}")

#6.	Convertir pesos colombianos a dólares.
Pesos=float(input("Ingrese la cantidad de pesos que desea convertir: "))

Dolares= Pesos * 0.00024

print(f"{Pesos} pesos colombianos serian {Dolares} dolares")


