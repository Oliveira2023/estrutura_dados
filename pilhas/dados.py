class Dados:

    def __init__(self) -> None:
        self.itens = []

    def __repr__(self):
        return str(self.itens)
    
    def push(self, item):
        self.itens.append(item)

    def pop(self):
        return self.itens.pop()
    
    def seach(self, item):
        while self.itens:
            if self.itens[-1] == item:
                return True
            else:
                self.itens.pop()
        return False
def main():
    dados = Dados()
    dados.push(1)
    dados.push(2)
    dados.push(3) #ultimo item adicionado
    print(dados)
    print(dados.pop()) # item removido
    print(dados)

    familia = Dados()
    familia.push('Lucas')
    familia.push('Maria')
    print(familia)
    parentes = familia.seach('Lucas')
    if parentes:
        print('São parentes')
    else:
        print('Não são parentes')

if __name__ == '__main__': #__name__: Quando um arquivo Python é executado, 
    #o interpretador define algumas variáveis especiais. Uma delas é __name__. 
    #Se o arquivo está sendo executado diretamente, __name__ é definido como
    #  "__main__". Se o arquivo está sendo importado como um módulo em outro 
    # script, __name__ será o nome do módulo.
    main()