import pdf_management

tabelas = pdf_management.extrair_tabela("cotacao_precos.pdf")

lista = []

for i in tabelas.itertuples():
    lista.append({
        "hortalicas": f"{i.hortalicas}",
        "valor_kg" : f"{i.valor_kg}",
        "unidade" : f"{i.unidade}",
        "quilo" : f"{i.kg}",
        "preco_minimo" : f"p{i.preco_minimo}",
        "preco_maximo" : f"{i.preco_maximo}",
        "preco_mais_comum" : f"{i.preco_mais_comum}" 
    })
print(lista)

