# @autor Cristhian Alejandro Luna Bravo
# @version 0.1
# @date 30/06/2020
# @last update 30/06/2020


#Ejercicio 1
#validacion Numerica
valorCentimetros=0
while( int(valorCentimetros) <=0):
    valorCentimetros=float(input("Ingrese un valor Numerico: "))

print("El valor ingresado es: "+ str(valorCentimetros)+" cm \n")

valorPulgadas= float (valorCentimetros) * 0.39370
valorPies= float(valorCentimetros) * 0.0328085

print ("El valor en Pulgadas es: "+ str(valorPulgadas)+" Pulgadas  \n") 
print ("El valor en Pies es: "+ str(valorPies)+" Pies")