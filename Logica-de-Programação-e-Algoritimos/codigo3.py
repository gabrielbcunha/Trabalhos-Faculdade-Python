# Função para escolher o serviço que será realizado
def escolha_servico():
    while True:

        tipo_servico = str(input("Entre com o tipo de serviço desejado\n" + "DIG - Digitação\n" + "ICO - Impressão Colorida\n" + "IPB - Impressão Preto e Branco\n" + "FOT - Fotocópia\n" + ">>")).upper()
        # Cada condição retorna o valor por unidade do serviço
        if tipo_servico == "DIG":
            return 1.10
        elif tipo_servico == "ICO":
            return 1.00
        elif tipo_servico == "IPB":
            return 0.40
        elif tipo_servico == "FOT":
            return 0.20
        else:
            print("Escolha Inválida, enter com o tipo do serviço novamente")

# Função para calcular o desconto com base no número de paginas informado pelo usuario
def num_pagina():
    while True:
        try:
            qnt_pag = int(input("Entre com o número de páginas:"))
            #cada condição retorna a quantidade de páginas e o desconto que o serviço terá
            if qnt_pag < 20:
                return qnt_pag, 0
            elif qnt_pag >= 20 and qnt_pag < 200:
                return qnt_pag, 0.15
            elif qnt_pag >= 200 and qnt_pag < 2000:
                return qnt_pag, 0.20
            elif qnt_pag >= 2000 and qnt_pag < 20000:
                return qnt_pag, 0.25
            elif qnt_pag >= 20000:
                print(
                    "Não aceitamos tantas páginas de uma vez.\n" + "Por favor, entre com o número de páginas novamente.")
        except ValueError:
            print("Por favor, digite um número válido")

# Função para escolher seriviços extras para o pedido
def servico_extra():
    while True:
        try:
            extra = int(input("Deseja adicionar algum serviço?:\n" + "1 - Encadernação Simples - R$ 15.00\n" + "2 - Encadernação Capa Dura - R$ 40.00\n" + "0 - Não desejo mais nada\n" + ">>"))
            #cada condição retorna o valor que será adicionado ao preço
            if extra == 1:
                return 15.00
            elif extra == 2:
                return 40.00
            elif extra == 0:
                return 0
        except ValueError:
            print("Por favor escolha uma opção valida")

# Mensagem de abertura da loja
print("Bem Vindo a Copiadora do Gabriel Cunha")

#Define as variaveis que armazenam os valores do pedido
valor_servico = escolha_servico()
num_paginas, desconto = num_pagina()
valor_extra = servico_extra()

# Calcula o valor total subtraindo o desconto e adicionando o valor do serviço extra
total_sem_desconto = valor_servico * num_paginas
total_com_desconto = total_sem_desconto - (total_sem_desconto * desconto)
total = total_com_desconto + valor_extra

print(f"Total: R$ {total:.2f} (serviço: {valor_servico:.2f} * páginas: {num_paginas:.2f} - desconto {total_sem_desconto * desconto} + extra: {valor_extra:.2f})")
