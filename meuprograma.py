saldo = 1000  # saldo inicial

while True:
    print("\n=== CAIXA ELETRÔNICO ===")
    print("1 - Ver saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("Seu saldo é: R$", saldo)

    elif opcao == "2":
        valor = float(input("Digite o valor para depositar: "))
        saldo += valor
        print("Depósito realizado!")

    elif opcao == "3":
        valor = float(input("Digite o valor para sacar: "))
        if valor > saldo:
            print("Saldo insuficiente!")
        else:
            saldo -= valor
            print("Saque realizado!")

    elif opcao == "4":
        print("Encerrando sistema...")
        break

    else:
        print("Opção inválida!")