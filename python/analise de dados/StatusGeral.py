#Vai exibir todos os dados/valores em uma forma geral de uma coluna com informações principais e criticas:
print(data["COLUNA"].value_counts())
#Vai exibir todos os dados/valores em forma de porcentagem de uma coluna com informações principais e criticas:
print(data["COLUNA"].value_counts(normalize=True).map(f"{:.1%}"))