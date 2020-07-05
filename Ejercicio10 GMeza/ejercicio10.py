# @autor Meza cedeño Galo
# Ejercicio 10


# Menu que se muestra el medio de tranporte a elegir
print("---------------Elija el medio de transporte------------- ")
menu = int(input("\n1. Bicicleta." 
                "\n2. Moto."
                "\n3. Auto."
                "\n4. Camión.\nIngrese opción: "))

# Validamos que los números de seleccion sean solo del 1 al 4
while menu!=1 and menu!=2 and menu!=3 and menu!=4:
    print("\nSelección no válida...")
    menu = int(input("1. Bicicleta." 
                "\n2. Moto."
                "\n3. Auto."
                "\n4. Camión\n Elija una opción :"))
                
# Como el valor de circulación de una bicicleta es fijo lo imprimimos irectamente                
if menu == 1:
     print("El valor de circulación de las bicicletas es fijo = 0.50 ctv")
     
   
# Selección 2 del menú 
elif menu == 2:
     print("--------------------------------")
     valor_moto = 0

     # while hace que no se puedan igresar valores negativos 
     while(float(valor_moto) <=0):
          valor_moto = float(input("Ingrese los km recorridos: "))
     a_pagar = valor_moto *  0.30
     print("El valor a pagar es: ", a_pagar, "dólares") 
     
# Selección 3 del menú 
elif menu == 3:
     print("--------------------------------")
     valor_auto = 0

     # while hace que no se puedan igresar valores negativos
     while(float(valor_auto) <=0):
          valor_auto = float(input("Ingrese los km recorridos: "))
     a_pagar = valor_auto *  0.30
     print("El valor a pagar es:" , a_pagar, "dólares")

# Selección 4 del menú 
elif menu == 4:
     print("--------------------------------")
     valor_camion = 0
     peso_camion = 0

     # while hace que no se puedan igresar valores negativos 
     while(float(valor_camion) <=0):
          valor_camion = float(input("Ingrese los km recorridos: "))
          a_pagar_camion = valor_camion * 0.50

     # while hace que no se puedan igresar valores negativos    
     while(float(peso_camion) <=0):
          peso_camion = float(input("Ingrese el valor de toneladas métricas del camión: "))
     a_pagar_peso = peso_camion *  0.10
     print("El valor a pagar es:",  a_pagar_peso + a_pagar_camion , "dólares")



