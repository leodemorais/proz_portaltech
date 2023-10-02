while True:
    entrada = input("Digite um número par (ou 'sair' para encerrar): ")

    if entrada.lower() == 'sair':
        print("Encerrando o programa.")
        break

    try:
        numero = int(entrada)

        if numero % 2 == 0:
            print(f"Você digitou um número par: {numero}")
        else:
            print("Você digitou um número ímpar. Tente novamente.")
    except ValueError:
        print("Você digitou um caractere inválido. Tente novamente.")
