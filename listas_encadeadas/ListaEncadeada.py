class ItemLista: #classe que representa cada item da lista
    def __init__(self, data=0, nexItem=None):
        self.data = data #dado do item
        self.next = nexItem #proximo item

    def __repr__(self):
        return "%s, %s" % (self.data, self.next)
    
class ListaEncadeada: #classe que representa a lista encadeada - que vai ser instanciada
    def __init__(self):
        self.head = None #quando instanciada cria o head

    def __repr__(self):
        return "%s" % (self.head) #representação da lista.
    
    def insere(self, lista, data): #metodo para inserir um item na lista
        item = ItemLista(data) #cria um novo item para armazenar na lista
        item.next = lista.head #next é apontado para o proximo item, que era o head antes
        lista.head = item #item atual se torna o head
    def insereSemLista(self, data):#metodo de inserir sem necessidade de enviar a lista,
        item = ItemLista(data) #já que ela está na chamada do metodo e acessa pelo self.
        item.next = self.head
        self.head = item

    def remove(lista,valor):
        if (lista.head and lista.head.data == valor): #verifica se o item a remover é o Head
            lista.head = lista.head.next
        else:
            before = None
            navegar = lista.head
            # print (before, navegar)
            while (navegar and navegar.data != valor):
                before = navegar
                navegar = navegar.next
            if (navegar):
                before.next = navegar.next

    def removeSemLista(self, valor):
        if (self.head and self.head.data == valor): #verifica se o item a remover é o Head
            self.head = self.head.next #O head vai ser o próximo do próprio head
        else:
            # Detecta a posição do elemento
            before = None
            navegar = self.head# navegar vai ser o head
            # print (before, navegar)
            while (navegar and navegar.data != valor):# Navega pela lista para encontrar o elemento
                before = navegar #o before vai ser igual o navegar que será o head 
                navegar = navegar.next #e navegar vai ser o proximo item da lista, se este item for o procurado ele pára a busca.
                #quando chega no final da lista sem encontrar o item??
            if (navegar):
                before.next = navegar.next    #o item anterior vai apontar para o proximo item agora.

    def busca(lista,valor):
        navegar = lista.head # o valor de navegar a principio vai ser o head
        while (navegar and navegar.data != valor): #enquanto navegar não vor igual ao valor procurado segue.
            navegar = navegar.next #navegar vai para o proximo item da lista.
        return (navegar) #retorna o item procurado.
    
