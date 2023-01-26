#importação da base de dados
#nessa parte é importante que você delete tOdas as informações desnecessarias:
import pandas as pd
data = pd.read_excel("Comercial.xlsx",1)
data = data.drop("DELETAR COLUNA", axis=1)
data = data.drop("DELETAR LINHA", axis=0)
display(data)