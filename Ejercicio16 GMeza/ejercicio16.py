# @autor Meza cedeño Galo
# Ejercicio 16

# Declaramos como variables los números a ingresar
numero1 = 0
numero2 = 0
numero3 = 0

# Ciclo que valida que la entrada se mayor a 0  
while(int(numero1) <=0):
    numero1 = int(input("Ingrese el PRIMER número positivo mayor que cero: "))

while(int(numero2) <=0):
    numero2 = int(input("Ingrese el SEGUNDO número positivo mayor que cero: "))

while(int(numero3) <=0):
    numero3 = int(input("Ingrese el TERCER número positivo mayor que cero: "))


menor = min(numero1, numero2, numero3)
mayor = max(numero1, numero2, numero3)
medio = (numero1 + numero2 + numero3) - menor - mayor

# Imprimimos el resultado 
print("El segundo mayor ingresado es: ", medio)


