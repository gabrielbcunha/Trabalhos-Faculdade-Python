# Mensagem de abertura e pede para que o usuario insira o valor e a quantidade do produto, definindo que a multiplicação deles é o valor total
print("Bem-vindo a Loja do Gabriel Cunha")
valor_unitario = int(input("Entre com o valor do produto:"))
quantidade = int(input("Entre com a quantidade do produto:"))
valor_total = valor_unitario * quantidade

# Aqui cada condição pega o valor total e calcula pela quantidade se terá desconto, imprimindo no terminal o valor com e sem desconto
if valor_total < 2500:
    desconto = 0
    print(f"O valor SEM desconto: R${valor_total}")
    print(f"O valor Com desconto: R${valor_total}")

elif valor_total >= 2500 and valor_total < 6000:
    desconto = valor_total * 4 / 100
    print(f"O valor SEM desconto: {valor_total}")
    print(f"O valor COM desconto: {valor_total - desconto}")

elif valor_total >= 6000 and valor_total < 10000:
    desconto = valor_total * 7 / 100
    print(f"O valor SEM desconto: {valor_total}")
    print(f"O valor COM desconto: {valor_total - desconto}")

elif valor_total >= 10000:
    desconto = valor_total * 11 / 100
    print(f"O valor SEM desconto: {valor_total}")
    print(f"O valor COM desconto: {valor_total - desconto}")

else:
    print("Insira um valor valido")
