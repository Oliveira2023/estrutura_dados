import array as arr # biblioteca para tratar arrays
import builtins

m = 15 # numero de indices na tabela

#inicialização da tabela como array de inteiros de 15 posições com 0
hashtable = arr.array('i', [0] * m)

def hashfunct(v, mh): # função hash usando método da divisão
    return v % mh

def insereTC(valor):
    hashtable[hashfunct(valor, m)] += 1

def retornaValor(valor): # retorna o número de produtos para determinada chave.
    return hashtable[hashfunct(valor, m)]  

# testes
# 
print(hashtable)
print()
print("Digite o número da etiqueta com 10 algarismos:")
x = int(input())
insereTC(x)
print()
print("Tabela atualizada")
print(hashtable)
print("Digite uma etiqueta para buscar a quantidade de produtos:")
x = int(input())
print()
print("Quantidade de produtos:", retornaValor(x)) 