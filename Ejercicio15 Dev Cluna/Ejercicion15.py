# @autor Cristhian Alejandro Luna Bravo
# @version 0.1
# @date 30/06/2020
# @last update 30/06/2020

#Ejercicio 15
valorInicial=0
valorFinal=0
valorMultiplo=0

#validacion
while(valorInicial<=0) or (valorFinal<=0) or (valorMultiplo <=0):
    print("Ingrese una valor mayor a CERO")
    valorMultiplo=int(input("Ingrese el valor a Multiplicar: "))
    valorInicial=int(input("Ingrese valor inicial: "))
    valorFinal=int(input("ingrese 2 valor final: "))
    print()

    while (valorFinal <=valorInicial):
        print("\nEl valor final debe ser menor al inicial\n")
        valorInicial=int(input("Ingrese valor inicial: "))
        valorFinal=int(input("ingrese 2 valor final: "))
        print(" ")

#Tabla Multiplicar en Ciclo For
print ("Ciclo For")
for i in range(valorInicial, valorFinal+1):
    multiploFor=valorMultiplo*int(i)
    print(valorMultiplo,"X", i,"=",multiploFor)
print()

#Tabla Multiplica en Ciclo While
print("Ciclo While")
acumuladorWhile=valorInicial-1
print(acumuladorWhile)
while (acumuladorWhile <valorFinal):
    acumuladorWhile=acumuladorWhile+1
    multiploWhile=acumuladorWhile*valorMultiplo
    print(valorMultiplo,"X",acumuladorWhile,"=",multiploWhile)
print()

#Tabla Multiplicar en Ciclo Do-While
print("Ciclo Do-While")
acumulador=valorInicial-1
while True:
    acumulador=acumulador+1
    multiploDo=acumulador*valorMultiplo
    
    print(valorMultiplo,"X",acumulador,"=",multiploDo)
    if(acumulador==valorFinal):
        break
    

