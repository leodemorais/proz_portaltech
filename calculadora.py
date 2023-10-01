def calculadora(num1, num2, operacao):
    if operacao == 1:
        resultado = num1 + num2
    elif operacao == 2:
        resultado = num1 - num2
    elif operacao == 3:
        resultado = num1 * num2
    elif operacao == 4:
        if num2 != 0:
            resultado = num1 / num2
        else:
            print("Erro: Divisão por zero.")
            resultado = 0
    else:
        print("Operação não reconhecida. Use 1 para Soma, 2 para Subtração, 3 para Multiplicação, ou 4 para Divisão.")
        resultado = 0

    return resultado

# Exemplo de uso:
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = int(input("Digite o número da operação (1 para Soma, 2 para Subtração, 3 para Multiplicação, 4 para Divisão): "))

resultado = calculadora(num1, num2, operacao)
print("Resultado:", resultado)
