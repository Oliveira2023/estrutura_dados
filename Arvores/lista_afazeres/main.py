import lista as ABB

# Criação da lista de afazeres

# quando cria esta lista de afazeres a 
# lista cria no construtor uma arvore de busca binaria
afazeres = ABB.ListaDeAfazeres() 

while True:

    try:

        afazeres.listar()
        # op = input("Escolha uma opção: ")
        op = input(
            """
            Digite i para inserir atividade
            Digite r para remover atividade
            Digite x para sair
            """
        )
        print(op)
        if op == "x":
            print("saindo...")
            break
        if op == "i":
            atividade = input("Entre com a atividade: ")
            ordem = int(input("Entre com a ordem (numero): "))
            afazeres.inserir(ordem, atividade)
            continue

        if op == "r":
            ordem = int(input("Entre com a ordem (numero): "))
            afazeres.remover(ordem)
            continue

    except Exception as e:
        print("Terminado pelo usuario ou erro: {}".format(e))
        break