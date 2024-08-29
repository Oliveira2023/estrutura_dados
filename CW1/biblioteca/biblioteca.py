import emprestimo

class Emprestimo: 
    def __init__(self, titulo, data_emprestimo, data_devolucao):
        self.titulo = titulo
        self.data_emprestimo = data_emprestimo
        self.data_devolucao = data_devolucao

livros = {
    "ISBN1": {
        "titulo": "A Arte da Guerra",
        "autor": "Sun Tzu",
        "ano": 500
    },
    "ISBN2": {
        "titulo": "1984",
        "autor": "George Orwell",
        "ano": 1949
    }
}

emprestimo1 = emprestimo.Emprestimo(livros["ISBN1"]["titulo"], "10/10/2021", "10/10/2022")

print(emprestimo1.titulo)
