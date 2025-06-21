# Menu inicial com as opções
print("Bem-Vindo a Loja de Gelados do Gabriel Cunha")
print("-------------------Cardápio--------------------")
print("-----------------------------------------------")
print("--- | Tamanho |  Cupuaçu (CP) | Açaí (AC) | ---")
print("--- |    P    |    R$ 9.00    |  R$11.00  | ---")
print("--- |    M    |    R$ 14.00   |  R$16.00  | ---")
print("--- |    G    |    R$ 18.00   |  R$20.00  | ---")
print("-----------------------------------------------")

# acumulador para armazenar o valor do pedido
valor_total = 0

# Dicionario dos nomes dos sabores
sabores_texto = {"CP": "Cupuaçu", "AC": "Açaí"}

# define as duas opções de sabor e de tamanho, o metodo .upper() serve para que independentemente se o usuario digitar s/S ou n/N sempre será lido como S & N
while True:
    sabor = input("Entre com o sabor desejado (CP/AC):").upper()
    if sabor not in ["CP", "AC", ]:
        print("Sabor inválido. Tente novamente.\n")
        continue

    tamanho = input("Entre com o tamanho desejado (P/M/G):").upper()
    if tamanho not in ["P", "M", "G"]:
        print("Tamanho inválido. Tente novamente.\n")
        continue

    # Aqui define os preços para cada combinação de sabor com tamanho
    if sabor == "CP":
        if tamanho == "P":
            valor = 9.00
        elif tamanho == "M":
            valor = 14.00
        elif tamanho == "G":
            valor = 18.00
    elif sabor == "AC":
        if tamanho == "P":
            valor = 11.00
        elif tamanho == "M":
            valor = 16.00
        elif tamanho == "G":
            valor = 20.00

        # Informa o pedido que foi feito e adiciona o valor no acumulador
    print(f"Você pediu um {sabores_texto[sabor]} no tamanho {tamanho}: R$ {valor:.2f}")
    valor_total += valor

    # Caso tenha mais algo para pedir o codigo retorna a seleção de sabor, se não tiver ele encerra e informa o valor final do pedido
    mais_pedidos = input("Deseja mais alguma coisa? (S/N):").upper()
    if mais_pedidos == "S":
        continue
    else:
        break

print(f'O valor total de seu pedido é: R${valor_total:.2f}')