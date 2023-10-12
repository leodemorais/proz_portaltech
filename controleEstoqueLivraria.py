estoque = {
    "1": {"titulo": "Macunaíma", "autor": "Mário de Andrade", "quantidade": 10},
    "2": {"titulo": "Pau-Brasil", "autor": "Oswald de Andrade", "quantidade": 5},
    "3": {"titulo": "Cobra Norato", "autor": "Raul Bopp", "quantidade": 7},
}


def listar_livros():
    for livro_id, livro_info in estoque.items():
        print(
            f"{livro_id}: Título: {livro_info['titulo']}, Autor: {livro_info['autor']}, Quantidade: {livro_info['quantidade']}")


def alterar_livro(livro_id, novo_titulo, novo_autor, nova_quantidade):
    if livro_id in estoque:
        estoque[livro_id]["titulo"] = novo_titulo
        estoque[livro_id]["autor"] = novo_autor
        estoque[livro_id]["quantidade"] = nova_quantidade
        print("Livro alterado com sucesso!")
    else:
        print("Livro não encontrado no estoque.")


def adicionar_livro(titulo, autor, quantidade):
    novo_id = str(len(estoque) + 1)
    estoque[novo_id] = {"titulo": titulo, "autor": autor, "quantidade": quantidade}
    print("Livro adicionado com sucesso!")


while True:
    print("\nOpções:")
    print("1 - Listar livros")
    print("2 - Alterar livro")
    print("3 - Adicionar livro")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        listar_livros()
    elif opcao == "2":
        livro_id = input("Digite o ID do livro que deseja alterar: ")
        novo_titulo = input("Novo título: ")
        novo_autor = input("Novo autor: ")
        nova_quantidade = int(input("Nova quantidade: "))
        alterar_livro(livro_id, novo_titulo, novo_autor, nova_quantidade)
    elif opcao == "3":
        titulo = input("Título do novo livro: ")
        autor = input("Autor do novo livro: ")
        quantidade = int(input("Quantidade do novo livro: "))
        adicionar_livro(titulo, autor, quantidade)
    elif opcao == "4":
        break
    else:
        print("Opção inválida. Tente novamente.")
