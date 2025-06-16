# Mensagem de boas-vindas com nome e sobrenome
print("Bem-vindo a Fabrica de Camisetas de Marcio Pedroso\n")

# Função para escolher o modelo da camiseta
def escolha_modelo():
    while True:
        print("Modelos disponíveis:")
        print("MCS - Manga Curta Simples | Preço: R$1,80")
        print("MLS - Manga Longa Simples | Preço: R$2,10")
        print("MCE - Manga Curta c/ Estampa | Preço: R$2,90")
        print("MLE - Manga Longa c/ Estampa | Preço: R$3,20")
        modelo = input("Digite o modelo desejado (MCS/MLS/MCE/MLE): ").upper()
        if modelo == "MCS":
            return 1.80
        elif modelo == "MLS":
            return 2.10
        elif modelo == "MCE":
            return 2.90
        elif modelo == "MLE":
            return 3.20
        else:
            print("Modelo inválido. Tente novamente!")

# Função para solicitar o número de camisetas e calcular desconto
def num_camisetas():
    while True:
        try:
            n = int(input("Digite o número de camisetas desejadas: "))
            if n > 20000:
                print("Quantidade não permitida (máximo 20000). Tente novamente!")
                continue
            elif n < 20:
                desconto = 0
            elif n < 200:
                desconto = 0.05
            elif n < 2000:
                desconto = 0.07
            else: # de 2000 até 20000
                desconto = 0.12
            # Retorna número de camisetas já com desconto aplicado
            return n, desconto
        except ValueError:
            print("Por favor, digite um número inteiro válido.")

# Função para escolher o tipo de frete
def frete():
    while True:
        print("Escolha o tipo de frete:")
        print("0 - Retirar na fábrica (R$0)")
        print("1 - Transportadora (R$100)")
        print("2 - Sedex (R$200)")
        op = input("Digite a opção de frete (0/1/2): ")
        if op == "0":
            return 0
        elif op == "1":
            return 100
        elif op == "2":
            return 200
        else:
            print("Opção inválida. Tente novamente!")

# Código principal (main)
modelo_valor = escolha_modelo()  # valor unitário da camiseta escolhida
quantidade, desconto = num_camisetas()  # número de camisetas e desconto
frete_valor = frete()  # valor do frete

# Calcula o total SEM desconto, aplica o desconto e soma o frete
subtotal = modelo_valor * quantidade
subtotal_com_desconto = subtotal * (1 - desconto)
total = subtotal_com_desconto + frete_valor

# Exibe o total a pagar, com detalhes
print(f"\nResumo do pedido:")
print(f"Valor unitário: R${modelo_valor:.2f}")
print(f"Quantidade: {quantidade}")
print(f"Subtotal: R${subtotal:.2f}")
if desconto > 0:
    print(f"Desconto aplicado: {desconto*100:.0f}%")
    print(f"Subtotal com desconto: R${subtotal_com_desconto:.2f}")
print(f"Frete: R${frete_valor:.2f}")
print(f"Valor total a pagar: R${total:.2f}")