#Ejercicio 1
#
print("Ingrese valor en Centimetros")

valorCentimetros=input()

print("El valor ingresado es: "+ str(valorCentimetros)+" cm \n")

valorPulgadas= float (valorCentimetros) * 0.39370
valorPies= float(valorCentimetros) * 0.0328085

print ("El valor en Pulgadas es: "+ str(valorPulgadas)+" Pulgadas  \n") 
print ("El valor en Pies es: "+ str(valorPies)+" Pies")