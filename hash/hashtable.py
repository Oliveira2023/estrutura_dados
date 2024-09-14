hashtable = {}
m = 10 # numero de indices na tabela

def hashfunct(v, mh): # função hash usando método da divisão
    return v % mh

def insereTC(valor):
    if hashtable[hashfunct(valor, m)] == '':
        hashtable[hashfunct(valor, m)] = valor
    else:
        print('Colisão!')
        print('Valor ', valor, ' não inserido!')
for i in range (m): # preenchendo indices da tabela
    hashtable[i] = ''

# inserindo elementos na tabela (numeros)
insereTC(235)
insereTC(578)
insereTC(1024)
insereTC(96)
insereTC(32)

print(hashtable) # exibindo a tabela

# inserção sem tratamento de colisão
# se houver colisão, o elemento é substituido
insereTC(18)

print(hashtable) # exibindo a tabela