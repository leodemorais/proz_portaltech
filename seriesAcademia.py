def main():
    #Solicita a quantidade de séries a serem feitas
    numero_series = int(input("Digite a quantidade de séries a serem feitas: "))

    #Define as mensagens para cada série do exercício
    mensagens = [f"Série {i + 1}: Pronto para começar!" for i in range(numero_series)]

    #Loop para cada série
    for mensagem in mensagens:
        input(mensagem) #Aguarda o cliente apertar Enter para marcar o fim da série
        mensagens.remove(mensagem) #Remove a mensagem após o cliente terminar a série

    print("Parabéns, você concluiu todas as séries!")

if __name__ == "__main__":
        main()