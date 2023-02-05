import random
resultado = False
while resultado == False:
    quest = str(input("Gostaria de jogar o dado? "))
    valor = random.randint(1,20)    
    if quest == "sim":
        if valor <= 9:
            print(f"poxa, o resultado dos dados foi {valor}.")
        elif valor >= 20:
            print(f"Uau, o valor dado foi {valor} ") 
            resultado = True
    else:
        print("Desculpe não vou rolar os dados")
quest2 = str(input("gostaria de jogar novamente?  "))
if quest2 == "sim":
    resultado = False
else:
    print("Obrigado por jogar!")
