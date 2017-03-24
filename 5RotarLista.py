#Programa que permite rotar una lista


import collections

lista= [3,2,5,7]
print lista

#primera vuelta
lista = collections.deque([3,2,5,7])
lista.rotate(3)

print lista

#segunda vuelta
lista = collections.deque([2,5,7,3])
lista.rotate(3)

print lista

#tercera vuelta
lista = collections.deque([5,7,3,2])
lista.rotate(3)

print lista
