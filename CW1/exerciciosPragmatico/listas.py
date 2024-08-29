def listagem(x):

    return x + x
# print(listagem('ha'))

def listagem2(x, a):
    for n in x:
        if n == a:
            return True
    return False
# print(listagem2([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3))

def listagem3(lista_ordenada, elemento):
    for i, n in enumerate(lista_ordenada):
        if n > elemento:
            return i
    return -1
# print(listagem3([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 15))


def encontra_duplicados(lista, m):
    if not lista:
        return []
    duplicados = []
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] == lista[j]:
                duplicados.append(lista[i])
    return duplicados
# print(encontra_duplicados([0, 1, 5, 2, 3, 4, 5, 6, 4, 7, 8, 2, 9, 10], 10))

def encontra_duplicados2(lista, m):
    if not lista:
        return []
    return [n for n in lista if lista.count(n) > 1]
# print(encontra_duplicados2([0, 1, 5, 2, 3, 4, 5, 6, 4, 7, 8, 2, 9, 10], 10))

def encontra_duplicados3(lista, m):
    if not lista:
        return []
    tabela_frequencia = [0] * m
    duplicatas = []
    for elemento in lista:
        tabela_frequencia[elemento] += 1
        print(elemento)
        if tabela_frequencia[elemento] > 1:
            duplicatas.append(elemento)
    return duplicatas
# print(encontra_duplicados3([0, 1, 1, 5, 2, 3, 4, 5, 6, 4, 7, 8, 2, 9, 10], 11))

def inverte_ordem(x):
    if not x:
        return []
    # return x[::-1]
    listaInvertida = []
    for elemento in x:
        listaInvertida.insert(0, elemento)
    return listaInvertida
# print(inverte_ordem([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

def zerosAlFinal(x):
    if not x:
        return []
    for elemento in x:
        if elemento == 0:
            x.append(elemento)
            x.remove(elemento)
    return x
print(zerosAlFinal([0, 1, 0, 3, 4, 5]))