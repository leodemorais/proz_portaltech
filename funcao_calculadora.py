def soma(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    if y == 0:
        return "Erro: Divisão por zero"
    return x / y

while True:
    print("Opções:")
    print("1: Soma")
    print("2: Subtração")
    print("3: Multiplicação")
    print("4: Divisão")
    print("0: Sair")

    escolha = input("Digite o número da operação desejada: ")

    if escolha == '0':
        print("Saindo da calculadora.")
        break
    elif escolha in ('1', '2', '3', '4'):
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if escolha == '1':
            print("Resultado:", soma(num1, num2))
        elif escolha == '2':
            print("Resultado:", subtracao(num1, num2))
        elif escolha == '3':
            print("Resultado:", multiplicacao(num1, num2))
        elif escolha == '4':
            resultado = divisao(num1, num2)
            if isinstance(resultado, str):
                print(resultado)
            else:
                print("Resultado:", resultado)
        else:
            print("Essa opção não existe.")
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
