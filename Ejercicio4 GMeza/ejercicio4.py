# @autor Meza cedeño Galo
# Ejercicio 4

# Definimos las variables
lado_a=0
lado_b=0
lado_c=0

# Validación de los datos a ingresar
while(float(lado_a) <=0):
    lado_a = float(input("Ingrese el PRIMER lado del triángulo (QUE SEA POSITIVO): "))

while(float(lado_b) <=0):
    lado_b = float(input("\nIngrese el SEGUNDO lado del triángulo (QUE SEA POSITIVO): "))

while(float(lado_c) <=0):
    lado_c = float(input("\nIngrese el TERCER lado del triángulo (QUE SEA POSITIVO):"))

#condicional que actua para que los datos ingresados sean iguales 
#imprima "los lados correspondeen a un triángulo"
if(lado_a+lado_b)>lado_c and (lado_a+lado_c)>lado_b and (lado_b+lado_c)>lado_a:
    print("\nlos lados corresponden a un triángulo")

# Se calcula el area
    raiz = (lado_a+lado_b+lado_c)/2
    area = (raiz * (raiz-lado_a) * (raiz-lado_b) * (raiz-lado_c)) ** 0.5
    print("El area del triangulo es ",area)

# Se imprime el segun los datos ingresados
    if(lado_a == lado_b == lado_c):
        print("Usted es una calculadora")
    elif(lado_a == lado_b or lado_a== lado_c or lado_b==lado_c):
        print("Bien, bien, no muy bien pero bien")
    else:
        print("Sería bueno hacer más cálculos mentales")


else:
    print("\nLos lados no corresponde a un triángulo")

