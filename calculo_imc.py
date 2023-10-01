# Solicita ao usuário o peso em quilogramas e a altura em metros
peso = float(input("Digite o peso em quilogramas: "))
altura = float(input("Digite a altura em metros: "))

# Calcula o IMC
imc = peso / (altura ** 2)

# Define as faixas de classificação do IMC
if imc < 18.5:
    classificacao = "Abaixo do peso"
elif 18.5 <= imc < 24.9:
    classificacao = "Peso normal"
elif 25 <= imc < 29.9:
    classificacao = "Sobrepeso"
elif 30 <= imc < 34.9:
    classificacao = "Obesidade grau 1"
elif 35 <= imc < 39.9:
    classificacao = "Obesidade grau 2"
else:
    classificacao = "Obesidade grau 3 (mórbida)"

# Exibe o resultado
print(f"Seu IMC é {imc:.2f} e sua classificação é: {classificacao}")
