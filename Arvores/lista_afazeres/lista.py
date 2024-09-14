import arvore_B_busca as ABB
class ListaDeAfazeres:
    def __init__(self):
        self.arvore = ABB.ArvoreBinariaBusca()

    def inserir(self, ordem, atividade): # ordem é a chave
        self.arvore.inserir(ordem, atividade) # vai pro arvore inserir

    def remover(self, ordem):
        self.arvore.remover(ordem)

    def listar(self):
        print("_" * 20)
        print("Lista de afazeres:")
        self.arvore.imprimir() # vai pro imprimir no vertice
        print("_" * 20)
