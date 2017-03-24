#Programa que permita generar un intervalo de los
#cuadrados de n numeros mayores a 100
    
n = int(input("Cantidad de numeros:\n"))
print "Introducir numero que el cuadrado sea >100"
while n > 0:
    num = int(input("Numero: "))
    n = n - 1
    c=num**2
    if c > 100:
        print "El cuadrado es: ",c
    else:
        print "El cuadrado no es mayor a 100"
    

