class Prontuario: #item do prontuário
    def __init__(self, paciente, diagnostico, tratamento, proximo=None):
        self.paciente = paciente
        self.diagnostico = diagnostico
        self.tratamento = tratamento
        self.proximo = proximo

    def __repr__(self):
        return "%s, %s, %s" % (self.paciente, self.diagnostico, self.tratamento)
        
class ListaEncadeadaProntuarios: #classe de objetos da lista de prontuários
    def __init__(self):
        self.head = None #quando instancia a classe cria o head vazio
        
    def __repr__(self):
        return "%s" % (self.head)

    def adicionar_prontuario(self, paciente, diagnostico, tratamento): #adiciona prontuario a lista de prontuários.
        novo_prontuario= Prontuario(paciente, diagnostico, tratamento, self.head)#cria um item da lista de prontuário
        self.head = novo_prontuario#adiciona o prontuario criado ao head da lista.

    def buscar_prontuario(self, nome_paciente):#busca de prontuáiros pelo nome do paciente
        atual = self.head #começando pelo head
        while atual: #enquanto tiver itens, continua a busca
            if atual.paciente == nome_paciente: #se o item atual for = ao item buscado retorna este item
                return atual
            atual = atual.proximo #e continua em busca de novos itens se não for igual
        return None 
    
sistema_prontuarios = ListaEncadeadaProntuarios()

sistema_prontuarios.adicionar_prontuario("Alice Santos", "Diabetes tipo 2", "Metformina")
sistema_prontuarios.adicionar_prontuario("João Silva", "Hipertensão", "Losartana")
sistema_prontuarios.adicionar_prontuario("Alice Santos", "Diabetes tipo 1", "Metformina")
sistema_prontuarios.adicionar_prontuario("Alice Santos", "Diabetes tipo 3", "Metformina")
sistema_prontuarios.adicionar_prontuario("João Silva", "Hipertensão", "Losartana")

prontuario_alice = sistema_prontuarios.buscar_prontuario("Alice Santos")
print(prontuario_alice)