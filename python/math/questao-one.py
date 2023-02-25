# usuario precisa digitar o número nesse campo:
divisao = int(input("-Digite o número para saber se o número é impar ou par: "))
#agora para determinar se ele é par usamos o operador resto da divisão:
resto = divisao % 2
if resto == 0:
    print(f"-O número escolhido foi {divisao} e ele é par.")
else:
    print(f"-O número escolhido foi {divisao} e ele é impar.")
