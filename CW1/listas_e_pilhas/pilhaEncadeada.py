class item:
    def __init__(self, valor= None, anterior= None):
        self.valor = valor
        self.anterior = anterior

    def __repr__(self):
        return "(%s\n%s" %(self.valor, self.anterior)
    
class Pilha:
    def __init__(self):
        self.head = None #cria uma plha vazia com o head que indica o topo da pilha

    def __repr__(self):
        return "%s" % (self.head)
    
    def push(self, valor): #Adiciona um item na pilha - emplilhar
        self.head = item(valor, self.head) # Cria um novo objeto Item e o atribui ao head
        # o head anterior (self.head) passa a ser o item anterior, parametro passado ao item


    def pop(self): #Retira um item da pilha - desempilhar
        assert self.head, "pilha vazia" # verifica se a pilha está vazia

        self.head = self.head.anterior # o head passa a ser o item anterior



def main():
    pilha = Pilha()
    pilha.push("a")
    # print("head:",pilha.head, 'tail:',pilha.head.anterior)
    pilha.push("b")
    # print("head:",pilha.head, 'tail:',pilha.head.anterior)
    pilha.push("c")
    # print("head:",pilha.head, 'tail:',pilha.head.anterior)
    pilha.push("d")
    print(pilha)
    # pilha.pop()
    # pilha.pop()
    print(pilha)

main()
