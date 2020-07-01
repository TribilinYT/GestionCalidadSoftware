valorKilometros=float(input("Ingrese valor total de Km recorridos: "))
valorGasolina=float(input("Ingrese valor $ de gasolina por Litros: "))
valorDinero=float(input("Ingrese valor $ gastado en el viaje: "))
valorTiempo=int(input("Ingrese valor de Horas: "))

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
