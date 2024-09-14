class ItemLista:
    #""" Representa cada item de uma lista encadeada"""
    def __init__(self, data=0, nextItem=None):
        self.data = data
        self.nextItem = nextItem

    def __repr__(self): #retorna uma mensagem para cada objeto apresentando  o item na lista
        return '%s => %s' % (self.data, self.nextItem)
    
class ListaEncadeada:
    #""" Cria uma lista encadeada"""
    def __init__(self):
        self.head = None

    def __repr__(self):
        return '%s' % (self.head)
    
    def insert(self, data):
        # cria um objeto para armazenar um novo item da lista
        newItem = ItemLista(data)
        # o head é apontado como próximo item
        newItem.nextItem = self.head
        # o item atual se torna o head
        self.head = newItem

    def search(self, data):
        # percorre a lista
        current = self.head
        while current and current.data != data:
            current = current.nextItem
        return current.data
    
    def delete(self, data):
        current = self.head
        if current.data == data:
            self.head = current.nextItem
        else:
            while current and current.data != data:
                previous = current
                current = current.nextItem
            if current.data == data:
                print(current.data, ' deletado')
                previous.nextItem = current.nextItem
            else:
                raise ValueError("Item not found")
            
        
