# @autor Cristhian Alejandro Luna Bravo
# @version 0.1
# @date 30/06/2020
# @last update 30/06/2020

#Ejercicio 3
#Se importa la libreria math
import math

#Contadores
valor1=0
valor2=0

#validacion
while( int(valor1) <=0):
   valor1=int(input("Ingrese primer valor numerico: "))

while( int(valor2) <=0):
   valor2=int(input("Ingrese segundo valor numerico: "))



mcd=math.gcd(valor1, valor2)            #se llama la funcion ".gdc" que calcula el maximo comun divisor
print ("El Maximo Comun Divisor entre "+str(valor1)+" y "+str(valor2)+" es: "+str(mcd))
#print (math.gcd(12, 6))
#print (math.gcd(10, 0))
#print (math.gcd(0, 34))
#print (math.gcd(0, 0))
