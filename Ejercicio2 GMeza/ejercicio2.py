# @autor Meza cedeño Galo


# Ejercicio 2

# Menu que se muestra para el tio de conversión a realizar
menu = int(input("1. De millas marinas a kilómetros" 
                "\n2. De millas marinas a metros"
                "\n3. De millas marinas a decímetros"
                "\n4. De millas marinas a centímetros\n Elija una opción :"))

# Validamos que los números ungresados sean los correctos
while menu!=1 and menu!=2 and menu!=3 and menu!=4:
    print("\nSelección no válida...")
    menu = int(input("1. De millas marinas a kilómetros" 
                "\n2. De millas marinas a metros"
                "\n3. De millas marinas a decímetros"
                "\n4. De millas marinas a centímetros\n Elija una opción :"))

    
# if que actua para que el dato ingresado se muetre en kilometros 
if menu == 1:
     print("--------------------------------")
     millas_marinas = 0
     while(int(millas_marinas) <=0):
          millas_marinas = int(input("Ingrese cantidad de millas marinas a convertir: "))
     
     kilometros = millas_marinas *  1.852
     print(millas_marinas, "millas marinas equivale a", kilometros,"kilómetros")

# if que actua para que el dato ingresado se muetre en metros
elif menu == 2:
     print("--------------------------------")
     millas_marinas = 0
     while(int(millas_marinas) <=0):
          millas_marinas = int(input("Ingrese cantidad de millas marinas a convertir: "))
     metros = millas_marinas *  1852
     print(millas_marinas, "millas marinas equivale a", metros,"metros") 
     
# if que actua para que el dato ingresado se muetre en decimetros
elif menu == 3:
     print("--------------------------------")
     millas_marinas = 0
     while(int(millas_marinas) <=0):
          millas_marinas = int(input("Ingrese cantidad de millas marinas a convertir: "))
     decimetros = millas_marinas *  18520
     print(millas_marinas, "millas marinas equivale a", decimetros,"decímetros")

# if que actua para que el dato ingresado se muetre en centimetros
elif menu == 4:
     print("--------------------------------")
     millas_marinas = 0
     while(int(millas_marinas) <=0):
          millas_marinas = int(input("Ingrese cantidad de millas marinas a convertir: "))
     centimetros = millas_marinas *  185200
     print(millas_marinas, "millas marinas equivale a", centimetros,"centímetros")






    