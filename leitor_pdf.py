import tabula

lista_tabelas = tabula.read_pdf("cotacao_precos.pdf", pages="all")

print(len(lista_tabelas))

for tabela in lista_tabelas:
    print(tabela)