#nessa parte os graficos vão ser gerados sobre todas as base de dados
import plotly.express as px
#laço de repetição:
for coluna in data.columns:
    grap= px.histogram(data, x=coluna, color="Coluna", text_auto=True)
    grap.update_yaxes(title = 'Nome desejado para os valores')
    grap.show()