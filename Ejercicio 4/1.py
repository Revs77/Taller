x,y,z,w = 15,10,20,8
esta_entre=min(y,z)<= x <= max(y, z)
#W es par
espar=(w %2==0)

print(f"x este entre y y z {esta_entre}")
print(f"w es par {espar}")

#Comprueba si a es mayor que b o si c es igual a d, pero no ambas condiciones

a,b,c,d=7,5,3,3
Condicion1= a>b
Condicion2= c==d

Resultado= Condicion1 != Condicion2

print(f"Exactamente una de las condiciones es verdadera {Resultado}")

#Verifique si x es negativo, y es positivo y z es cero:

x, y, z = -3, 5, 0

Negativo = x<0
Positivo = y>0
es_igual = z==0

print(f"x es negativo {Negativo}")
print(f"y es positivo {Positivo}")
print(f"z es igual a cero {es_igual}")



