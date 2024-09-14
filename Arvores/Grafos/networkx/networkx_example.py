import matplotlib.pyplot as plt
import networkx as nx

class visualizacaoGrafo:
    
    def __init__(self):
        self.visual = []

    def adicionarAresta(self, a, b):
        temp = [a, b] # armazena a aresta temporária
        self.visual.append(temp) # insere na lista visual

    def desenhar(self):
        G = nx.Graph() # cria-se um grafo G
        #adiciona-se então a lista de arestas a G
        G.add_edges_from(self.visual)
        # Executa-se a funçãõ de desenho
        nx.draw_networkx(G, node_color='lightgrey')
        # o grafo é então desenhado na tela
        plt.show()

G = visualizacaoGrafo()
G.adicionarAresta('Pedro', 'CP')
G.adicionarAresta('Pedro', 'Carla')
G.adicionarAresta('Carla', 'CP')
G.adicionarAresta('Pedro', 'CC')
G.adicionarAresta('Joao', 'CC')
G.desenhar()
