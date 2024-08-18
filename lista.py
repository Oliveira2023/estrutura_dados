
#listas sao mutaveis
frutas = ['maca', 'banana', 'laranja']
print(frutas)

frutas.append('uva')
print(frutas)
frutas.remove
len(frutas)
#tuplas sao imutaveis
tupla = ('maca', 'banana', 'laranja')
tupla2 = "sempre", "uma", "tupla"

#dicionarios sao mutaveis - chaves e valores
dicionario = {'maca': 1, 'banana': 2, 'laranja': 3}
dicionario['maca'] = 0
chaves_dicionario = dicionario.keys()
print(chaves_dicionario)

#set elementos unicos
set = {'maca', 'banana', 'laranja', 'maca'}

#conjuntos sao mutaveis
conjunto = {'maca', 'banana', 'laranja', 'maca'}    
consuntoNumerico = {1, 2, 3, 4, 7, 8, 9, 10}
consuntoNumerico2 = {1, 2, 3, 4, 5, 6, 10, 10, 10, 10, 10}   #não permite valores repetidos, o que acontece com esta declaração?
consuntoNumerico.add(11)
consuntoNumerico2.remove(2)
uniaoConjuntos = consuntoNumerico.union(consuntoNumerico2)
print(uniaoConjuntos)