#Realiza una función que permita obtener el máximo de 3 números.

 
A=int(input("Ingrese primer numero\n"))
B=int(input("Ingrese segundo numero\n"))
C=int(input("Ingrese tercer numero\n"))
if(A > B and A > C):
 print("El numero mayor es " + str(A))
else:
 if(B > A and B > C):
  print("El numero mayor es " + str(B))
 else:
  print("El numero mayor es " + str(C))
