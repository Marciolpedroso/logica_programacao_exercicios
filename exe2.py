#Boas-vindas a loja e exibição do menu.
print('--------- Bem-Vindo a Loja de Marmitas do Marcio Pedroso ---------')
print('----------------------------- Cardápio ---------------------------')
print('------------------------------------------------------------------')
print('--- |  Tamanho  |  Bife Acebolado(BA)  |  Filé de Frango(FF) | ---')
print('--- |     P     |      R$ 16.00        |       R$ 15.00      | ---')
print('--- |     M     |      R$ 18.00        |       R$ 17.00      | ---')
print('--- |     G     |      R$ 22.00        |       R$ 21.00      | ---')
print('------------------------------------------------------------------')

#Acumulador para o valor total dos pedidos.
total = 0.0

while True:
    # Entrada de dados pelo usuário.
    sabor = input('Entre com o sabor desejado (BA/FF): ').upper()
    if sabor != 'BA' and sabor != 'FF':
        print('Sabor inválido, tente novamente!')
        continue

    tamanho = input('Entre com o tamanho desejado (P/M/G): ').upper()
    if tamanho != 'P' and tamanho != 'M' and tamanho != 'G':
        print('Tamanho inválido, tente novamente!')
        continue

    #Estrutura aninhada para definir o valor de acordo com sabor e tamanho.
    if sabor == "BA":
        if tamanho == "P":
            preco = 16
        elif tamanho == "M":
            preco = 18
        else: #Tamanho G
            preco = 22
    elif sabor == "FF":
        if tamanho == "P":
            preco = 15
        elif tamanho == "M":
            preco = 17
        else: #Tamanho G
            preco = 21

    #Soma ao acumulador o valor do pedido.
    total += preco
    print(f"Você pediu uma marmita de {sabor} tamanho {tamanho} - R${preco:.2f}.")

    #Pergunta se deseja pedir mais alguma coisa.
    mais = input('Deseja pedir mais alguma coisa (S/N)?').upper()
    if mais != "S":
        break #Sai do loop

#Exibe o valor total dos pedidos.
print(f"O valor total dos pedidos é R${total:.2f}")
