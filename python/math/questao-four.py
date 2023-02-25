#digite a nota do aluno:
nota = float(input("-Digite a nota de qualificação do aluno: "))
#começo da serie de condicionais:
#classificação superior:
if nota >= 9.0 and nota <= 10.0:
    print(f"-A classificação do aluno é superior, pois a nota foi: {nota}")
#classificação médio superior:
elif nota >= 7.0 and nota <= 8.9:
    print(f"-A classificação do aluno é médio superior, pois a nota foi: {nota}")
#classificação média:    
elif nota >= 5.0 and nota <= 6.9:
    print(f"-A classificação do aluno é média, pois a nota foi: {nota}")
#classificação médio inferior:
elif nota >=3.0 and nota <= 4.9:
    print(f"-A classificação do aluno é médio inferior, pois a nota foi: {nota}")
#classificação inferior:    
elif nota >= 0.1 and nota <= 2.9:
    print(f"-A classificação do aluno é inferior, pois a nota foi: {nota}")
#classificação sem redimento:
elif nota == 0:
    print(f"-A classificação do aluno é sem rendimento, pois a nota foi: {nota}")
