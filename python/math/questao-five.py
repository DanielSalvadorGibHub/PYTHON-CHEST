primeira = float(input("Qual foi a primeira nota do aluno? "))
segunda = float(input("Qual foi a segunda nota do aluno? "))
terceira = float(input("Qual foi a terceira nota do aluno? "))
soma = primeira+segunda+terceira
media = soma/3
final = "null"
resultado = False
while resultado == False:
    if media >= 7:
        final = "Aprovado"
        print(f"a sua média nesse trimestre foi {media} logo você foi {final}!")
        resultado = True
    elif media == 6:
        final = "RECUPERAÇÃO"
        print(f"a sua média nesse trimestre foi {media} logo você está em {final}!")
        resultado = True
    elif media <= 5:
        final = "REPROVADO"
        print(f"a sua média nesse trimestre foi {media} logo você foi {final}!")
        resultado = True
print("====== AQUI ESTÃO MAIS DETALHES SOBRE O BOLETIM ========")
print(f"Primeira nota: {primeira} ")
print(f"Segunda nota: {segunda} ")
print(f"Terceira nota: {terceira} ")
print(f"Média geral do curso: {media} ")
print(f"O seu resultado final foi: {final}  ")
print("========================================================")
