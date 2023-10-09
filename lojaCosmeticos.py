#Uma nova loja de cosméticos abriu no seu bairro e pediram
# para você elaborar um sistema que imprime na tela na frente
# da loja os novos produtos que chegaram. O sistema da loja já
# tem um array com os produtos, você precisa apenas imprimir
# eles no terminal, um por um.

#Como desafio opcional, tente imprimir cada produto com a frase
# "Temos [produto] à venda!" (ex. "Temos máscaras faciais à venda!").

produtos = ['máscaras faciais', 'batons', 'esmaltes', 'perfumes', 'loções', 'xampus', 'sabonetes', 'delineadores']
for i in range(len(produtos)):
    print("Confira os novos produtos que chegaram!")
    print("Temos", produtos[i], "à venda!")
