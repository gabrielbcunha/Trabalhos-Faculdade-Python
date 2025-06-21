# Lista para armazenar os livros e váriavel global
lista_livro = []
id_global = 0

# Função que cria o menu cadastrar livros
def cadastrar_livro(id):
    print("---------------------------------------------------")
    print("------------- MENU CADASTRAR LIVRO  ---------------")
    print(f"Id do livro: {id}")
    nome = str(input("Por favor entre com o nome do livro:")).lower()
    autor = str(input("Por favor entre com o autor do livro:")).lower()
    editora = str(input("Por favor entre com a editora do livro:")).lower()
    # Armazena os dados informados pelo usuario no dicionário livro e envia para a lista_livro
    livro = {"id": id, "nome": nome, "autor": autor, "editora": editora}
    lista_livro.append(livro)


# Função que cria o menu consultar livro
def consultar_livro():
    while True:
        print("---------------------------------------------------")
        print("------------- MENU CONSULTAR LIVRO  ---------------")
        escolha = int(input(
            "Escolha a opção desejada:\n" + "1 - Consultar Todos os Livros\n" + "2 - Consultar Livro por id\n" + "3 - Consultar Livro(s) por autor\n" + "4 - Retornar\n" + ">>"))
        # busca todos os dicionarios livros na lista lista_livros e os imprime
        if escolha == 1:
            for livro in lista_livro:
                print(
                    f"ID: {livro['id']}\n Nome: {livro['nome']}\n Autor: {livro['autor']}\n Editora: {livro['editora']}\n \n")
                # busca dentro dos dicionarios da lista_livro o id selecionado e se encontrado o imprime
        elif escolha == 2:
            id_consulta = int(input("Digite o ID do livro:"))
            livro_encontrado = False
            for livro in lista_livro:
                if livro["id"] == id_consulta:
                    print(
                        f"ID: {livro['id']}\n Nome: {livro['nome']}\n Autor: {livro['autor']}\n Editora: {livro['editora']}\n \n")
                    livro_encontrado = True
                    break
            if not livro_encontrado:
                print("Livro não encontrado")
                break

                # busca dentro dos dicionarios da lista_livro o autor selecionado e se encontrado os imprime
        elif escolha == 3:

            autor_consulta = input("Digite o Autor do livro:")
            livros_encontrados = [livro for livro in lista_livro if livro["autor"].lower() == autor_consulta.lower()]
            if livros_encontrados:
                for livro in livros_encontrados:
                    print(
                        f"ID: {livro['id']}\nNome: {livro['nome']}\nAutor: {livro['autor']}\nEditora: {livro['editora']}\n")
            else:
                print("Nenhum livro encontrado para esse autor.")
                # encerra esse menu
        elif escolha == 4:
            break

        else:
            print("Opção inválida")

        # Função para remover livro


def remover_livro():
    while True:
        print("---------------------------------------------------")
        print("-------------- MENU REMOVER LIVRO  ----------------")

        try:
            id_removido = int(input("Digite o id do livro a ser removido:"))
            # busca dentro dos dicionarios da lista_livro o id informado e se encontrado remove o dicionario inteiro
            livro_encontrado = False
            for livro in lista_livro:
                if livro['id'] == id_removido:
                    lista_livro.remove(livro)
                    print("Livro removido com sucesso!")
                    livro_encontrado = True
                    break

            if not livro_encontrado:
                print("Livro não encontrado.")

            break
        except ValueError:
            print("Por favor, digite um ID válido")

        # Menu principal


while True:
    print("Bem vindo a livraria do Gabriel Cunha")
    print("---------------------------------------------------")
    print("---------------- MENU PRINCIPAL -------------------")
    escolha = int(input(
        "Escolha a opção desejada:\n" + "1 - Cadastrar Livro\n" + "2 - Consultar Livro(s)\n" + "3 - Remover Livro\n" + "4 - Retornar\n" + ">>"))
    # Cada condição abre a função determinada atribuida
    if escolha == 1:
        id_global += 1
        cadastrar_livro(id_global)

    elif escolha == 2:
        consultar_livro()

    elif escolha == 3:
        remover_livro()

    elif escolha == 4:
        break