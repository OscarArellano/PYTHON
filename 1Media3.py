#Programa que permita obtener la media de 3 numeros


b,num,suma=0,5,0
print("PARA SALIR INGRESA CERO\n")
while(num!=0):
 num=int(input("Ingresa numero\n"))
 suma=suma+num
 b=b+1
print 'Media aritmetica es: ',(suma/(b-1))




