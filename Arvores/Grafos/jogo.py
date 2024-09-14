import grafo as gf

# INICIO DO PROGRAMA

arestas = [
    ('v1', 'v2'),
    ('v1', 'v3'),
    ('v1', 'v4'),
    ('v1', 'v5'),
    ('v2', 'v3'),
    ('v2', 'v4'),
    ('v2', 'v5'),
    ('v3', 'v4'),
    ('v3', 'v5'),
    ('v4', 'v5'),

    ('v1A', 'v2A'),
    ('v1A', 'v3A'),
    ('v1A', 'v4A'),
    ('v1A', 'v5A'),
    ('v2A', 'v3A'),
    ('v2A', 'v4A'),
    ('v2A', 'v5A'),
    ('v3A', 'v4A'),
    ('v3A', 'v5A'),
    ('v4A', 'v5A'),

    ('v1B', 'v2B'),
    ('v1B', 'v3B'),
    ('v1B', 'v4B'),
    ('v1B', 'v5B'),
    ('v2B', 'v3B'),
    ('v2B', 'v4B'),
    ('v2B', 'v5B'),
    ('v3B', 'v4B'),
    ('v3B', 'v5B'),
    ('v4B', 'v5B'),

    ('v1C', 'v2C'),
    ('v1C', 'v3C'),
    ('v1C', 'v4C'),
    ('v1C', 'v5C'),
    ('v2C', 'v3C'),
    ('v2C', 'v4C'),
    ('v2C', 'v5C'),
    ('v3C', 'v4C'),
    ('v3C', 'v5C'),
    ('v4C', 'v5C'),

    ('v1D', 'v2D'),
    ('v1D', 'v3D'),
    ('v1D', 'v4D'),
    ('v1D', 'v5D'),
    ('v2D', 'v3D'),
    ('v2D', 'v4D'),
    ('v2D', 'v5D'),
    ('v3D', 'v4D'),
    ('v3D', 'v5D'),
    ('v4D', 'v5D'),

    ('v1E', 'v2E'),
    ('v1E', 'v3E'),
    ('v1E', 'v4E'),
    ('v1E', 'v5E'),
    ('v2E', 'v3E'),
    ('v2E', 'v4E'),
    ('v2E', 'v5E'),
    ('v3E', 'v4E'),
    ('v3E', 'v5E'),
    ('v4E', 'v5E'),

    ('v1A', 'v4'),
    ('v2A', 'v1E'),
    ('v3A', 'v1D'),
    ('v4A', 'v1C'),
    ('v5A', 'v1B'),
]

grafo = gf.Grafo()
vertice = gf.Vertice()
# insere as arestas do grafo
grafo.inserir_arestas(arestas)

sala_atual = 'v1'
while True:
    print("")

    # obtém o objeto da classe Vertice, para obter seus vizinhos
    sala = grafo.obter_vertice(sala_atual)

    # obtém os vizinhos, ou seja, as salas adjacentes
    salas_vizinhas = gf.Vertice.ids_dos_adjacentes(sala)

    # solicita ao usuário que entre uma das salas apresentadas
    sala_escolhida = input(
        "Escolha uma das SALAS : {}\n>>> ".format(" ".join(salas_vizinhas)))

    if sala_escolhida not in salas_vizinhas:
        # a sala não existe, interrompe o programa
        print("Fim de jogo")
        break

    # a sala atual passa a ser a sala escolhida
    sala_atual = sala_escolhida