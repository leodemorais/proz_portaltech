import datetime

def obter_ano_atual():
    return datetime.datetime.now().year

while True:
    nome = input("Digite seu nome completo: ")
    ano_nascimento = input("Digite seu ano de nascimento (1922 a 2021): ")

    try:
        ano_nascimento = int(ano_nascimento)

        if 1922 <= ano_nascimento <= 2021:
            idade = obter_ano_atual() - ano_nascimento
            print(f"Nome: {nome}")
            print(f"Idade: {idade} anos")
            break
        else:
            print("Ano de nascimento fora do intervalo válido (1922 a 2021). Tente novamente.")
    except ValueError:
        print("Ano de nascimento inválido. Digite um número válido.")
