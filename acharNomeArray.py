def achar_elemento(elem, arr):
  achou = False
  comprimento = len(arr)

  for i in range(comprimento):
    if (arr[i] == elem):
      achou = True

  if(achou == True):
    print('Achei o nome: ' + elem)
  else:
     print('Não achei o nome: ' + elem)

nomes = ['Piva', 'Willer', 'Bicelli', 'De Franceschi']
achar_elemento('Piva', nomes)