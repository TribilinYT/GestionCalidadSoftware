# @autor Meza cedeño Galo
# Ejercicio 8

# Definimos la lista que va a contener los datos ingresados 
# variable con un input tipo entero para 
# el ingreso de datos 
lista = []
numero = int(input("Ingrese tres dígitos a invertir:  "))

# Bucle while restringe el valor del número ingresado
while numero > 1000 or numero < 100 or numero == 1000:
    print(" \nDeben ser tres dígitos menores a 1000... ")
    numero = int(input("Ingrese tres digitos a invertir:  "))

# Lista en la cual se guarda el número ingresado
lista.append(str(numero))
cadena = ""

# Determinamos el rango del número ingresado
for i in range(3):
    valor = lista[0] [-(i+1)]
    cadena = cadena + valor

# Se muestra el número ingresado y el número invertido
print("\nNúmero ingresado:  ", numero)
print("\nNúmero invertido:  ", cadena)
