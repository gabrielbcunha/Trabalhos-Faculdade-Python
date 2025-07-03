class ElementoDaListaSimples:
    def __init__(self, sigla, nomeEstado):
        self.sigla = sigla
        self.nomeEstado = nomeEstado
        self.proximo = None

    def __repr__(self):
        return f"{self.sigla}, {self.nomeEstado}"

class TabelaHash:
    def __init__(self):
        self.tabela = [None] * 10

    def hashFunc(self, sigla):
        if sigla.upper() == "DF":
            return 7
        else:
            return (ord(sigla[0]) + ord(sigla[1])) % 10

    def inserirNoInicio(self, sigla, nomeEstado):
        i = self.hashFunc(sigla)
        novo = ElementoDaListaSimples(sigla, nomeEstado)
        novo.proximo = self.tabela[i]
        self.tabela[i] = novo

    def imprimirTabelaHash(self):
        for i, head in enumerate(self.tabela):
            print(f"{i}:", end=" ")
            atual = head
            while atual:
                print(f"{atual.sigla}", end=" -> ")
                atual = atual.proximo
            print("None")

estados = [
    ("AC", "Acre"), ("AL", "Alagoas"), ("AP", "Amapá"), ("AM", "Amazonas"),
    ("BA", "Bahia"), ("CE", "Ceará"), ("DF", "Distrito Federal"), ("ES", "Espírito Santo"),
    ("GO", "Goiás"), ("MA", "Maranhão"), ("MT", "Mato Grosso"), ("MS", "Mato Grosso do Sul"),
    ("MG", "Minas Gerais"), ("PA", "Pará"), ("PB", "Paraíba"), ("PR", "Paraná"),
    ("PE", "Pernambuco"), ("PI", "Piauí"), ("RJ", "Rio de Janeiro"), ("RN", "Rio Grande do Norte"),
    ("RS", "Rio Grande do Sul"), ("RO", "Rondônia"), ("RR", "Roraima"), ("SC", "Santa Catarina"),
    ("SP", "São Paulo"), ("SE", "Sergipe"), ("TO", "Tocantins")
]

tabela = TabelaHash()

tabela.imprimirTabelaHash()
print(" ")

for sigla, nome in estados:
    tabela.inserirNoInicio(sigla, nome)

tabela.imprimirTabelaHash()
print(" ")

tabela.inserirNoInicio("GC", "Gabriel Borges da Cunha")
tabela.imprimirTabelaHash()
