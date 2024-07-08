menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[u] Criar usuario
[c] Criar conta corrente
[l] Listar contas
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
usuarios = []
contas = []
numero_conta = 1
numero_controle = 1


def cadastrar_usuario(numero_controle):
    novo_usuario = {}
    while True:
        novo_usuario = obter_nome_usuario()
        if novo_usuario:
            novo_usuario = obter_data_nascimento(novo_usuario)
            if novo_usuario:
                novo_usuario = obter_cpf(novo_usuario)
                if novo_usuario:
                    novo_usuario = obter_endereco(novo_usuario)
                    if novo_usuario:
                        novo_usuario["numero_controle"] = numero_controle  # Adicionando número de controle
                        usuarios.append(novo_usuario)
                        print(f"Usuário {novo_usuario['nome']} cadastrado com sucesso com número de controle {numero_controle}!")
                        numero_controle += 1  # Incrementando número de controle para o próximo usuário
                        break

def criar_conta_corrente(usuarios):
    if usuarios:  # Verifica se há usuários cadastrados
        numero_controle = int(input("\nDigite o número de controle do usuário para criar a conta: "))
        
        # Busca o usuário pelo número de controle
        usuario_encontrado = None
        for usuario in usuarios:
            if usuario["numero_controle"] == numero_controle:
                usuario_encontrado = usuario
                break
        
        if usuario_encontrado:
            # Lógica para criar a conta corrente
            numero_conta = len(contas) + 1  # Número sequencial da conta
            agencia = "0001"  # Agência fixa
            # Outros detalhes da conta, como saldo inicial, podem ser definidos aqui

            # Criação da conta e associação ao usuário encontrado
            conta = {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario_encontrado, "cpf": usuario_encontrado['cpf']}
            contas.append(conta)  # Adiciona a conta à lista de contas
            print(f"\nConta corrente criada com sucesso para o usuário {usuario_encontrado['nome']}.")

        else:
            print("\nUsuário não encontrado. Verifique o número de controle digitado.")

    else:
        print("\nNão há usuários cadastrados. Cadastre um usuário primeiro.")

def depositar(saldo, extrato):
    valor = float(input("Informe o valor do depósito: "))
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato

def sacar(saldo, extrato, numero_saques, limite, LIMITE_SAQUES):
    valor = float(input("Informe o valor do saque: "))

    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
        return saldo, extrato, numero_saques

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
        return saldo, extrato, numero_saques

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
        return saldo, extrato, numero_saques

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("Saque realizado com sucesso!")
        return saldo, extrato, numero_saques

    else:
        print("Operação falhou! O valor informado é inválido.")
        return saldo, extrato, numero_saques
    
def mostrar_extrato(saldo, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def obter_nome_usuario():
    nome_usuario = input("\nDigíte seu nome completo: ").strip().title()

    if all(digitos.isalpha() or digitos == ' ' for digitos in nome_usuario):
        usuario = {"nome": {nome_usuario}}
        return usuario
        
    else:
        print("\nEntrada inválida! Esse campo só aceita letras")

def obter_data_nascimento(usuario):
            
    data_nascimento = input("\nDigite sua data de nascimento (dd/mm/aaaa): ").strip()

    if len(data_nascimento) == 10 and data_nascimento[2] == '/' and data_nascimento[5] == '/':
        dia, mes, ano = data_nascimento.split('/')
            
        if dia.isdigit() and mes.isdigit() and ano.isdigit():
            dia = int(dia)
            mes = int(mes)
            ano = int(ano)
                
            if 1 <= dia <= 31 and 1 <= mes <= 12 and 1900 <= ano <= 2100:
                usuario["data de nascimento"] = data_nascimento  # Adiciona a data ao dicionário
                return usuario
            else:
                print("\nData de nascimento inválida! Verifique os valores.")
        else:
            print("\nData de nascimento inválida! Use apenas números para dia, mês e ano.")
    else:
        print("\nFormato de data inválido! Use o formato dd/mm/aaaa.")

    nome_usuario = input("\nDigíte seu nome completo: ").strip().title()

    if all(digitos.isalpha() or digitos == ' ' for digitos in nome_usuario):
        usuario = {"nome": {nome_usuario}}
        return usuario
        
    else:
        print("\nEntrada inválida! Esse campo só aceita letras")

def obter_cpf(usuario):

    cpf_usuario = input("\nDigite o número do seu CPF: ").strip()
    cpf_usuario = ''.join([char for char in cpf_usuario if char.isdigit()])

    if len(cpf_usuario) == 11:
        usuario["cpf"] = cpf_usuario
        return usuario
    
    else:
        print("\nCPF inválido! O CPF deve conter 11 dígitos.")

def obter_endereco(usuario):

    endereco_usuario = input("\nDigite o seu endereço atual (rua, número, bairro, cidade/estado): ").strip()
    partes_endereco = endereco_usuario.split(',')

    if len(partes_endereco) == 4:
        rua = partes_endereco[0].strip()
        numero_casa = partes_endereco[1].strip()
        bairro = partes_endereco[2].strip()
        cidade_estado = partes_endereco[3].strip()

        usuario["rua"] = rua
        usuario["numero_casa"] = numero_casa
        usuario["bairro"] = bairro
        usuario["cidade_estado"] = cidade_estado

        return usuario
    else:
        print("\nFormato de endereço inválido! Use o formato 'rua, número, bairro, cidade/estado'.")

def listar_contas(contas):
    for conta in contas:
        print(f"""\
            Agência:{conta['agencia']}
            C/C:{conta['numero_conta']}
            Titular:{conta['usuario']['nome']}
            CPF:{conta['cpf']}
        """)


while True:
    opcao = input(menu)

    if opcao == "d":
        saldo, extrato = depositar(0, "")

    elif opcao == "s":
        saldo, extrato, numero_saques = sacar(saldo=saldo, extrato=extrato, numero_saques=numero_saques, limite=limite, LIMITE_SAQUES=LIMITE_SAQUES)

    elif opcao == "e":
        mostrar_extrato(saldo, extrato)

    elif opcao == "u":
        novo_usuario = cadastrar_usuario(numero_controle=numero_controle)
        if novo_usuario:
            usuarios.append(novo_usuario)
            print("\nUsuário cadastrado com sucesso!")

    elif opcao == "c":
        if usuarios:
            criar_conta_corrente(usuarios)
        else:
            print("\nNão há usuários cadastrados. Cadastre um usuário primeiro.")

    elif opcao == "l":
        listar_contas(contas)

    elif opcao == "q":
        break
    
    else:
        print("\nOperação inválida, por favor selecione novamente a operação desejada.")
