def alterarProduto(produto1, produto2, lista):
  achou = False

  for i in range(len(lista)):
    if lista[i] == produto1:
      achou = True
  if (achou == False):
    print("Produto " + produto1 + " não encontrado. Por favor digite novamente.")
  else:
    print("Sucesso. Produto " + produto1 + " substituído por " + produto2 + "\n")
    lista[i] = produto2

def adicionarProduto(produtoAdicional, lista):
  achou = False

  for i in range(len(lista)):
    if lista[i] == produtoAdicional:
      achou = True
  if (achou == False):
    lista.append(produtoAdicional)
    print("Sucesso. Produto " + produtoAdicional + " adicionado ao Estoque.\n")
  else:
    print("Produto " + produtoAdicional + " não pode ser adicionado pois já está existe no estoque. Por favor digite outro produto.")

def checarSeInputString(input):
    try:
        inteiro = int(input)
        return False
    except ValueError:
        try:
            real = float(input)
            return False
        except ValueError:
            return True

estoque = []

def programaEstoque():
  menuValido = False

  while not menuValido:
    try:
      print("Digite o número da opção correspondente:\n 1: Ver Estoque\n 2: Alterar Produto\n 3: Adicionar Produto\n 4: Sair do Programa")
      menu = int(input())
      if (menu < 0) or (menu > 4):
        print("Essa opção não existe\n")
        menu = ""
      elif (menu == 1):
        if (estoque == []):
          print("Estoque ainda sem nenhum produto, por favor utilize o menu 3 e adicione o primeiro produto.\n")
        else :
          print(estoque)
      elif (menu == 2) and (estoque == []):
        print("Nenhum produto a ser alterado pois o estoque está vazio. Por favor utilize o menu 3 e adicione um produto ao estoque.\n")
      elif (menu == 2):
        print("Insira o produto a ser substituido: ")
        produtoSubstituido = input()
        while (checarSeInputString(produtoSubstituido) != True):
          print("Por favor, utilize texto.")
          produtoSubstituido = (input("Insira o produto a ser substituido: "))
        else :
          produtoAdicionado = (input("Insira o produto a ser adicionado: "))
          while (checarSeInputString(produtoAdicionado) != True):
            print("Por favor, utilize texto.")
            produtoAdicionado = (input("Insira o produto a ser adicionado: "))
          else :
            alterarProduto(produtoSubstituido, produtoAdicionado, estoque)
      elif (menu == 3):
        adicionar = (input("Insira o produto a ser adicionado no Estoque. "))
        while (checarSeInputString(adicionar) != True):
          print("Por favor, utilize texto.")
          adicionar = (input("Insira o produto a ser adicionado no Estoque. "))
        else :
          adicionarProduto(adicionar, estoque)
      elif (menu == 4):
        print("Encerrando programa.")
        break

    except ValueError:
      print("Por favor, insira um número válido.")

programaEstoque()
