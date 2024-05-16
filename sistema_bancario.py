import textwrap
# Separar as funções existentes de saque, depósito e extrato. Criar duas novas funções: cadastrar usuário (cliente) e cadastrar conta bancária.

def menu():
    menu ="""
    ======================  Menu  ==========================
    
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nc] Nova Conta
    [tc] Listar contas
    [nu Novo usuário
    [q] Sair

    => """
    return input(textwrap.dedent(menu))

def sacar (*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\n Operação falhou! Você não tem saldo o suficiente")

    elif excedeu_limite:
        print("\n Operação falhou! O valor do saque é maior que o valor do limite.")

    elif excedeu_saques:
        print("\n Operação falhou! Limite de saques já alcançado.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n Saque realizado com sucesso!")
    
    else:
        print("\n Operação falhou! O valor informado é inválido")
            
    return saldo, extrato

def depositar (saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n Operação falhou! O valor informado não é válido")

    return saldo, extrato

def mostrar_extrato (saldo, /, *, extrato):
    print("\n ------------------- Extrato --------------------")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print("\n Saldo \t\tR$ {saldo:.2f}")
    print("---------------------------------------------------")
    return None

def cadastrar_usuario (cliente):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, cliente) # type: ignore

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF: @@@")
        return
    
    nome = input("Informe seu nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nº - bairro - cidade/sigla estado): ")

    cliente.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print(" Usuário criado com sucesso!")

def cadastrar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios) # type: ignore

    if usuario:
        print("\n Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\n Usuário não encontrado, fluxo da criação de conta encerrado!")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0 
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES,)
        
        elif opcao == "e":
            mostrar_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            cadastrar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = cadastrar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()
