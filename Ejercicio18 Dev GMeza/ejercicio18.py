# @autor Meza cedeño Galo
# EJERCICIO 18

# Definimos el ciclo for y el rango desde dónde 
# se empieza a incrementar
def suma(N,S):
       for i in range(2,N):
             if(N % i==0):
                    S=S+i
       return S
suma1,suma2=1,1

#Ingresamos las variables de los numeros a ingresa 
numero1 = 0
numero2 = 0

# Bucle while que valida a entrada de datos 
# que no sean cero ni negativos
while(numero1 <=0):
    numero1=int(input("ingrese PRIMER número mayor a cero:\n"))

while(numero2 <=0):
    numero2=int(input("ingrese SEGUNDO número mayor a cero:\n"))

 
suma1 = suma(numero1, suma1)
suma2 = suma(numero2, suma2)

# Condición previa a cumplirse si los números son amigos 
if((suma1==numero2)and (suma2==numero1)):
       print("los numeros "+str(numero1)+" y "+
       str(numero2)+" Si son numeros amigos")

# si no se cumple los números no son amigos
else:
       print("los numeros "+str(numero1)+" y "+
       str(numero2)+" No son numeros amigos")

