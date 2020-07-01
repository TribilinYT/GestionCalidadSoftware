# @autor Cristhian Alejandro Luna Bravo
# @version 0.1
# @date 30/06/2020
# @last update 30/06/2020

#Ejercicio 17
def factorial(n):
	fact=1
	for x in range(1,n):
		fact = fact * x
	return fact

while True:
	try:
		numero=0
		s=0
		mensaje = " s = "
		while True:
			numero = int(input("Ingrese un número límite para calcular el valor de la expresión matemática\n s=(1/0!)...(1/n!): "))
			if (numero < 0):
				print("Ha ingresado un numero negativo. Introduzca un Valor mayor a 0")
			else:
				break
		for x in range(0,numero+1):
			s = s+(1/factorial(x))
			mensaje = mensaje+"1/" + str(x) + "! +"
		print("\n" + mensaje)
		print(" s = " + str(s))
		break
	except Exception as ex:
		print("los caracteres no son validos, Intente nuevamente")
		print(ex)

print("EL PROGRAMA HA FINALIZADO")

