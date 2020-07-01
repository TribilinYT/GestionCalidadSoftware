# @autor Meza cedeño Galo

# Ejercicio 20

# Por ciclo for y rango que hará que se muestren los pirmeros 
# números perfectos 
for i in range(2,9000):
    numero = 0

    # Variable controlador tomará valores des 1
    for controlador in range(1, (i // 2) +1):


        #identifica el residuo de una división 
        if((i % controlador) == 0):
            numero = numero + controlador
    # Si la vanumero es igual a controlador imprimimos el mensaje       
    if(numero == i):
        print("El número  " + str(i) + "  es perfecto")
