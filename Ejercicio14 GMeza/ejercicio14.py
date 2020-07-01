# @autor Meza cedeño Galo


# Ejercicio 14

#declaramos variables 
print('Calculo de la depreciación anual de un valor')
numAnos = float(input('Introduce el número de años: '))
valorInicial = float(input('Introduce el valor del vehiculo: '))

# Definimos que condicional al número de datos
def calcularDenominador(numAnos):
    denominador = 0
    while numAnos!=0:
        denominador=denominador+numAnos
        numAnos=numAnos-1
    return denominador

i = 0
denominador = calcularDenominador(numAnos)

# Última condicional que posterior muestra los resultados
while numAnos!=0:
    ano = 0
    ano=ano+1
    print('Final del año: ', ano)
    depreciacion = valorInicial*(numAnos/denominador)
    print('Depreciacion: ', depreciacion)
    valorActual = valorInicial-depreciacion
    print('Valor actual: ', valorActual)
                    
    numAnos=numAnos-1
