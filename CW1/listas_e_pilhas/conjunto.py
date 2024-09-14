conjunto = set([1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10])
conjunto2 = {1, 2, 11, 4, 12, 5, 32, 7, 14, 9, 10}

conjunto.add(777)

print(conjunto)

conjunto.remove(777)

print(conjunto)

print('diferença')
print(conjunto2 - conjunto)
print('interseccão')
print(conjunto2 & conjunto)
print('uniao')
print(conjunto2 | conjunto)
