valor=""

while len(valor)!= 1:
    print("Ingrese un solo caracter")
    valor=input("Ingrese Valor: ")
    print(" ")

print ("El valor es: ",valor)

if (ord(valor)>=0)and (ord(valor)<=32):
    print("El valor",'"',valor,'"',"representa una ACCION el codigo ASCII:",ord(valor))
   
if(ord(valor)>=33) and (ord(valor)<=47):
        print("El valor",'"',valor,'"',"representa un SIMBOLO el codigo ASCII:",ord(valor))

if(ord(valor)>=48)and (ord(valor)<=57):
        print("El valor",'"',valor,'"',"representa un NUMERO el codigo ASCII:",ord(valor))

if(ord(valor)>=58)and (ord(valor)<=64):
        print("El valor",'"',valor,'"',"representa un simbolo el codigo ASCII:",ord(valor))

if(ord(valor)>=65)and (ord(valor)<=90):
        print("El valor",'"',valor,'"',"representa una LETRA MAYUSCULA el codigo ASCII:",ord(valor))

if(ord(valor)>=91)and (ord(valor)<=96):
        print("El valor",'"',valor,'"',"representa un SIMBOLO el codigo ASCII:",ord(valor))
if(ord(valor)>=97)and (ord(valor)<=122):
        print("El valor",'"',valor,'"',"representa una LETRA MINUSCULA el codigo ASCII:",ord(valor))

if(ord(valor)>=123)and (ord(valor)<=127):
        print("El valor",'"',valor,'"',"representa una SIMBOLO el codigo ASCII:",ord(valor))

if(ord(valor)>=128)and (ord(valor)<=165):
        print("El valor",'"',valor,'"',"representa una LETRA CON ACENTO el codigo ASCII:",ord(valor))

if(ord(valor)>=166)and (ord(valor)<=180):
        print("El valor",'"',valor,'"',"representa una SIMBOLO el codigo ASCII:",ord(valor))

if(ord(valor)>=181)and (ord(valor)<=183):
        print("El valor",'"',valor,'"',"representa una LETRA CON ACENTO el codigo ASCII:",ord(valor))

if(ord(valor)>=184)and (ord(valor)<=197):
        print("El valor",'"',valor,'"',"representa una SIMBOLO el codigo ASCII:",ord(valor))

if(ord(valor)>=198)and (ord(valor)<=199):
        print("El valor",'"',valor,'"',"representa una LETRA CON ACENTO el codigo ASCII:",ord(valor))

if(ord(valor)>=200)and (ord(valor)<=207):
        print("El valor",'"',valor,'"',"representa una SIMBOLO el codigo ASCII:",ord(valor))

if(ord(valor)>=208)and (ord(valor)<=216):
        print("El valor",'"',valor,'"',"representa una LETRA CON ACENTO el codigo ASCII:",ord(valor))

if(ord(valor)>=217)and (ord(valor)<=223):
        print("El valor",'"',valor,'"',"representa una SIMBOLO el codigo ASCII:",ord(valor))

if(ord(valor)>=224)and (ord(valor)<=237):
        print("El valor",'"',valor,'"',"representa una LETRA CON ACENTO el codigo ASCII:",ord(valor))

if(ord(valor)>=238)and (ord(valor)<=255):
        print("El valor",'"',valor,'"',"representa una LETRA CON ACENTO el codigo ASCII:",ord(valor))


