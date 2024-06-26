import os

def limpar_terminal():
    os.system('cls')

saldo = 0
LIMITE_SAQUES = 3
max_saque = 500.00
min_deposito = 100.00
text_extrato = '\n================================================\n                Extrato de conta                \n================================================\n'
saques = 0                                                                          

def depositar(valor):
    global saldo
    saldo = saldo + valor
    global text_extrato
    text_extrato += f'\nDeposito Realizado-------> R${valor:.2f}\nSaldo--------------------> R${saldo:.2f}'
                                                                              
def sacar(valor):
    global saldo
    saldo = saldo - valor
    global text_extrato
    text_extrato += f'\nSaque Realizado----------> R${valor:.2f}\nSaldo--------------------> R${saldo:.2f}'

def exibir_extrato():
    limpar_terminal()
    input(f'\n{text_extrato}\n\nSaldo Final--------------> R${saldo:.2f}\n\n================================================\n\nDigite enter para continuar.')
                                                 
def mostrar_menu():
    print("Menu:")
    print("d. Deposito")
    print("s. Saque")
    print("e. Extrato")
    print("q. Sair")

def escolha_menu(opcao):
    if opcao == 'd':
        valor = float(input("\nDigite o valor do deposito: "))
        if valor >= 100:
            depositar(valor)
            input(f"Seu deposito de R${valor:.2f} foi realizado com sucesso!\n\nAperte enter para continuar!")
        else:
            input("Valor abaixo do minimo permitido!\n\nAperte enter para continuar!")
        
    elif opcao == 's':
        global saques
        if saques < LIMITE_SAQUES:
            valor = float(input("\nDigite o valor do saque: "))
            if valor <= saldo:
                sacar(valor)
                input(f"Seu saque de R${valor:.2f} foi realizado com sucesso! \n\nAperte enter para continuar!")
                saques = saques + 1
            else:
                input("Valor indisponivel!\n\nAperte enter para continuar!")
        else:
            input("Quantidades de saques diários excedido!\n\nAperte enter para continuar!")
        
    elif opcao == 'e':
        exibir_extrato()
        
    elif opcao == 'q':
        print("Saindo...")
        return False
    else:
        input("Opção inválida. Tente novamente!\n\nAperte enter para continuar!")
    return True

def main():
    limpar_terminal()
    continuar = True
    while continuar:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")
        continuar = escolha_menu(opcao)
        limpar_terminal()

if __name__ == "__main__":
    main()