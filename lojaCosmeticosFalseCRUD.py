# A loja de cosméticos ficou muito feliz com seu trabalho e chamaram você novamente!
# Dessa vez, eles precisam que você atualize o array de produtos.
# Agora, eles estão vendendo rímel ao invés de batons, e cremes hidratantes no lugar de loções.
# Além disso, ficaram sem delineadores, então precisam que você remova ele da lista de produtos.
# Imprima a nova lista no terminal para verificar que as alterações foram realizadas corretamente.
# Como desafio, adicione dois novos produtos da sua escolha à lista.


produtos_loja_cosmeticos = ['máscara facial', 'baton', 'creme para o rosto',
                            'perfume', 'loção', 'xampu', 'sabonete', 'delineador']

# Adicionando dois novos produtos
produtos_loja_cosmeticos.append("rímel")
produtos_loja_cosmeticos.append("creme hidratante")

# Atualizando os produtos conforme as instruções
produtos_loja_cosmeticos[1] = "rímel"  # Substituindo "batom" por "rímel"
produtos_loja_cosmeticos[2] = "creme hidratante"  # Substituindo "creme para o rosto" por "creme hidratante"
produtos_loja_cosmeticos.remove("delineador")  # Removendo "delineador"

# Imprimindo a nova lista de produtos
print("Produtos atualizados da loja de cosméticos:")
for produtos_loja_cosmeticos in produtos_loja_cosmeticos:
    print(f"Temos {produtos_loja_cosmeticos} à venda!")

