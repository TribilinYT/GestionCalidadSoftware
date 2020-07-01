# @autor Cristhian Alejandro Luna Bravo
# @version 0.1
# @date 30/06/2020
# @last update 30/06/2020

#Ejercicio 5
numero=input('Introduce un número: ')
suma=0
for cifra in numero:
    print("Operando: "+ str(cifra))
    
    suma+=int(cifra)


print("La suma final es: "+str(suma))