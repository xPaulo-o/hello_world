print("")
print("Selecione a operação:")
print("1. Soma")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")
print("5. Modulo(resto)")
print("6. Exponenciação")
print("0. Sair")


while True:

    print("")
    escolha = float(input("Escolha uma operação: "))

    if escolha != 0:

        if escolha >= 0 and escolha <= 6:

                print("")
                num1 = float(input("Informe o primeiro numero para a operação: "))
                num2 = float(input("Informe o segundo numero para a operação: "))
                print("")

                match escolha:
                    case 1:
                        result = num1 + num2
                        print("A soma dos numeros e: ",result)
                    case 2:
                        result = num1 - num2
                        print("A substração dos numeros e: ",result)
                    case 3:
                        result = num1 * num2
                        print("A multiplicação dos numeros e: ",result)
                    case 4:
                        if num2 == 0:
                            print("Erro! Divisão por zero não é permitida!!")
                        else:
                            result = num1 / num2
                            print("A divisão dos numeros e: ",result)
                    case 5:
                        if num2 == 0:
                            print("Erro! Divisão por zero não é permitida!!")
                        else:
                            result = num1 % num2
                            print("O modulo(resto) dos numeros e: ",result)
                    case 6:
                        result = num1 ** num2
                        print("A exponenciação dos numeros e: ",result)

        else:
            print("")
            print("Informe uma operação valida!!")

    else:
        print("")
        print("Ate logo!!")
        print("")
        break