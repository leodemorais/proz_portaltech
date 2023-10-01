
word = "garrafas"

for cerva_num in range(99, 0, -1):
    print(cerva_num, word, "de cerveja na parede.")
    print(cerva_num, word, "de cerva.")
    print("Dê um gole...")
    print("passe adiante.")
    if cerva_num == 1:
        print("Não tem mais cerveja na parede.")
    else:
        new_num = cerva_num - 1
        if new_num == 1:
            word = "garrafa"
        print(new_num, word, "de cerveja na parede.")
    print()
