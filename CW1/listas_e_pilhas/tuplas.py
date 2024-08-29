#forma de declarar uma dupla
tupla = (1, 2, 3)

# outra forma de declarar uma tupla
tupla2 = 1, 2, 3
print(tupla)
print(tupla2)

# Desempacotamento de tuplas
tupla = (1, 2, 3)
a, b, c = tupla
print('a: ',a)
print('b: ',b)
print('c: ',c)

print()
print('for na tupla')
for i in tupla:
    print(i)