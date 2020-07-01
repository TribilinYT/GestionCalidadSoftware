# @autor Cristhian Alejandro Luna Bravo
# @version 0.1
# @date 30/06/2020
# @last update 30/06/2020

#Ejercicio 11
#Se inicializan el valor de entrada y un acumulador (sumaAcumulada)
valor=int(input("Ingrese un valor numerico entre 10 y 99 "))
sumaAcumulada=int(0)

#Se autosuman los digitos del valor ingresado y luego el valor de la suma
#pasa por un condicional para verificar si son primos
if (valor >9) and (valor <100): #Validadcion de Entradas
    print("Su valor es: ",valor)
    for i in str(valor):
        sumaAcumulada +=int(i)
        print("OPERANDO:",i)
    print("el valor de la suma es:",sumaAcumulada)

    #Condicional verificacion de numeros primos
    for j in range(2,sumaAcumulada):
        if(sumaAcumulada % j)==0:
            print("EL VALOR de:",sumaAcumulada, "no es primo")
    else:
        print("EL VALOR de:",sumaAcumulada, " es primo")

#salida negativa de entrada
else:
    print(valor, "No respeta el valor indicado")