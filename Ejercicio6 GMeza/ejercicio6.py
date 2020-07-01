# @autor Meza cedeño Galo
# Ejercicio 6

#programa que identifique numeros naturales Automórficos.
print("--------numeros Automórficos----------")

numero=0
while(int(numero <=0) or int(numero > 1000)):
    numero = int(input("Ingrese un número del 1 al 1000: "))

cuadrado = numero**2
numero, cuadrado, automorfico = list(str(numero)), list(str(cuadrado)), False

# Determinamos el rango del número ingresado
for i in range(-1, -len(numero) - 1, -1):
    if numero[i] == cuadrado[i]:
        automorfico = True
    else:
        automorfico = False
        break

# Si imprime el resultado
if automorfico:
    print("El numero ingresado SI es Automórfico.")
else:
    print("El numero natural NO es Automórfico.")