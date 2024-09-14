import ListaEncadeada as le #importando a lista para poder usar os metodos aqui

lista = le.ListaEncadeada() #instancio uma lista encadeada- objeto chamado lista
print("Conteúdo da lista(vazia):", lista) # lista está vazia)
lista.insere(lista, 'biscoito') #inserindo alguns itens
lista.insere(lista, 'detergente')
lista.insere(lista, 'abobrinha ')
lista.insere(lista, 'banana')
print("Conteúdo da lista: ",lista)

listaCompras = le.ListaEncadeada()
listaCompras.insereSemLista("abacate")
listaCompras.insereSemLista("legumes")
listaCompras.insereSemLista("arroz")
print("listaCompras: ", listaCompras)
listaCompras.removeSemLista("legumes")
print("listaCompras: ", listaCompras)
listaCompras.removeSemLista("leite") #item não existe, teste
print("listaCompras: ", listaCompras)

listaDeTarefas = le.ListaEncadeada()
listaDeTarefas.insere(listaDeTarefas, 'limpar o banheiro')
listaDeTarefas.insere(listaDeTarefas, 'limpar o quarto')
listaDeTarefas.insere(listaDeTarefas, 'limpar a cozinha')
listaDeTarefas.insere(listaDeTarefas, 'lavar a louça')
print("lista de tarefas: ", listaDeTarefas)

lista.remove('banana')
print("Conteúdo da lista: ",lista)

listaDeTarefas.remove('limpar o quarto')
print("lista de tarefas: ", listaDeTarefas)

print(" ")
#busca de itens
query = "biscoito" #item buscado
item_buscado = lista.busca(query) #função de busca na listaEncadeada
if item_buscado: #se encontrar printa a mensagem encontrado
    print("Item encontrado: ", item_buscado.data)
else: #se não encontra printa a mensagem não encontrado
    print("Item não encontrado")