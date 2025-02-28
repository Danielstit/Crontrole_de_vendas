
vendas = [
    ('20/08/2020', 'iphone x', 'azul', '128gb', 350, 4000),
    ('20/08/2020', 'iphone x', 'prata', '128gb', 1500, 4000),
    ('20/08/2020', 'ipad', 'prata', '256gb', 127, 6000),
    ('20/08/2020', 'ipad', 'prata', '128gb', 981, 5000),
    ('21/08/2020', 'iphone x', 'azul', '128gb', 397, 4000),
    ('21/08/2020', 'iphone x', 'prata', '128gb', 1017, 4000),
    ('21/08/2020', 'ipad', 'prata', '256gb', 50, 6000),
    ('21/08/2020', 'ipad', 'prata', '128gb', 4000, 5000)
]
faturamento_Reais =0
for i , item in enumerate(vendas):
    Data, produto, cor, memoria, Unidades, preco = item
    if Data == '20/08/2020' and produto == 'iphone x':
        faturamento_Reais += Unidades * preco
print("o faturamento do Iphone no dia {} foi de {}R$\n".format(Data,faturamento_Reais))

produrto_mais_vendido = ''
qtde_produto_mais_vendido = 0
cor_produrto_mais_vendido = ''
capaciade_produrto_mais_vendido = ''
for i , item in enumerate(vendas):
    Data, produto, cor, memoria, Unidades, preco = item
    if Data == '21/08/2020':
        if Unidades > qtde_produto_mais_vendido:
            produrto_mais_vendido = produto
            qtde_produto_mais_vendido = Unidades
            cor_produrto_mais_vendido = cor
            capaciade_produrto_mais_vendido = memoria
print("O produto mais vendido foi {} {} {}. Com {} unidades vendidas".format(produrto_mais_vendido,cor_produrto_mais_vendido,
capaciade_produrto_mais_vendido, qtde_produto_mais_vendido))
        