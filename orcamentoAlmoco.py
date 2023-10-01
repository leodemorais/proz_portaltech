almoco_favorito = "tropeiro"
almoco_preco = 25.50
bebida_favorita = "cerveja"
bebida_preco = 8.80
sobremesa_favorita = "sorvete de chocolate"
sobremesa_preco = 7.20
orcamento = 100


print(almoco_preco + bebida_preco + sobremesa_preco)
total = (almoco_preco + bebida_preco + sobremesa_preco)
print(orcamento - total)

print("Meu almoço hoje foi",almoco_favorito,",",bebida_favorita,"e",sobremesa_favorita)
print("O valor total da conta é de R$",total)
print("Meu orçamento é R$", orcamento)
print("O que sobrou do orçamento foi R$",orcamento-total)

amigos = 3
total = (almoco_preco * amigos) + (bebida_preco * amigos) + (sobremesa_preco * amigos)
print(total)

total_por_pessoa = total / amigos

if(orcamento >= total):
    print("Bora pagar a conta, galeraaaa!")
else:
    print("Deu ruim, esqueci a carteira!")
