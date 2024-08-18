class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def __repr__(self):
        return "%s" % (self.value)
    
    def add_child(self, child_node):
        self.children.append(child_node)

    def get_children(self):
        return self.children
    
root = Node('Classification') #cria a raiz  

livre = Node('Livre') # crio outros nós
dez_anos = Node('10 anos')
doze_anos = Node('12 anos')
quatorze_anos = Node('14 anos')
dezesseis_anos = Node('16 anos')
dezoito_anos = Node('18 anos')

root.add_child(livre)
root.add_child(dez_anos)
root.add_child(doze_anos)
root.add_child(quatorze_anos)
root.add_child(dezesseis_anos)
root.add_child(dezoito_anos)

livre.add_child(Node("Toy Story"))
livre.add_child(Node("Vida de Menina"))
livre.add_child(Node("O Lobo de Wall Street"))

dez_anos.add_child(Node("Cidade de Deus"))
dez_anos.add_child(Node("Cidadao Kane"))
dez_anos.add_child(Node("O Resgate do Soldado Ryan"))

doze_anos.add_child(Node("Os Sete Pecados Capitais"))

quatorze_anos.add_child(Node("O Padrão-14"))

dezesseis_anos.add_child(Node("O Padrão -16"))

dezoito_anos.add_child(Node("O Padrão-18"))

# print(livre.get_children())

def recomendar_filmes(root, idade):
    recomendacoes = []
    for child in root.get_children():
        if idade >= obter_idade_minima(child.value):
            for filme in child.get_children():
                recomendacoes.append(filme.value)
    return recomendacoes

def obter_idade_minima(faixa_etaria):
    if faixa_etaria == '10 anos':
        return 10
    elif faixa_etaria == '12 anos':
        return 12
    elif faixa_etaria == '14 anos':
        return 14
    elif faixa_etaria == '16 anos':
        return 16
    elif faixa_etaria == '18 anos':
        return 18
    else:
        return 0
    
print(recomendar_filmes(root, 13))
