def sacar(saldo):
    while True:
        saque=int(input("Informe o valor que você deseja sacar: "))
        if (saldo < saque or saque <= 0):
            while True:
                op01=str(input("Valor não disponivel ou inválido. Deseja tentar novamente (sim ou nao)"))
                if (op01 != "sim" and op01 != "nao"):
                        print("Opção invalida, tente no vamente: ")
                elif (op01 != "sim"):
                    return saldo
                else:
                    break
        else:
            print("Saque concluído com sucesso.")
            saldo = saldo - saque
            print(f"Seu novo saldo é de: R$ {saldo:.2f}")
            return saldo

def depositar(saldo):
    while True:
        deposito=int(input("Informe o valor que você deseja depositar: "))
        if (deposito <= 0):
            while True:
                op03=str(input("Deposito inválido. Deseja tenter novamente (sim ou nao)"))
                if (op03 != "sim" and op03 != "nao"):
                    print("Opção invalida, tente novamente: ")
                elif (op03 != "sim"):
                    return saldo
                else:
                    break
        else:
            print("Deposito concluído com sucesso.")
            saldo = saldo + deposito
            print(f"Seu novo saldo é de: R$ {saldo:.2f}")
            return saldo

def saldo_cliente(saldo):
    print(f"Seu saldo atual é de: R$ {saldo:.2f}")
    while True: 
        op04=str(input("Digite (sair) para voltar para o menu. "))
        if (op04 != "sair"):
            print ("Opção invalida, tente novamente.")
        else:
            return

def menu():
    saldo = 100
    print("="*45)
    print("💵 Sejam bem vindos ao banco cesariano. 💵")
    print("="*45)
    while True:
        print("Digite 1 para SAQUE 💸")
        print("Digite 2 para DEPOSITO 💰")
        print("Digite 3 para CONSULTAR SEU SALDO (caso não lembre)")
        print("Digite 4 para SAIR") 
        opcao=int(input("Informe a transação desejada: "))
        
        match opcao:
            case 1:
                saldo = sacar(saldo)

            case 2:
                saldo = depositar(saldo)
    
            case 3:
                saldo_cliente(saldo)
                
            case 4:
                break
menu()