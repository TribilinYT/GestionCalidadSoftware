#Ejercicio 3
#Se importa la libreria math
import math
#

valor1=int(input("Ingrese primer valor: "))
valor2=int(input("Ingrese Segundo valor: "))
mcd=math.gcd(valor1, valor2)            #se llama la funcion ".gdc" que calcula el maximo comun divisor
print ("El Maximo Comun Divisor entre "+str(valor1)+" y "+str(valor2)+" es: "+str(mcd))
#print (math.gcd(12, 6))
#print (math.gcd(10, 0))
#print (math.gcd(0, 34))
#print (math.gcd(0, 0))
