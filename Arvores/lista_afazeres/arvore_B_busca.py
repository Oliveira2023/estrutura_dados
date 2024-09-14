import vertice as V

class ArvoreBinariaBusca:
    def __init__(self):
        self.raiz = None
        

    def inserir(self, chave, dado):
        
        if self.raiz is None:
            self.raiz = V.Vertice(chave, dado) # cria um vertice raiz
        else:
            self.raiz.inserir(chave, dado) # vai pro vertice inserir

    def remover(self, chave):
        if self.raiz:
            removido = self.raiz.remover(chave) # vai pro vertice remover
            if removido is self.raiz:
                self.raiz = None

    def imprimir(self):
        if self.raiz:
            self.raiz.imprimir()
