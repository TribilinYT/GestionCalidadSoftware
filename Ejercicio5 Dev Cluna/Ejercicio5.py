# @autor Cristhian Alejandro Luna Bravo
# @version 0.1
# @date 30/06/2020
# @last update 30/06/2020

#Ejercicio 5
#validacion
numero=0
print("ingrese valor numerico")
while( int(numero < 10) or int (numero > 1000)):
    numero =int(input("El valor debe ser entre 10 y 1000 "))


suma=0

for cifra in str(numero):
    print("Operando: "+ str(cifra))
    
    suma+=int(cifra)


print("La suma final es: "+str(suma))