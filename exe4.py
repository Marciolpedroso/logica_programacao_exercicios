#Mensagem de boas-vindas com nome e sobrenome.
print('Bem vindo a Empresa do Marcio Pedroso')

# Lista de funcionários (lista de dicionários)
lista_funcionarios = []

# id_global
id_global = 4954536

# Função para cadastrar um novo funcionário
def cadastrar_funcionario(id):
    print("\nCadastro de Funcionário")
    nome = input("Nome: ")
    setor = input("Setor: ")
    salario = input("Salário: ")
    funcionario = {
        "id": id,
        "nome": nome,
        "setor": setor,
        "salario": salario
    }
    # Copia o dicionário para a lista de funcionários
    lista_funcionarios.append(funcionario.copy())
    print(f"Funcionário cadastrado com sucesso! ID: {id}\n")

# Função para consultar funcionários
def consultar_funcionarios():
    while True:
        print("\nConsultar Funcionário")
        print("1. Consultar Todos")
        print("2. Consultar por Id")
        print("3. Consultar por setor")
        print("4. Retornar ao menu")
        opc = input("Escolha uma opção: ")
        if opc == "1":
            print("\n--- Todos os Funcionários ---")
            for func in lista_funcionarios:
                print(f"ID: {func['id']} | Nome: {func['nome']} | Setor: {func['setor']} | Salário: {func['salario']}")
            if not lista_funcionarios:
                print("Nenhum funcionário cadastrado.")
        elif opc == "2":
            id_consulta = input("Digite o ID do funcionário: ")
            encontrado = False
            for func in lista_funcionarios:
                if str(func["id"]) == id_consulta:
                    print(f"ID: {func['id']} | Nome: {func['nome']} | Setor: {func['setor']} | Salário: {func['salario']}")
                    encontrado = True
            if not encontrado:
                print("Funcionário não encontrado.")
        elif opc == "3":
            setor_consulta = input("Digite o setor: ")
            encontrados = [func for func in lista_funcionarios if func["setor"].lower() == setor_consulta.lower()]
            if encontrados:
                for func in encontrados:
                    print(f"ID: {func['id']} | Nome: {func['nome']} | Setor: {func['setor']} | Salário: {func['salario']}")
            else:
                print("Nenhum funcionário encontrado nesse setor.")
        elif opc == "4":
            return  # Retorna ao menu principal
        else:
            print("Opção inválida.")

# Função para remover funcionário
def remover_funcionario():
    while True:
        print("\nRemover Funcionário")
        id_remove = input("Digite o ID do funcionário a ser removido: ")
        for func in lista_funcionarios:
            if str(func["id"]) == id_remove:
                lista_funcionarios.remove(func)
                print(f"Funcionário ID {id_remove} removido com sucesso.")
                return
        print("Id inválido. Tente novamente!")

# ---------------------- MENU PRINCIPAL ----------------------
while True:
    print("\nMenu Principal")
    print("1. Cadastrar Funcionário")
    print("2. Consultar Funcionário")
    print("3. Remover Funcionário")
    print("4. Encerrar Programa")
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        cadastrar_funcionario(id_global)
        id_global += 1  # Incrementa o id_global após cada cadastro
    elif opcao == "2":
        consultar_funcionarios()
    elif opcao == "3":
        remover_funcionario()
    elif opcao == "4":
        print("Encerrando programa...")
        break
    else:
        print("Opção inválida.")