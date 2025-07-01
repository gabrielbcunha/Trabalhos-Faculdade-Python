#Criação dos elementos da lista
class ElementoDaListaSimples:
    def __init__(self, numero, cor):
        self.numero = numero
        self.cor = cor
        self.proximo = None

    def __repr__(self):
        return f"{self.numero}, {self.cor})"

#Criação da Lista Encadeada Simples
class ListaEncadeadaSimples:
    def __init__(self, nodos=None):
        self.head = None
        self.contador_A = 201 #A começa no 201
        self.contador_V = 1 #V começa no 1

        if nodos is not None:
            numero, cor = nodos.pop(0)
            nodo = ElementoDaListaSimples(numero=numero, cor=cor)
            self.head = nodo
            for numero, cor in nodos:
                novo = ElementoDaListaSimples(numero=numero, cor=cor)
                nodo.proximo = novo
                nodo = novo

    def __repr__(self):
        nodo = self.head
        nodos = []
        while nodo is not None:
            nodos.append(str(nodo))  # usa __repr__ do nodo
            nodo = nodo.proximo
        nodos.append("None")
        return " -> ".join(nodos)

    def inserirSemPrioridade(self, nodo):
        if self.head is None:
            self.head = nodo
            return

        nodo_atual = self.head
        while nodo_atual.proximo != None:
            nodo_atual = nodo_atual.proximo

        nodo_atual.proximo = nodo
        return

    def inserirComPrioridade(self, nodo):
        if self.head is None:
            self.head = nodo
            return
        elif self.head.cor != 'A':
            nodo.proximo = self.head
            self.head = nodo
            return

        nodo_atual = self.head
        while nodo_atual.proximo is not None and nodo_atual.proximo.cor == 'A':
            nodo_atual = nodo_atual.proximo

        nodo.proximo = nodo_atual.proximo
        nodo_atual.proximo = nodo

    def inserir(self):

        cor = input("Informe a cor do cartão (A/V)").strip().upper()

        if cor != 'A' and cor != 'V':
            print("Por favor insira uma opção válida")
            return

        if cor == 'A':
            numero = self.contador_A
            self.contador_A += 1

        if cor == 'V':
            numero = self.contador_V
            self.contador_V += 1

        nodo = ElementoDaListaSimples(numero, cor)

        if self.head is None:
            self.head = nodo
        elif cor == 'A':
            self.inserirComPrioridade(nodo)
        elif cor == 'V':
            self.inserirSemPrioridade(nodo)

    def imprimirListaEspera(self):
        if self.head is None:
            print("Lista de espera vazia")
            return

        nodo = self.head
        nodos = []

        while nodo:
            nodos.append(f"[{nodo.cor},{nodo.numero}]")
            nodo = nodo.proximo
        print("Lista -> " + " ".join(nodos))

    def atenderPaciente(self):
        if self.head is None:
            print("Lista de espera vazia")
            return

        paciente_atendido = self.head
        self.head = paciente_atendido.proximo
        print(f"Atendendo o paciente cartão cor {paciente_atendido.cor} e número {paciente_atendido.numero}")


def menu():
    fila = ListaEncadeadaSimples()
    while True:
        print("Escolha uma Opção")
        print("1 - Adicionar pacientes a fila")
        print("2 - Mostrar pacientes na fila")
        print("3 - Chamar paciente")
        print("4 - Sair")
        escolha = int(input(">>"))

        if escolha == 1:
            fila.inserir()
        elif escolha == 2:
            fila.imprimirListaEspera()
        elif escolha == 3:
            fila.atenderPaciente()
        elif escolha == 4:
            print("Obrigado por utilizar o sistema. Encerrando...")
            break
        else:
            print("Por favor insira uma opção válida")

menu()