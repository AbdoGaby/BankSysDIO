menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opçao = input(menu)

    if opçao == "1":
        print("#Depósito#")
        novo_deposito = float(input("Quanto gostaria de depositar? \n"))
        saldo = novo_deposito + saldo
        print("Extrato atualizado: {}".format(saldo))

    elif opçao == "2":
        
        print("#Saque#")
        novo_saque = float(input("Quanto deseja sacar? \n"))
        
        if numero_saques > LIMITE_SAQUES or novo_saque > limite:
            print("Limite atingido! Operação cancelada!")
        else:
            saldo = saldo - novo_saque
            numero_saques += 1
            print("Seu novo extrato é de {}".format(saldo))

    elif opçao == "3":
        print("#Extrato#")
        print("Valor atual: {}".format(saldo))
    
    elif opçao == "0":
        print("Obrigada por utilizar nosso sistema!")
        break
    else:
        print("Operação inválida. Selecione novamente a opção desejada.")


    