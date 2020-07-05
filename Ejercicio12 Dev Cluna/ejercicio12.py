# @autor Cristhian Alejandro Luna Bravo
# @version 0.1
# @date 30/06/2020
# @last update 01/07/2020

print("---Si no tiene el billete de alguna denominacion ingrese el valor 0---")
billestes100 =  int(input("Ingrese la cantidad de billetes de $100 que tiene: "))

# Bucles que valida las el ingreso de la cantidad de billetes
#  en cada uno de los campos de ingreso
while (billestes100 < 0):
    billestes100= int(input("Ingrese la cantidad de billetes de $100 que tiene: "))

billestes20 = int(input("Ingrese la cantidad de billetes de $20 que tiene: "))

while (billestes20 < 0):
    billestes20= int(input("Ingrese la cantidad de billetes de $20 que tiene: "))

billestes10 = int(input("Ingrese la cantidad de billetes de $10 que tiene: "))
while (billestes10 < 0):
    billestes10= int(input("Ingrese la cantidad de billetes de $10 que tiene: "))

billestes5 = int(input("Ingrese la cantidad de billetes de $5 que tiene: "))

while (billestes5 < 0):
    billestes5= int(input("Ingrese la cantidad de billetes de $5 que tiene: "))


billestes1 = int(input("Ingrese la cantidad de billetes de $1 que tiene: "))

while (billestes10 < 0):
    billestes10= int(input("Ingrese la cantidad de billetes de $1 que tiene: "))


# operaciones de los datos ingresados como cantidad
#  de billetes y muestra el monto total
sumaTotal= float((billestes100*100) + (billestes20*20) + (billestes10*10) + (billestes5) +(billestes1*1))
print("cuenta con un total de: $",sumaTotal,"USD")

# Ingreso de valor del artículo que sea mayor que cero
valorArticulo=float(input("Ingrese valor del articulo: "))
while (valorArticulo <= 0):
    valorArticulo=float(input("Ingrese valor del articulo: "))

#condicional que muestra el dinero que le faltaría
if(valorArticulo > sumaTotal):
    valorFinal=(valorArticulo-sumaTotal)
    print("El dinero faltante es: ",valorFinal)

#valor que sobraría
else:
    valorFinal=(sumaTotal - valorArticulo)
    print("El suelto es: ",valorFinal)

