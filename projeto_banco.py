NOME_BANCO = "Banco DioDevs"
LIMITE_SAQUES = 3
limite = 500.00
saldo = 0.0
numero_saques = 0
transacoes = []


texto_menu = f"""

#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨#
#                                                                                                                                      #
#                                                     Bem vindo ao {NOME_BANCO}!                                                       #
#                                                                                                                                      #
#                      * Como podemos ajudá-lo hoje?                                                                                   #
#                                                                                                                                      #
#       [1] Extrato                                                                                                                    #
#                                                                                                                                      #
#       [2] Saque                                                                                                                      #
#                                                                                                                                      #
#       [3] Depósito                                                                                                                   #
#                                                                                                                                      #
#       [0] Sair!                                                                                                                      #
#                                                                                                                                      #
#                                                                                                                                      #
#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨#
"""
print(texto_menu)


def saque(saldo, numero_saques):

    if numero_saques >= LIMITE_SAQUES:
        print("\nNúmero máximo de saques alcançado!\n")
        return saldo, numero_saques
    
    valor_saque = float(input("Digite o valor do saque: R$ "))

    if valor_saque <= 0:
        print("\nOperação falhou! O valor informado é inválido.\n")
        return saldo, numero_saques

    if valor_saque > saldo:
        print("\nSaldo insuficiente para realizar o saque!\n")

    elif valor_saque > limite:
        print("\nO valor do saque não pode ser maior que R$ 500.00!\n")

    else:
        saldo -= valor_saque
        transacoes.append(('saque', valor_saque))
        numero_saques += 1
        print(f"\nSaque de R$ {valor_saque:.2f} realizado com sucesso!")
        print(f"Saldo atual: R${saldo:.2f}\n")

    return saldo, numero_saques


def deposito(saldo):

    valor = float(input("Digite o valor do depósito: R$ "))

    if valor > 0:
        saldo += valor    
        transacoes.append(('deposito', valor))
        print(f"\nDepósito de R$ {valor:.2f} realizado com sucesso!")
        print(f"Saldo atual: R$ {saldo:.2f}\n")
    
    else:
        print("\nOperação falhou! O valor informado é inválido.\n")
    

    return saldo


def extrato(transacoes, saldo):

    print("\nExtrato de Transações:")

    if not transacoes:
        print("Nenhuma transação realizada.\n")

    else:
        for tipo, valor in transacoes:
            if tipo == 'saque':
                print(f"Saque de R$ {valor:.2f}")

            elif tipo == 'deposito':
                print(f"Depósito de R$ {valor:.2f}")
        print(f"\nSaldo atual: R$ {saldo:.2f}\n")


def menu():

    global saldo
    global numero_saques
    while True:

        opcao = input("Digite a opção desejada:\n")
        
        if opcao == "1":
            print("Você selecionou a opção Extrato:\n")
            extrato(transacoes, saldo)

        elif opcao == "2":
            print("Você selecionou a opção Saque:\n")
            saldo, numero_saques = saque(saldo, numero_saques)
        
        elif opcao == "3":
            print("Você selecionou a opção Depósito\n")
            saldo = deposito(saldo)

        elif opcao == "0":
            print("Você selecionou a opção Sair. Até mais!\n")
            break
        
        else:
            print("\nOpção inválida. Tente novamente.\n")

menu()
