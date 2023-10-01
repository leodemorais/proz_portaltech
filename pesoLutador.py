#Agrupar lutadores segundo sua categoria de peso

#Recebemos uma lista de lutadores com 2 colunas, uma com o nome e a outra com o peso.

nome = input('Escreva seu nome')
peso = float(input('Digite seu peso'))

#O algoritmo deverá ler cada fileira e escrever o nome do lutador em uma de 3 listas.

if peso > 75:
    print(f'{nome}, sua classificação é a de peso pesado!')

elif peso < 57:
    print(f'{nome}, sua classificação é a de peso pena!')

else:
    print(f'{nome}, sua classificação é a de peso médio!')