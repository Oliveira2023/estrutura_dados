class BibliotecaVirtual:
    def __init__(self) -> None:
        # Dicionario para armazenar os livros. A chave é o titulo do livro.
        self.livros = {} # inicio da biblioteca com um dicionário vazio

    def adicionar_livro(self,titulo, autor, ano):
        if titulo in self.livros:
            print("Livro ja existente na biblioteca.")
        else:
            self.livros[titulo] = {"autor": autor, "ano": ano}
            print("Livro adicionado com sucesso.")

    def remover_livro(self, titulo):
        if titulo in self.livros:
            del self.livros[titulo]
            print("Livro removido com sucesso.")
        else:
            print("Livro inexistente na biblioteca.")

    def pesquisar_livro(self, titulo):
        if titulo in self.livros:
            return self.livros.get(titulo, 'Nenhum livro encontrado.')
        
    def listar_livros(self):
        for titulo, infos in self.livros.items(): #items são chave e valor. no caso, o titulo é a chave e infos o valor
            # como o valor é um dic aninhado, temos as opções de autor e ano dentro.
            print(f"{titulo} - {infos['autor']} - {infos['ano']}")

# Exemplo de uso
biblioteca = BibliotecaVirtual()
biblioteca.adicionar_livro("1984", "George Orwell", 1949)
biblioteca.adicionar_livro("A Arte da Guerra", "Sun Tzu", 500)
biblioteca.adicionar_livro("Dom Casmurro", "Machado de Assis", 1899)

biblioteca.listar_livros()
biblioteca.remover_livro("A Arte da Guerra")
biblioteca.listar_livros()

print(biblioteca.pesquisar_livro("1984"))