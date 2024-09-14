import arvoreAvl as avl
class Catálogo:
    def __init__(self):
        self.avl = avl.ArvoreAVL()

    def atualizar(self, produto):
        """
        Atualiza o catálogo de produtos
        inserindo um produto novo ou atualizando dados
        de um existente.
        """
        encontrado = self.avl.buscar(produto.codigo)
        if encontrado:
            encontrado.dado.atualizar(produto)
        else:
            self.avl.inserir(produto.codigo, produto)
        
    def inserir(self, posicao, produto):
        self.avl.inserir(posicao, produto)

    def obter_produto(self, posicao):
        vertice = self.avl.buscar(posicao)
        if vertice:
            return vertice.dado
