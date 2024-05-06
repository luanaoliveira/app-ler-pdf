import tabula
import pandas as pd

lista_tabelas = tabula.read_pdf("cotacao_precos.pdf", pages="all")

print(len(lista_tabelas))

tabela1 = lista_tabelas[0]
tabela1.columns = tabela1.iloc[0]
tabela1[[0,1,2,3,5,6,7]] = tabela1["COTAÇÃO DE PREÇOS / JUAZEIRO BAHIA"].str.split(" ", expand=True )
tabela1 = tabela1.drop("COTAÇÃO DE PREÇOS / JUAZEIRO BAHIA", axis=1)
tabela1 = tabela1[1:]
tabela1.columns = tabela1.iloc[0]
tabela1 = tabela1[1:]
tabela1 = tabela1.drop("COMUM", axis=1)
tabela1 = tabela1.drop("MAIS", axis=1)
tabela1.rename(columns={'MÁXIMO': 'MAIS COMUM'}, inplace = True)
tabela1.rename(columns={'MÍNIMO': 'MÁXIMO'}, inplace = True)
tabela1.rename(columns={'KG': 'MÍNIMO'}, inplace = True)
tabela1.rename(columns={'': 'KG'}, inplace = True)

tabela2 = lista_tabelas[1]
tabela2[[0,1,2,3]] = tabela2["COTAÇÃO DE PREÇOS / JUAZEIRO BAHIA"].str.split(" ", expand=True )
tabela2 = tabela2.drop("COTAÇÃO DE PREÇOS / JUAZEIRO BAHIA", axis=1)
tabela2.columns.values[0] = 'HORTALIÇAS'
tabela2.columns.values[1] = 'MAIS COMUM'
tabela2.columns.values[2] = 'VALOR/Kg'
tabela2.columns.values[3] = 'UNID.'
tabela2.columns.values[4] = 'KG'
tabela2.columns.values[5] = 'MÍNIMO'
tabela2.columns.values[6] = 'MÁXIMO'

tabela2_ordenado = tabela2.reindex(['HORTALIÇAS', 'VALOR/Kg', 'UNID.', 'KG', 'MÍNIMO', 'MÁXIMO', 'MAIS COMUM'], axis=1)

tabela3 = lista_tabelas[2]
tabela3[[0,1,2,3]] = tabela3["COTAÇÃO DE PREÇOS / JUAZEIRO BAHIA"].str.split(" ", expand=True )
tabela3 = tabela3.drop("COTAÇÃO DE PREÇOS / JUAZEIRO BAHIA", axis=1)
tabela3.columns.values[0] = 'HORTALIÇAS'
tabela3.columns.values[1] = 'MAIS COMUM'
tabela3.columns.values[2] = 'VALOR/Kg'
tabela3.columns.values[3] = 'UNID.'
tabela3.columns.values[4] = 'KG'
tabela3.columns.values[5] = 'MÍNIMO'
tabela3.columns.values[6] = 'MÁXIMO'

tabela3_ordenado = tabela3.reindex(['HORTALIÇAS', 'VALOR/Kg', 'UNID.', 'KG', 'MÍNIMO', 'MÁXIMO', 'MAIS COMUM'], axis=1)

tabelas = pd.concat([tabela1, tabela2_ordenado, tabela3_ordenado])

tabelas = tabelas.set_index("HORTALIÇAS")

print(tabelas)


