def sacar(valor):
    saldo = 500

    if saldo >= valor:
        print("valor sacado!")
        print("Retire o seu dinheiro no caixa.")
    
    print("Obrigado por utilizar nossos serviços, volte sempre.")

def depositar(valor):
    saldo = 500
    saldo += valor

sacar(1000)