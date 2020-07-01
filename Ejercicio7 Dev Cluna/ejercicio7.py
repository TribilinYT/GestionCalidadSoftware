# @autor Cristhian Alejandro Luna Bravo
# @version 0.1
# @date 30/06/2020
# @last update 30/06/2020

#Ejercicio 7

primerValor=0
segundoValor=0
tercerValor=0

#Validacion Numerica

while( float(primerValor) <=0):
  primerValor=int(input("Ingrese primer valor: "))
print()

while( float(segundoValor) <=0):
   segundoValor=int(input("Ingrese segundo valor: "))
print()

while( float(tercerValor) <=0):
   tercerValor=int(input("Ingrese tercer valor: "))
print()


#Los numeros primos son mayores que uno
if (primerValor > 1):

#VALIDACION PRIMOS PRIMER VALOR
#primoValor recogera 1 si es primo o 0 si no es primo
    for i in range(2,primerValor):
        if (primerValor% i)==0:
            print("EL PRIMER VALOR no es primo")
            print(i,"veces",primerValor//i, "es",primerValor)
            primoValor1=0
            break
    else:
        primoValor1=1
        print("EL PRIMER VALOR:",primerValor,"es un numero primo")

#VALIDACION PRIMOS SEGUNDO VALOR
#primoValor recogera 1 si es primo o 0 si no es primo
    for j in range(2,segundoValor):
        if (segundoValor% j)==0:
            print("EL SEGUNDO VALOR no es primo")
            print(i,"veces",segundoValor//i, "es",segundoValor)
            primoValor2=0
            break
    else:
        primoValor2=1
        print("EL SEGUNDO VALOR:",segundoValor,"es un numero primo")

#VALIDACION PRIMOS TERCER VALOR
#primoValor recogera 1 si es primo o 0 si no es primo
    for k in range(2,tercerValor):
        if (tercerValor % k)==0:
            print("EL TERCER VALOR no es primo")
            print(i,"veces",tercerValor//i, "es",tercerValor)
            primoValor3=0
            break
    else:
        primoValor3=1
        print("EL TERCER VALOR:",tercerValor,"es un numero primo")

#Validacion de los primos ternarios
#compara los valores primoValor para verificar si los 3 valores son primos
if (primoValor1==1) and (primoValor2==1) and (primoValor3==1):
  print("El PRIMER valor",primerValor
    ,", el SEGUNDO valor",segundoValor," y el TERCER valor",tercerValor,
    " son TRIO PITAGORICO")
else:
    print("El PRIMER valor",primerValor
    ,", el SEGUNDO valor",segundoValor," y el TERCER valor",tercerValor,
    "no son TRIO PITAGORICO")

                