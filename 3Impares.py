#Programa que obtiene la intercalacion de
#10 numero impares empezando desde el 13

n = 13
h = ''
while n <= 31:
    if n%2 != 0:
        h += ' %i' % n
    n += 1
print h
