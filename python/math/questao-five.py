#AQUI ESTÃO PRESENTES AS VARIAVEIS QUE VAMOS USAR PARA DESCOBRIR O RESULTADO DO ALUNO:
primeira = float(input("Qual foi a primeira nota do aluno? "))
segunda = float(input("Qual foi a segunda nota do aluno? "))
terceira = float(input("Qual foi a terceira nota do aluno? "))
#A SOMA TEM QUE SEGUIR A REGRA DE PEMDAS
media = (primeira+segunda+terceira)/3
final = "null"
resultado = False
# APARTIR DESSE PONTO COMEÇAMOS UM LOOP PARA QUE O CÓDIGO NÃO SE ATROPELE.
while resultado == False:
    #AQUI ESTÁ A CONDICIONAL SE O ALUNO FOI APROVADO!
    if media >= 7:
        final = "Aprovado"
        print(f"a sua média nesse trimestre foi {media} logo você foi {final}!")
        resultado = True
    #AQUI ESTÁ A CONDICIONAL SE O ALUNO ESTÁ EM RECUPERAÇÃO!
    elif media == 6:
        final = "RECUPERAÇÃO"
        print(f"a sua média nesse trimestre foi {media} logo você está em {final}!")
        resultado = True
    #AQUI ESTÁ A CONDICIONAL SE O ALUNO REPROVAR
    elif media <= 5:
        final = "REPROVADO"
        print(f"a sua média nesse trimestre foi {media} logo você foi {final}!")
        resultado = True
# QUANDO A VARIAVEL RESULTADO FOR ALTERADA PARA TRUE O LOOP PARA DE RODAR.
#NA SEQUENCIA ELE EXIBE ESSA TELA ONDE TEM INFORMAÇÕES MAIS DETALHADA SOBRE A MÉDIA
print("====== AQUI ESTÃO MAIS DETALHES SOBRE O BOLETIM ========")
print(f"Primeira nota: {primeira} ")
print(f"Segunda nota: {segunda} ")
print(f"Terceira nota: {terceira} ")
print(f"Média geral do curso: {media} ")
print(f"O seu resultado final foi: {final}  ")
print("========================================================")
