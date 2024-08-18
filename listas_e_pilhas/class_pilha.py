class Pilha:
    def __init__(self):
        self.items = []

    def __repr__(self):
        return "%s" % (self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.items:
            return self.items.pop()
        else:
            return None
        
# Exemplo de uso da pilha. nesse caso poderia ser outro arquivo

myStack = Pilha()
myStack.push(1)
myStack.push(2)
myStack.push(3)
print(myStack)
print(myStack.pop())
print(myStack.pop())
print(myStack.pop())