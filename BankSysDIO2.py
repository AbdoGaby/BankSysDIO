def menu():
    menu_str = """
    ### Bem vindo ao Banco Coding 4F! ###
    ### Selecione a opção desejada: ###

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Novo usuário
    [5] Criar conta
    [6] Listar contas
    [0] Sair
    """
    print(menu_str)
    return input("=>")

def depositar(saldo, novo_deposito):
    if novo_deposito > 0:
        saldo = novo_deposito + saldo
        print(f"Extrato atualizado: {saldo:.2f}")
    else:
        print("Operação inválida! Digite um valor válido!")
    return saldo

def sacar(saldo, novo_saque, limite, LIMITE_SAQUES, numero_saques):
    if numero_saques >= LIMITE_SAQUES or novo_saque > limite:
        print("Limite atingido! Operação cancelada!")
    else:
        saldo -= novo_saque
        numero_saques += 1
        print(f"Seu novo extrato é de {saldo:.2f}")
    return saldo, numero_saques

def exibir_extrato(saldo):
    print(f"Valor atual: {saldo:.2f}")

def criar_usuario(usuarios):
    nome = input("Digite o nome do usuário: ")
    cpf = input("Digite o CPF do usuário: ")
    data_nascimento = input("Digite a data de nascimento do usuário (formato: dd/mm/aaaa): ")
    endereco = input("Digite o endereço do usuário: ")

    if cpf in usuarios:
        print("CPF já cadastrado. Não é possível criar um usuário com CPF duplicado.")
        return None

    usuario = {"nome": nome, "cpf": cpf, "data_nascimento": data_nascimento, "endereco": endereco}
    usuarios[cpf] = usuario
    return usuario

def criar_conta(contas, usuarios):
    cpf_titular = input("Digite o CPF do titular da conta: ")

    if cpf_titular not in usuarios:
        print("CPF não encontrado. Crie um usuário com esse CPF primeiro ou selecione a opção 4 para criar um usuário.")
        return None

    numero_conta = len(contas) + 1  # Cria um número de conta sequencial
    agencia = "0001"
    saldo = 0

    conta = {"numero": numero_conta, "agencia": agencia, "cpf_titular": cpf_titular, "saldo": saldo}
    contas.append(conta)
    return conta

def listar_contas(contas):
    print("Lista de Contas:")
    for conta in contas:
        cpf_titular = conta['cpf_titular']
        print(f"Conta: {conta['numero']} - Agência: {conta['agencia']} - Titular: {cpf_titular}")

def main():
    LIMITE_SAQUES = 3

    numero_saques = 0
    saldo = 0
    limite = 500

    usuarios = {}  # Dicionário para armazenar os usuários (CPF é a chave)
    contas = []    # Lista para armazenar as contas

    while True:
        opcao = menu()
        if opcao == "1":
            print("#Depósito#")
            novo_deposito = float(input("Quanto gostaria de depositar? \n"))
            saldo = depositar(saldo, novo_deposito)

        elif opcao == "2":
            print("#Saque#")
            novo_saque = float(input("Quanto deseja sacar? \n"))
            saldo, numero_saques = sacar(saldo, novo_saque, limite, LIMITE_SAQUES, numero_saques)

        elif opcao == "3":
            print("#Extrato#")
            exibir_extrato(saldo)

        elif opcao == "4":
            print("#Novo Usuário#")
            novo_usuario = criar_usuario(usuarios)
            if novo_usuario:
                print(f"Usuário {novo_usuario['nome']} criado com sucesso!")

        elif opcao == "5":
            print("#Criar Conta#")
            listar_contas(contas)  # Listar contas para facilitar a escolha do CPF
            cpf_titular = input("Digite o CPF do titular da conta: ")
            if cpf_titular not in usuarios:
                print("CPF não encontrado. Crie um usuário com esse CPF primeiro.")
                continue
            criar_conta(contas, usuarios)
            print("Conta criada com sucesso!")

        elif opcao == "6":
            print("#Listar Contas#")
            listar_contas(contas)

        elif opcao == "0":
            print("Obrigada por utilizar nosso sistema!")
            break

        else:
            print("Operação inválida. Selecione novamente a opção desejada.")

main()
