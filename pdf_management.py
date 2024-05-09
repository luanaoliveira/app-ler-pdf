import tabula 
import pandas as pd

def extrair_tabela(path):
    lista_tabelas = tabula.read_pdf(path, pages="all")
    print(len(lista_tabelas))

    # Tabela 1
    tabela1 = lista_tabelas[0]
    tabela1.columns = tabela1.iloc[0]
    tabela1[[0,1,2,3,5,6,7]] = tabela1["COTAÇÃO DE PREÇOS / JUAZEIRO BAHIA"].str.split(" ", expand=True )
    tabela1 = tabela1.drop("COTAÇÃO DE PREÇOS / JUAZEIRO BAHIA", axis=1)
    tabela1 = tabela1[1:]
    tabela1.columns = tabela1.iloc[0]
    tabela1 = tabela1[1:]
    tabela1 = tabela1.drop("COMUM", axis=1)
    tabela1 = tabela1.drop("MAIS", axis=1)

    tabela1.columns = ['hortalicas', 'valor_kg', 'unidade', 'kg', 'preco_minimo', 'preco_maximo', 'preco_mais_comum']

    # Tabela 2 
    tabela2 = lista_tabelas[1]
    tabela2[[0,1,2,3]] = tabela2["COTAÇÃO DE PREÇOS / JUAZEIRO BAHIA"].str.split(" ", expand=True )
    tabela2 = tabela2.drop("COTAÇÃO DE PREÇOS / JUAZEIRO BAHIA", axis=1)

    tabela2.columns = ['hortalicas', 'preco_mais_comum', 'valor_kg', 'unidade', 'kg', 'preco_minimo', 'preco_maximo']

    tabela2_ordenado = tabela2.reindex(['hortalicas', 'valor_kg', 'unidade', 'kg', 'preco_minimo', 'preco_maximo', 'preco_mais_comum'], axis=1)

    # Tabela 3
    tabela3 = lista_tabelas[2]
    tabela3[[0,1,2,3]] = tabela3["COTAÇÃO DE PREÇOS / JUAZEIRO BAHIA"].str.split(" ", expand=True )
    tabela3 = tabela3.drop("COTAÇÃO DE PREÇOS / JUAZEIRO BAHIA", axis=1)

    tabela3.columns = ['hortalicas', 'preco_mais_comum', 'valor_kg', 'unidade', 'kg', 'preco_minimo', 'preco_maximo']

    tabela3_ordenado = tabela3.reindex(['hortalicas', 'valor_kg', 'unidade', 'kg', 'preco_minimo', 'preco_maximo', 'preco_mais_comum'], axis=1)

    # Concatena tabelas
    tabelas = pd.concat([tabela1, tabela2_ordenado, tabela3_ordenado])
    return tabelas
