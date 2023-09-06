preco_produto = float(input("Qual é o preço do produto? R$"))
desconto = preco_produto * 0.05
preco_final = preco_produto - desconto
print("O produto custava R${:.2f}, na promoção com desconto de 5% (R${:.2f}), vai custar R${:.2f}".format(preco_produto,desconto,preco_final))
