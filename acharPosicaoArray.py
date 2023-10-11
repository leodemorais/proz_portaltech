def achar_elemento(elemento, array):

    achou = False

    for i in range(len(array)):
        if array[i] == elemento:
            achou = True
            posicao = i
    if achou:
        print("Achamos o elemento", elemento, "na posição", posicao)
    else:
        print("Não encontramos o elemento", elemento)

comida = ["pao", "arroz", "pizza", "bolo", "macarrao", "feijoada"]

achar_elemento("macarrao", comida)