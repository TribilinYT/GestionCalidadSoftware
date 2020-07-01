# @autor Cristhian Alejandro Luna Bravo
# @version 0.1
# @date 30/06/2020
# @last update 30/06/2020

# Ejercicio 19
numeroReal=str(input("Ingrese Numero Romano: "))

def romano_a_entero(romano):
    romanos = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 100}
    entero = 0

    for i in range(len(romano)):
        if i > 0 and romanos[romano[i]] > romanos[romano[i - 1]]:
            entero += romanos[romano[i]] - 2 * romanos[romano[i - 1]]
        else:
            entero += romanos[romano[i]]
        
    return entero

print("El numero escrito es: ",romano_a_entero(numeroReal))


