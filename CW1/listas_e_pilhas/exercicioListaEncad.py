class Node: #nó representa a demanda na fila
    def __init__(self, id):
        self.id = id
        self.next = None

    def __repr__(self):
        return "%s" % (self.id)
        

class Queue: #fila - gerencia os processos
    def __init__(self):
        self.head = None
        self.tail = None #fim -cauda

    def __repr__(self):
        return "%s" % (self.head)
    def enqueue(self, id): #enfileirar - push
        new_node = Node(id)

        if self.tail:
            
            self.tail.next = new_node #se já tiver um elemento na cauda, o novo elemento será o proximo, estou dizendo que o self.tail atual agora vai apontar para o novo elemento
            
            
        self.tail = new_node #o novo elemento é a cauda agora

        if not self.head:
            self.head = new_node
        

    def dequeue(self): #desenfileirar - pop
        if not self.head: #verifica se a fila está vazia
            return None
        
        removed_id = self.head.id #elemento removido vai ser o elemento que estiver no head
        self.head = self.head.next #o head passa a apontar para o proximo

        if not self.head: #verifica se a fila ficou vazia
            self.tail = None #o tail passa a apontar para None
        return removed_id

    def peek(self): #imprime a fila completa.
        filaTotal = []
        atual = self.head
        while atual is not None:
            # print(atual.id)
            filaTotal.append(atual.id)
            atual = atual.next

        print(filaTotal)
    
process_queue = Queue() #cria uma fila vazia (head = None, next = None)
print("head:",process_queue.head,"tail:",process_queue.tail)
process_queue.enqueue(1)
print("head:",process_queue.head,"tail:",process_queue.tail)
process_queue.enqueue(2)
print("head:",process_queue.head,"tail:",process_queue.tail)
process_queue.enqueue(3)
print("head:",process_queue.head,"tail:",process_queue.tail)
process_queue.enqueue(4)
print("head:",process_queue.head,"tail:",process_queue.tail)
process_queue.enqueue(5)
print("head:",process_queue.head,"tail:",process_queue.tail)

# print(process_queue)
process_queue.peek()

print(process_queue.dequeue())
print(process_queue.dequeue())
# print(process_queue.dequeue())
# print(process_queue.dequeue())

process_queue.peek()