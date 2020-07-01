#Ejercicio 5
numero=input('Introduce un número: ')
suma=0
for cifra in numero:
    print("Operando: "+ str(cifra))
    
    suma+=int(cifra)


print("La suma final es: "+str(suma))