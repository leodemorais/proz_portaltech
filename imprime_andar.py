#Precisamos imprimir um número para cada andar de um hotel de 20 andares. Porém, o dono do hotel é supersticioso e optou por não ter um 13ro andar.
#Escreva um código que imprima todos os números exceto o número 13.

for andar in range(1, 21):
    if andar != 13:
        print(andar)


#Escreva mais dois códigos que resolvam o mesmo problema, mas dessa vez usando os outros dois tipos de laços de repetição aprendidos.


andar = 1
while andar <= 20:
    if andar != 13:
        print(andar)
    andar += 1

andar = 1
while True:
    if andar != 13:
        print(andar)
    andar += 1
    if andar > 20:
        break

#Como desafio, imprima eles em ordem decrescente (20, 19, 18...)

andar = 20
while andar >= 1:
    if andar != 13:
        print(andar)
    andar -= 1

andar = 20
while True:
    if andar != 13:
        print(andar)
    andar -= 1
    if andar < 1:
        break
