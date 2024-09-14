import ListaEncadeada as le

# Cria o objeto
lista = le.ListaEncadeada()

print('Conteúdo da lista:', lista)

# Insere itens na lista
lista.insert('abacate')
lista.insert('biscoito')
lista.insert('cenoura')
lista.insert('desodorante')
lista.insert('Espinafre')

print('Conteúdo da lista:', lista)

# Busca itens na lista
print ('Busca cenoura: ', lista.search('cenoura'))

# Remove itens da lista
lista.delete('cenoura')

print('Conteúdo da lista:', lista)