# @autor Cristhian Alejandro Luna Bravo
# @version 0.1
# @date 30/06/2020
# @last update 30/06/2020

#Ejercicio 9

#Incializacion de Variables
valorKilometros=0
valorGasolina= 0
valorDinero= 0
valorTiempo=0

#Validacion Numerica
while( float(valorKilometros) <=0):
   valorKilometros=float(input("Ingrese valor total de Km recorridos: "))
print()

while( float(valorGasolina) <=0):
   valorGasolina=float(input("Ingrese valor $ de gasolina por Litros: "))
print()

while( float(valorDinero) <=0):
   valorDinero=float(input("Ingrese valor $ gastado en el viaje: "))
print()

while( float(valorTiempo) <=0):
  valorTiempo=int(input("Ingrese valor de Horas: "))
print()


#El consumo de la gasolina es el dinero gasta en gasolida 
# y el precio de la gasolina sobre la cantidad de kilometros

#Literal A
consumoGasolina100Litros= valorDinero/(valorGasolina*valorKilometros)*100
consumoGasolina100Dinero= (valorDinero/valorKilometros)*100
print("El consumo de gasolina por 100Km Litros: "+ str(consumoGasolina100Litros)+" L")
print("El consumo de gasolina por 100Km Dinero: "+ str(consumoGasolina100Dinero)+" USD \n")

#Literal B
consumoGasolinaLitros= valorDinero/(valorGasolina*valorKilometros) 
consumoGasolinaDinero=valorDinero/valorKilometros
print("El consumo de gasolina por Litro: "+str(consumoGasolinaLitros)+" L")
print("El consumo de gasolina por Dinero: "+str(consumoGasolinaDinero)+" USD \n")

#Literal C
velocidadMediaKilometro= valorKilometros/valorTiempo
velocidadMediaMetro= (valorKilometros/1000)/(valorTiempo/60)
print("El valor de velocidad (Km/s) : "+str(velocidadMediaKilometro))
print("El valor de velocidad (m/s) : "+str(velocidadMediaMetro))
