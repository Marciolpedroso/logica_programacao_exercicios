#Mensagem de boas-vindas com nome da loja.
print("Bem-Vindo à loja do Marcio Pedroso.")

#Entrada de dados do usuário.
valor = float(input("Digite o valor do pedido: "))
parcelas = int(input("Digite a quantidade de parcelas: "))

#Uso de if, else e elif para determinar a taxa de juro.
if parcelas < 4:
    juros = 0 #0% de taxa de juros.
elif parcelas < 6:
    juros = 0.04 #4% de taxa de juros.
elif parcelas < 9:
    juros = 0.08 #8% de taxa de juros.
elif parcelas < 13:
    juros = 0.16 #16% de taxa de juros.
else:
    juros = 0.32 #32% de taxa de juros acima de 13 parcelas.

#Cálculo do valor de cada parcela e do valor total parcelado.
valor_da_parcela = (valor * (1 + juros)) / parcelas
valor_total_parcelado = valor_da_parcela * parcelas

#Resultados
print(f"O valor das parcelas é de R${valor_da_parcela:.2f}")
print(f"O valor total parcelado é de R${valor_total_parcelado:.2f}")


